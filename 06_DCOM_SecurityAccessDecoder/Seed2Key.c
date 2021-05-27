//C:\MTC10Tools\MinGW\V4_6_2\bin\gcc.exe Seed2Key.c
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#define SECURITY_MASK              0xEF6FD7  /* Mask for position C. Bytes C21, C16, C13, C6 and C4. (111011110110111111010111) */
#define SECURITY_POSITION_A_CONSTANT    0xC541A9  /* Position A:3 bytes fixed constants in the specification */
//#define SECURITY_FIXEDBYTES             0x5E4D3C2B1A
//#define SECURITY_FIXEDBYTES             0x43BB42AA41
//#define SECURITY_FIXEDBYTES             0x53414E4F4A
//#define SECURITY_FIXEDBYTES             0xFFFFFFFFFF
#define SECURITY_FIXEDBYTES             0x7A03DB3571

/* Prototype defined to avoid MISRA warning */
uint32_t Seed2Key(uint32_t);

uint32_t Seed2Key(uint32_t seed)
{
    uint32_t retVal; /* return value 00,R1,R2,R3 */

    long int R1, R2, R3, R_LHS, R_RHS, /* final response bytes */
    CB_H, CB_L, /* challenge bytes */
    A, /* A initial */
    B24, B21, B16, B13, B6, B4, /* single bits in lower block */
    C21, C16, C13, C6, C4; /* single bits in upper block */
    //F1, F2, F3, F4, F5;
    int i;
    long int CB_32;
    uint8_t S1, S2, S3;

    S1 = ((seed >> 16) & 0xFF);
    S2 = ((seed >> 8) & 0xFF);
    S3 = (seed & 0xFF);

    /* Calculate last 4 bytes of the challenge number (F5 F4 F3 F2) */
    CB_H = (SECURITY_FIXEDBYTES >> 8);

    /* Calculate first 4 bytes of the challenge number (F1 S3 S2 S1) */
    CB_L = ((SECURITY_FIXEDBYTES & 0xFF) * 256) + S3;
    CB_L = (CB_L * 256) + S2;
    CB_L = (CB_L * 256) + S1; /* First 4 bytes of the challenge number (F1 S3 S2 S1) */

    A = SECURITY_POSITION_A_CONSTANT; /* 3 bytes initial value, These are fixed constants in the Ford specification */

    i = 0;

    CB_32 = CB_L;

    while (i < 64)
    {
        i++;

        if (i == 33)
        {
            CB_32 = CB_H;
        }

        B24 = (A & 0x01) ^ (CB_32 & 0x01);

        A = A >> 1;
        /* printf("\nA first time %X\n", A); */

        A = (B24 << 23) + A;
        /* printf("\nA second time %X B24 second time %X\n", A, B24); */

        /* Position A */
        B21 = (A >> 20);
        B21 = (B21 & 0x01);
        B16 = (A >> 15);
        B16 = (B16 & 0x01);
        B13 = (A >> 12);
        B13 = (B13 & 0x01);
        B6 = (A >> 5);
        B6 = (B6 & 0x01);
        B4 = (A >> 3);
        B4 = (B4 & 0x01);

        /* Position B */
        C21 = B24 ^ B21;
        C21 = C21 & 0x01;
        C16 = B24 ^ B16;
        C16 = C16 & 0x01;
        C13 = B24 ^ B13;
        C13 = C13 & 0x01;
        C6 = B24 ^ B6;
        C6 = C6 & 0x01;
        C4 = B24 ^ B4;
        C4 = C4 & 0x01;

        A &= SECURITY_MASK;

        /* Position C */
        A = (C21 << 20) + A;
        A = (C16 << 15) + A;
        A = (C13 << 12) + A;
        A = (C6 << 5) + A;
        A = (C4 << 3) + A;

        CB_32 = CB_32 >> 1;
    }

    /* Calculate R1 */
    R1 = A & 0xfff;
    R1 = R1 >> 4;

    /* Calculate R2 */
    R_RHS = A >> 20;
    R_RHS = R_RHS & 0xf;
    R_LHS = A >> 12;
    R_LHS = R_LHS & 0xf;
    R_LHS = R_LHS << 4;
    R2 = R_LHS + R_RHS;

    /* Calculate R3 */
    R_LHS = A & 0xf;
    R_LHS = R_LHS << 4;
    R_RHS = A >> 16;
    R_RHS = R_RHS & 0xf;
    R3 = R_LHS + R_RHS;

    retVal = (unsigned int) (((R1 & 0x000000FF) << 16) | ((R2 & 0x000000FF) << 8) | (R3 & 0x000000FF));

    printf("number 100 hex : 0x%x \n",100);
    printf("seed hex : 0x%x \n",seed);
    printf("retVal hex : 0x%x \n",retVal);

    return retVal;
}

int main()
{
    uint32_t seed = 0x00010203;   // retVal = 0x4bea02
    uint32_t seed1 = 0x00445599;  // retVal = 0x256bb1
    uint32_t retVal = Seed2Key(seed1);
    printf("retVal : 0x%x \n",retVal);
    return 0;

}
