# D:\000_Programs\Python\Python37\python Seed2Key.py
import numpy as np
import traceback 

class Seed2Key_Decoder:
    def __init__(self):
        self.decodedKeyBytes = [0x00,0x00,0x00]
    #  Security access Seed2Key algorithim
    ################################################################################################################
    def Seed2Key(self, recievedSeedBytes):
        SECURITY_MASK = np.uint32(0xEF6FD7)   # Mask for position C. Bytes C21, C16, C13, C6 and C4. (111011110110111111010111)
        SECURITY_POSITION_A_CONSTANT = np.uint32(0xC541A9)   # Position A:3 bytes fixed constants in the specification
        SECURITY_FIXEDBYTES = np.uint64(0x7A03DB3571)   # Position A:3 bytes fixed constants in the specification

        retVal = np.uint32(0x0)        # return value 00,R1,R2,R3
        
        seed = np.uint32(0x0)

        # convert the recievedSeedBytes [0x00,0x00,0x00] into np uint32 type
        
        for i in range(3):
            seed = np.left_shift(seed,8)
            seed = np.bitwise_or(seed,np.uint8(recievedSeedBytes[i]))
            #print("recievedSeedBytes[i]: ", str(hex(recievedSeedBytes[i])))            
        #print("seed Value: ", str(hex(seed)))   
        # np.int_() , c type, long.
        # np.uintc() , c type, unsigned int.
        R1, R2, R3, R_LHS, R_RHS = np.int_(),np.int_(),np.int_(),np.int_(),np.int_()  # final response bytes
        CB_H, CB_L = np.int_(),np.int_() # challenge bytes 
        A = np.int_()  # A initial
        B24, B21, B16, B13, B6, B4 = np.int_(),np.int_(),np.int_(),np.int_(),np.int_(),np.int_() # single bits in lower block 
        C21, C16, C13, C6, C4 = np.int_(),np.int_(),np.int_(),np.int_(),np.int_()  # single bits in upper block

        i = np.uintc()
        CB_32 = np.uint32(0x0)
        S1, S2, S3 =np.uint8(0x0),np.uint8(0x0),np.uint8(0x0)

        # np.right_shift(x1, x2) , Shift the bits of an integer to the right.
        S1 = np.bitwise_and(np.right_shift(seed,16),0xFF)
        S2 = np.bitwise_and(np.right_shift(seed,8),0xFF)
        S3 = np.bitwise_and(seed,0xFF)

        print("current seed byte1 : ", str(hex(S1)),"current seed byte2 : ", str(hex(S2)),"current seed byte3 : ", str(hex(S3)))

        # Calculate last 4 bytes of the challenge number (F5 F4 F3 F2) */
        # CB_H = np.right_shift(SECURITY_FIXEDBYTES,8)
        CB_H = np.uint32(0x7A03DB35)

        # Calculate first 4 bytes of the challenge number (F1 S3 S2 S1) */
        CB_L = (np.bitwise_and(0x71 ,0xFF) * 256) + S3;
        CB_L = (CB_L * 256) + S2;
        CB_L = (CB_L * 256) + S1;  #First 4 bytes of the challenge number (F1 S3 S2 S1) */

        A = SECURITY_POSITION_A_CONSTANT; # 3 bytes initial value, These are fixed constants in the Ford specification */

        i = 0
        CB_32 = CB_L


        ##########################################
        while (i < 64):
            i=i+1
            if (i == 33):
                CB_32 = CB_H

            B24 = np.bitwise_xor(np.bitwise_and(A ,0x01) ,np.bitwise_and(CB_32 ,0x01))

            A = np.right_shift(A,1)
            # printf("\nA first time %X\n", A); */

            A = np.left_shift(B24 ,23) + A
            # printf("\nA second time %X B24 second time %X\n", A, B24); */

            # Position A */
            B21 = np.right_shift(A , 20)
            B21 = np.bitwise_and(B21 , 0x01)
            B16 = np.right_shift(A ,15)
            B16 = np.bitwise_and(B16 , 0x01)
            B13 = np.right_shift(A , 12)
            B13 = np.bitwise_and(B13 , 0x01)
            B6 = np.right_shift(A , 5)
            B6 = np.bitwise_and(B6 , 0x01)
            B4 = np.right_shift(A , 3)
            B4 = np.bitwise_and(B4 , 0x01)

            # Position B */
            C21 = np.bitwise_xor(B24 , B21)
            C21 = np.bitwise_and(C21 , 0x01)
            C16 = np.bitwise_xor(B24 , B16)
            C16 = np.bitwise_and(C16 , 0x01)
            C13 = np.bitwise_xor(B24 , B13)
            C13 = np.bitwise_and(C13 , 0x01)
            C6 = np.bitwise_xor(B24 , B6)
            C6 = np.bitwise_and(C6 , 0x01)
            C4 = np.bitwise_xor(B24 , B4)
            C4 = np.bitwise_and(C4 , 0x01)

            A = np.bitwise_and(A , SECURITY_MASK)

            # Position C */
            A = np.left_shift(C21 , 20) + A
            A = np.left_shift(C16 , 15) + A
            A = np.left_shift(C13 , 12) + A
            A = np.left_shift(C6 , 5) + A
            A = np.left_shift(C4 , 3) + A

            CB_32 = np.right_shift(CB_32 , 1)

        # Calculate R1 */
        R1 = np.bitwise_and(A , 0xFFF)
        R1 = np.right_shift(R1 , 4)

        # Calculate R2 */
        R_RHS = np.right_shift(A , 20)
        R_RHS = np.bitwise_and(R_RHS , 0xF)
        R_LHS = np.right_shift(A , 12)
        R_LHS = np.bitwise_and(R_LHS , 0xF)
        R_LHS = np.left_shift(R_LHS , 4)
        R2 = R_LHS + R_RHS;

        # Calculate R3 */
        R_LHS = np.bitwise_and(A , 0xF)
        R_LHS = np.left_shift(R_LHS , 4)
        R_RHS = np.right_shift(A , 16)
        R_RHS = np.bitwise_and(R_RHS , 0xF)
        R3 = R_LHS + R_RHS;

        #print("A Value: ", str(hex(A)))

        #print("current R1 : ", str(hex(R1)),"current R2 : ", str(hex(R2)),"current R3 : ", str(hex(R3)))

        retVal = np.uintc( (np.left_shift(np.bitwise_and(R1 , 0x000000FF) , 16) | np.left_shift(np.bitwise_and(R2 , 0x000000FF) , 8) | np.bitwise_and(R3 , 0x000000FF)) )
        print("current retVal : ", str(hex(retVal)))
    ##########################################

        # retVal into the decodedKeyBytes[] and return it back
        # highest bytes in the retVal set into 1st position in the list
        for i in range(2,-1,-1):
            self.decodedKeyBytes[i] = np.bitwise_and(retVal,0xFF)
            retVal = np.right_shift(retVal,8)
            #print("current decodedKeyBytes[ ", i,"]hex value: ", str(hex(self.decodedKeyBytes[i])))
        return self.decodedKeyBytes
    #####################################################################################################################

def main():
        recievedSeedBytes = [0x01,0x02,0x03]   # // retVal = 0x4bea02
        recievedSeedBytes1 = [0x44,0x55,0x99]  # // retVal = 0x256bb1
        geely_Seed2Key = Seed2Key_Decoder()
        geely_Seed2Key.Seed2Key(recievedSeedBytes1)
        
if __name__ =='__main__':
    main()