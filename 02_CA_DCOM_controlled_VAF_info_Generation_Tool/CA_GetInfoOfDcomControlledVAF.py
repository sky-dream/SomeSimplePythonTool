#CA_GetInfoOfDcomControlledVAF.py
#pyinstaller -F CA_GetInfoOfDcomControlledVAF.py -w -i xxxx.ico
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo,showwarning,showerror
import numpy as np
import traceback                    
class GetInfoOfDcomControlledVAF:
    def __init__(self):
        window = Tk()                  
        window.title("CA DCOM controlled VAF info Generation Tool ")   
        window.geometry("800x600+200+200")

        self.frame_Title = Frame(window)         
        self.frame_Title.pack(fill=Y,expand=1)

        self.frame_FunctionControl = Frame(window)         
        self.frame_FunctionControl.pack(fill=BOTH,expand=1)
        self.frame_FunctionInByte00 = Frame(self.frame_FunctionControl)
        self.frame_FunctionInByte00.pack(fill=BOTH ,expand=1,side=LEFT,padx=10)
        self.frame_FunctionInByte01 = Frame(self.frame_FunctionControl)         
        self.frame_FunctionInByte01.pack(fill=BOTH,expand=1,side=LEFT,padx=10)
        self.frame_FunctionInByte02 = Frame(self.frame_FunctionControl)         
        self.frame_FunctionInByte02.pack(fill=BOTH,expand=1,side=LEFT,padx=10)
        self.frame_FunctionInByte03 = Frame(self.frame_FunctionControl)         
        self.frame_FunctionInByte03.pack(fill=BOTH,expand=1,side=RIGHT,padx=10)        
        self.frame_F101Value = Frame(window)         
        self.frame_F101Value.pack(fill=BOTH,expand=1,padx=10)
        self.frame_ControlBytesValue = Frame(window)         
        self.frame_ControlBytesValue.pack(fill=BOTH,expand=1,padx=10)        
        self.frame_OperationButton = Frame(window)         
        self.frame_OperationButton.pack(fill=Y,expand=1)
        self.frame_ToolVersion = Frame(window)         
        self.frame_ToolVersion.pack(fill=Y,side=RIGHT)

        self.L_titile = Label(self.frame_Title,text='CA DCOM controlled VAF info Generation Tool')
        self.L_titile.config(font='Helvetica -15 bold',fg='blue')
        self.L_titile.pack(fill = X, expand = NO, pady = 10, padx = 10)

        self.L_author = Label(self.frame_ToolVersion, text='ToolVersion: v0.2 used for changan carbon projects')
        self.L_author.config(font='Helvetica -10 bold')
        self.L_author.pack( expand=False,side= RIGHT,anchor='e')


        #function choose
        self.fucntionStatus = {'AutoApply':IntVar()}
        self.fucntionStatus['AutoApply'] = IntVar() 
        self.fucntionStatus['AVH'] = IntVar()
        self.fucntionStatus['HBB'] = IntVar()
        self.fucntionStatus['HDC'] = IntVar()
        self.fucntionStatus['HHC'] = IntVar() #checked is 1，unchecked is 0
        self.fucntionStatus['HSM'] = IntVar()
        self.fucntionStatus['NotUsed_00_01'] = IntVar()
        self.fucntionStatus['NotUsed_00_00'] = IntVar()        
        self.fucntionStatus['NotUsed_01_07'] = IntVar()
        self.fucntionStatus['NotUsed_01_06'] = IntVar()
        self.fucntionStatus['NotUsed_01_05'] = IntVar() #checked is 1，unchecked is 0
        self.fucntionStatus['NotUsed_01_04'] = IntVar()
        self.fucntionStatus['NotUsed_01_03'] = IntVar()
        self.fucntionStatus['NotUsed_01_02'] = IntVar()        
        self.fucntionStatus['NotUsed_01_01'] = IntVar()
        self.fucntionStatus['NotUsed_01_00'] = IntVar()
        self.fucntionStatus['NotUsed_02_07'] = IntVar()
        self.fucntionStatus['NotUsed_02_06'] = IntVar()
        self.fucntionStatus['NotUsed_02_05'] = IntVar() #checked is 1，unchecked is 0
        self.fucntionStatus['NotUsed_02_04'] = IntVar()
        self.fucntionStatus['NotUsed_02_03'] = IntVar()
        self.fucntionStatus['NotUsed_02_02'] = IntVar()        
        self.fucntionStatus['NotUsed_02_01'] = IntVar()
        self.fucntionStatus['NotUsed_02_00'] = IntVar()
        self.fucntionStatus['NotUsed_03_07'] = IntVar()
        self.fucntionStatus['NotUsed_03_06'] = IntVar()
        self.fucntionStatus['NotUsed_03_05'] = IntVar() #checked is 1，unchecked is 0
        self.fucntionStatus['NotUsed_03_04'] = IntVar()
        self.fucntionStatus['NotUsed_03_03'] = IntVar()
        self.fucntionStatus['NotUsed_03_02'] = IntVar()        
        self.fucntionStatus['NotUsed_03_01'] = IntVar()
        self.fucntionStatus['NotUsed_03_00'] = IntVar()        
        #print(self.fucntionStatus.keys())
        self.functionControlBytes = [0x00,0x00,0x0,0x0]

        self.MASK_AutoApply = 0x80  # VAF setting is in Dcom Control data Byte0,Bit7
        self.MASK_AVH = 0x40  # VAF setting is in Dcom Control data Byte0,Bit6
        self.MASK_HBB = 0x20  # VAF setting is in Dcom Control data Byte0,Bit5
        self.MASK_HDC = 0x10  # VAF setting is in Dcom Control data Byte0,Bit4
        self.MASK_HHC = 0x08  # VAF setting is in Dcom Control data Byte0,Bit3
        self.MASK_HSM = 0x04  # VAF setting is in Dcom Control data Byte0,Bit2
        self.MASK_NotUsed_00_01 = 0x02  # VAF setting is in Dcom Control data Byte0,Bit1
        self.MASK_NotUsed_00_00 = 0x01  # VAF setting is in Dcom Control data Byte0,Bit0
        self.MASK_NotUsed_01_07 = 0x80  # VAF setting is in Dcom Control data Byte1,Bit7
        self.MASK_NotUsed_01_06 = 0x40  # VAF setting is in Dcom Control data Byte1,Bit6
        self.MASK_NotUsed_01_05 = 0x20  # VAF setting is in Dcom Control data Byte1,Bit5
        self.MASK_NotUsed_01_04 = 0x10  # VAF setting is in Dcom Control data Byte1,Bit4
        self.MASK_NotUsed_01_03 = 0x08  # VAF setting is in Dcom Control data Byte1,Bit3
        self.MASK_NotUsed_01_02 = 0x04  # VAF setting is in Dcom Control data Byte1,Bit2
        self.MASK_NotUsed_01_01 = 0x02  # VAF setting is in Dcom Control data Byte1,Bit1
        self.MASK_NotUsed_01_00 = 0x01  # VAF setting is in Dcom Control data Byte1,Bit0
        self.MASK_NotUsed_02_07 = 0x80  # VAF setting is in Dcom Control data Byte2,Bit7
        self.MASK_NotUsed_02_06 = 0x40  # VAF setting is in Dcom Control data Byte2,Bit6         
        self.MASK_NotUsed_02_05 = 0x20  # VAF setting is in Dcom Control data Byte2,Bit5
        self.MASK_NotUsed_02_04 = 0x10  # VAF setting is in Dcom Control data Byte2,Bit4
        self.MASK_NotUsed_02_03 = 0x08  # VAF setting is in Dcom Control data Byte2,Bit3
        self.MASK_NotUsed_02_02 = 0x04  # VAF setting is in Dcom Control data Byte2,Bit2
        self.MASK_NotUsed_02_01 = 0x02  # VAF setting is in Dcom Control data Byte2,Bit1
        self.MASK_NotUsed_02_00 = 0x01  # VAF setting is in Dcom Control data Byte2,Bit0
        self.MASK_NotUsed_03_07 = 0x80  # VAF setting is in Dcom Control data Byte3,Bit7
        self.MASK_NotUsed_03_06 = 0x40  # VAF setting is in Dcom Control data Byte3,Bit6         
        self.MASK_NotUsed_03_05 = 0x20  # VAF setting is in Dcom Control data Byte3,Bit5
        self.MASK_NotUsed_03_04 = 0x10  # VAF setting is in Dcom Control data Byte3,Bit4
        self.MASK_NotUsed_03_03 = 0x08  # VAF setting is in Dcom Control data Byte3,Bit3
        self.MASK_NotUsed_03_02 = 0x04  # VAF setting is in Dcom Control data Byte3,Bit2
        self.MASK_NotUsed_03_01 = 0x02  # VAF setting is in Dcom Control data Byte3,Bit1
        self.MASK_NotUsed_03_00 = 0x01  # VAF setting is in Dcom Control data Byte3,Bit0

        self.L_functionControledInByte00 = Label(self.frame_FunctionInByte00,text='Function In Byte00:').pack(fill=Y,expand=0,side=TOP,anchor="nw")
        self.L_functionControledInByte01 = Label(self.frame_FunctionInByte01,text='Function In Byte01:').pack(fill=Y,expand=0,side=TOP,anchor="nw")
        self.L_functionControledInByte02 = Label(self.frame_FunctionInByte02,text='Function In Byte02:').pack(fill=Y,expand=0,side=TOP,anchor="nw")
        self.L_functionControledInByte03 = Label(self.frame_FunctionInByte03,text='Function In Byte03:').pack(fill=Y,expand=0,side=TOP,anchor="nw")

        self.checkboxDict = {'AutoApply':Checkbutton(self.frame_FunctionInByte00)}
        for i in range(8):
            functionName = list(self.fucntionStatus.keys())[i]            
            cmd = 'Checkbutton(self.frame_FunctionInByte00,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack)
        for i in range(8,16):
            functionName = list(self.fucntionStatus.keys())[i]
            
            cmd = 'Checkbutton(self.frame_FunctionInByte01,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack)
        for i in range(16,24):
            functionName = list(self.fucntionStatus.keys())[i]
            cmd = 'Checkbutton(self.frame_FunctionInByte02,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack)                
        for i in range(24,32):
            functionName = list(self.fucntionStatus.keys())[i]
            cmd = 'Checkbutton(self.frame_FunctionInByte03,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack) 

        self.DcomControlledFunctionPDMStr = StringVar()
        self.L_customerVarcode = Label(self.frame_F101Value,text='PDM value based on function status: ')
        self.L_customerVarcode.pack(expand=0,side= LEFT,anchor='w')
        self.lebal_varcode = Entry(self.frame_F101Value, textvariable = self.DcomControlledFunctionPDMStr,width=50)
        self.lebal_varcode.pack(expand=0,side= LEFT,anchor='w')

        self.functionControlBytesStr = ""
        self.L_functionControlBytes = Label(self.frame_ControlBytesValue,text='Pls input functionControlByte 00,01,02,03 hex value(00-ff): ')
        self.L_functionControlBytes.pack(expand=0,side= LEFT,anchor='w')
        self.lebal_functionControlByte_00 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_00.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_functionControlByte_01 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_01.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_functionControlByte_02 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_02.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_functionControlByte_03 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_03.pack(expand=0,side= LEFT,anchor='w',padx=10)

        self.B_getVarCodeValue = Button(self.frame_OperationButton,text="GetVarCodeValue",command=\
        self.displayVarCode)
        self.B_decodeFunctionStatus = Button(self.frame_OperationButton,text="DecodeFunctionStatus",command=\
        self.decodeFunctionStatusFromVarcode)
        self.B_getVarCodeValue.pack(expand=False,side= LEFT,anchor='e')
        self.B_decodeFunctionStatus.pack(expand=False,side= RIGHT,anchor='e')

        window.mainloop()


    def getFunctionControlBytes(self):
        self.functionControlBytes[0] = 0
        self.functionControlBytes[1] = 0
        self.functionControlBytes[2] = 0
        self.functionControlBytes[3] = 0        
        for i in range(8):
            functionName = list(self.fucntionStatus.keys())[i]
            if 'NotUsed' not in functionName:         
                cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
                self.functionControlBytes[0]= self.functionControlBytes[0]+eval(cmd)
            else:
                cmd = 'self.MASK_%s' % (functionName)            
                self.functionControlBytes[0]= self.functionControlBytes[0]+eval(cmd)
        for i in range(8,16):
            functionName = list(self.fucntionStatus.keys())[i]            
            if 'NotUsed' not in functionName:         
                cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
                self.functionControlBytes[1]= self.functionControlBytes[1]+eval(cmd)
            else:
                cmd = 'self.MASK_%s' % (functionName)            
                self.functionControlBytes[1]= self.functionControlBytes[1]+eval(cmd)                
        for i in range(16,24):
            functionName = list(self.fucntionStatus.keys())[i]            
            if 'NotUsed' not in functionName:         
                cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
                self.functionControlBytes[2]= self.functionControlBytes[2]+eval(cmd)
            else:
                cmd = 'self.MASK_%s' % (functionName)            
                self.functionControlBytes[2]= self.functionControlBytes[2]+eval(cmd)            
        for i in range(24,32):
            functionName = list(self.fucntionStatus.keys())[i]            
            if 'NotUsed' not in functionName:         
                cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
                self.functionControlBytes[3]= self.functionControlBytes[3]+eval(cmd)   
            else:
                cmd = 'self.MASK_%s' % (functionName)            
                self.functionControlBytes[3]= self.functionControlBytes[3]+eval(cmd)                                              
        functionControlStr = " "
        for x in self.functionControlBytes:
             functionControlStr = functionControlStr + "  "+ str(hex(x))                               
        #print(functionControlStr)   


    def displayVarCode(self):
        l_VarcodeStr = ""
        self.getFunctionControlBytes()
        for v in self.functionControlBytes:
            v_str=str(hex(v))
            if (len(v_str)!=4):
                l_VarcodeStr=l_VarcodeStr+" "+"0"+v_str[-1:] 
            else:    
                l_VarcodeStr=l_VarcodeStr+" "+v_str[-2:]            
        self.DcomControlledFunctionPDMStr.set(l_VarcodeStr)
    
    def decodeFunctionStatusFromVarcode(self):
        self.recievedControlBytes = [0x00,0x00,0x0,0x0]
        try:
            if eval('0x'+self.lebal_functionControlByte_00.get()) not in range(256):
                showwarning('Warning','Byte_00 value is not in the 1 bytehex value range(00-ff)')
            if eval('0x'+self.lebal_functionControlByte_01.get()) not in range(256):
                showwarning('Warning','Byte_01 value is not in the 1 byte hex value range(00-ff)')
            if eval('0x'+self.lebal_functionControlByte_02.get()) not in range(256):
                showwarning('Warning','Byte_02 value is not in the 1 byte hex value range(00-ff)')
            if eval('0x'+self.lebal_functionControlByte_03.get()) not in range(256):
                showwarning('Warning','Byte_03 value is not in the 1 byte hex value range(00-ff)')                
            else:
                self.recievedControlBytes[0] = eval('0x'+self.lebal_functionControlByte_00.get())
                self.recievedControlBytes[1] = eval('0x'+self.lebal_functionControlByte_01.get())
                self.recievedControlBytes[2] = eval('0x'+self.lebal_functionControlByte_02.get())
                self.recievedControlBytes[3] = eval('0x'+self.lebal_functionControlByte_03.get())                
                for i in range(8):
                    functionName = list(self.fucntionStatus.keys())[i]            
                    cmd_1 = 'self.MASK_%s == (self.recievedControlBytes[0]& self.MASK_%s)' % (functionName,functionName)            
                    cmd_2 = 'self.checkboxDict[%r].select()' %(functionName)
                    cmd_3 = 'self.checkboxDict[%r].deselect()' %(functionName)
                    if eval(cmd_1):
                        eval(cmd_2)
                    else:
                        eval(cmd_3)    
                for i in range(8,16):
                    functionName = list(self.fucntionStatus.keys())[i]            
                    cmd_1 = 'self.MASK_%s == (self.recievedControlBytes[1]&self.MASK_%s)' % (functionName,functionName)            
                    cmd_2 = 'self.checkboxDict[%r].select()' %(functionName)
                    cmd_3 = 'self.checkboxDict[%r].deselect()' %(functionName)
                    if eval(cmd_1):
                        eval(cmd_2)
                    else:
                        eval(cmd_3)
                for i in range(16,24):
                    functionName = list(self.fucntionStatus.keys())[i]            
                    cmd_1 = 'self.MASK_%s == (self.recievedControlBytes[2]&self.MASK_%s)' % (functionName,functionName)            
                    cmd_2 = 'self.checkboxDict[%r].select()' %(functionName)
                    cmd_3 = 'self.checkboxDict[%r].deselect()' %(functionName)
                    if eval(cmd_1):
                        eval(cmd_2)
                    else:
                        eval(cmd_3)
                for i in range(24,32):
                    functionName = list(self.fucntionStatus.keys())[i]            
                    cmd_1 = 'self.MASK_%s == (self.recievedControlBytes[3]&self.MASK_%s)' % (functionName,functionName)            
                    cmd_2 = 'self.checkboxDict[%r].select()' %(functionName)
                    cmd_3 = 'self.checkboxDict[%r].deselect()' %(functionName)
                    if eval(cmd_1):
                        eval(cmd_2)
                    else:
                        eval(cmd_3)                             
        except Exception :
            print(traceback.print_exc())
            showwarning('Warning','Pls input right hex value string(00-ff) of byte 00,01,02,03(eg:1f,a3,12)')

def main():
    GetInfoOfDcomControlledVAF()
    
if __name__ =='__main__':
    main()