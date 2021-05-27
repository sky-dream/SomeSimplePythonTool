# DCOM_SecurityAccessDecoder.py
# D:\000_Programs\Python\Python37\python DCOM_SecurityAccessDecoder.py
# pyinstaller -F DCOM_SecurityAccessDecoder.py -w -i xxxx.ico
from tkinter import Tk
from tkinter import Frame
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo,showwarning,showerror
import numpy as np
import traceback    
from Seed2Key import Seed2Key_Decoder            
class DCOM_SecurityAccessDecoder:
    def __init__(self):
        window = Tk()                  
        window.title("DCOM Security Access Decoder Tool")   
        window.geometry("800x600+200+200")

        self.frame_Title = Frame(window)         
        self.frame_Title.pack(fill=Y,expand=1)
       
        # get input value
        self.frame_ControlBytesValue = Frame(window)         
        self.frame_ControlBytesValue.pack(fill=BOTH,expand=1,padx=10)  
        # show output value
        self.frame_DecodeOutKeyBytes = Frame(window)         
        self.frame_DecodeOutKeyBytes.pack(fill=BOTH,expand=1,padx=10)
        # control button
        self.frame_OperationButton = Frame(window)         
        self.frame_OperationButton.pack(fill=Y,expand=1)
        self.frame_ToolVersion = Frame(window)         
        self.frame_ToolVersion.pack(fill=Y,side=RIGHT)

        self.L_titile = Label(self.frame_Title,text='DCOM Security Access Decoder Tool')
        self.L_titile.config(font='Helvetica -15 bold',fg='blue')
        self.L_titile.pack(fill = X, expand = NO, pady = 10, padx = 10)

        self.L_author = Label(self.frame_ToolVersion, text='ToolVersion: v0.1')
        self.L_author.config(font='Helvetica -10 bold')
        self.L_author.pack( expand=False,side= RIGHT,anchor='e')

        self.recievedSeedBytes = [0x00,0x00,0x00]
       
        self.decodedKeyBytes = [0xff,0xff,0xff]

        self.L_functionControlBytes = Label(self.frame_ControlBytesValue,text='Pls input the Seed Bytes hex value(00-ff) start from the highest byte: ')
        self.L_functionControlBytes.pack(expand=0,side= LEFT,anchor='w')



        self.DcomControlledFunctionPDMStr = StringVar()
        self.L_KeyBytes = Label(self.frame_DecodeOutKeyBytes,text='Decode out key Bytes hex value start from the highest byte: ')
        self.L_KeyBytes.pack(expand=0,side= LEFT,anchor='w')
        self.lebal_KeyBytes = Entry(self.frame_DecodeOutKeyBytes, textvariable = self.DcomControlledFunctionPDMStr,width=50)
        self.lebal_KeyBytes.pack(expand=0,side= LEFT,anchor='w')

        self.KeyBytesStr = ""

        self.lebal_keyByte_00 = Entry(self.frame_ControlBytesValue, textvariable = self.KeyBytesStr,width=10)
        self.lebal_keyByte_00.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_keyByte_01 = Entry(self.frame_ControlBytesValue, textvariable = self.KeyBytesStr,width=10)
        self.lebal_keyByte_01.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_keyByte_02 = Entry(self.frame_ControlBytesValue, textvariable = self.KeyBytesStr,width=10)
        self.lebal_keyByte_02.pack(expand=0,side= LEFT,anchor='w',padx=10)

        # Button widgets
        self.B_decodeFunctionStatus = Button(self.frame_OperationButton,text="DecodeFunctionStatus",command=\
        self.decodeDCOMPrivateKeyBytes)

        self.B_decodeFunctionStatus.pack(expand=False,side= RIGHT,anchor='e')

        window.mainloop()


    def getDCOMPublicKeyBytes(self):
        
        try:
            if eval('0x'+self.lebal_keyByte_00.get()) not in range(256):
                showwarning('Warning','Byte_00 value is not in the 1 bytehex value range(00-ff)')
            if eval('0x'+self.lebal_keyByte_01.get()) not in range(256):
                showwarning('Warning','Byte_01 value is not in the 1 byte hex value range(00-ff)')
            if eval('0x'+self.lebal_keyByte_02.get()) not in range(256):
                showwarning('Warning','Byte_02 value is not in the 1 byte hex value range(00-ff)')
              
            else:
                self.recievedSeedBytes[0] = eval('0x'+self.lebal_keyByte_00.get())
                self.recievedSeedBytes[1] = eval('0x'+self.lebal_keyByte_01.get())
                self.recievedSeedBytes[2] = eval('0x'+self.lebal_keyByte_02.get())             
                            
        except Exception :
            print(traceback.print_exc())
            showwarning('Warning','Pls input right hex value string(00-ff) of byte 00,01,02(eg:1f,a3,12)')  

    #  Security access Seed2Key algorithim
    ################################################################################################################
    # function moved into class Seed2Key in Seed2Key.py
    #####################################################################################################################


    def displayPrivateKeyBytes(self):
        l_VarcodeStr = ""
        # highest bytes in the retVal set into 1st position in the output
        for v in self.decodedKeyBytes:
            v_str=str(hex(v))

            if (len(v_str)!=4):
                l_VarcodeStr=l_VarcodeStr+" "+"0"+v_str[-1:] 
            else:    
                l_VarcodeStr=l_VarcodeStr+" "+v_str[-2:]            
        self.DcomControlledFunctionPDMStr.set(l_VarcodeStr)
    
    def decodeDCOMPrivateKeyBytes(self):
        self.getDCOMPublicKeyBytes()
        geely_Seed2Key = Seed2Key_Decoder()
        self.decodedKeyBytes = geely_Seed2Key.Seed2Key(self.recievedSeedBytes)
        self.displayPrivateKeyBytes()


def main():
    DCOM_SecurityAccessDecoder()
    
if __name__ =='__main__':
    main()