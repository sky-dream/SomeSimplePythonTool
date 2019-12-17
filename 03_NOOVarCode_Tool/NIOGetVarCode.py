#NOOGetVarCode.py
#pyinstaller -F NOOGetVarCode.py -w -i Panda_001.ico 
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo,showwarning,showerror
import numpy as np
import traceback                    
class NOOGetVarCode:
    def __init__(self):
        window = Tk()                  
        window.title("NOO F101 Var Code Generation Tool v0.3")   
        window.geometry("800x600+200+200")

        self.frame_Title = Frame(window)         
        self.frame_Title.pack(fill=Y,expand=1)
        self.frame_Product = Frame(window)         
        self.frame_Product.pack(fill=BOTH,expand=1,padx=10)
        self.frame_FunctionControl = Frame(window)         
        self.frame_FunctionControl.pack(fill=BOTH,expand=1)
        self.frame_FunctionInByte08 = Frame(self.frame_FunctionControl)
        #self.frame_FunctionInByte08['bg']  = 'green'       
        self.frame_FunctionInByte08.pack(fill=BOTH ,expand=1,side=LEFT,padx=10)
        self.frame_FunctionInByte09 = Frame(self.frame_FunctionControl)         
        self.frame_FunctionInByte09.pack(fill=BOTH,expand=1,side=LEFT,padx=10)
        #self.frame_FunctionInByte09['bg']  = 'red' 
        self.frame_FunctionInByte10 = Frame(self.frame_FunctionControl)         
        self.frame_FunctionInByte10.pack(fill=BOTH,expand=1,side=RIGHT,padx=10)
        #self.frame_FunctionInByte10['bg']  = 'yellow' 
        self.frame_VehicleVariant = Frame(window)         
        self.frame_VehicleVariant.pack(fill=BOTH,expand=1,padx=10)
        self.frame_F101Value = Frame(window)         
        self.frame_F101Value.pack(fill=BOTH,expand=1,padx=10)
        self.frame_ControlBytesValue = Frame(window)         
        self.frame_ControlBytesValue.pack(fill=BOTH,expand=1,padx=10)        
        self.frame_OperationButton = Frame(window)         
        self.frame_OperationButton.pack(fill=Y,expand=1)
        self.frame_ToolVersion = Frame(window)         
        self.frame_ToolVersion.pack(fill=Y,side=RIGHT)

        self.L_titile = Label(self.frame_Title,text='NOO F101 variant code')
        self.L_titile.config(font='Helvetica -15 bold',fg='blue')
        self.L_titile.pack(fill = X, expand = NO, pady = 10, padx = 10)

        self.L_author = Label(self.frame_ToolVersion, text='ToolVersion: v0.3 Used for BSS05 SP01')
        self.L_author.config(font='Helvetica -10 bold')
        self.L_author.pack( expand=False,side= RIGHT,anchor='e')

        self.L_Product = Label(self.frame_Product,text='Pls choose product type: ')
        self.L_Product.pack(expand=0,side= LEFT,anchor='w')
        self.productType = IntVar()
        self.R_ESP=Radiobutton(self.frame_Product, text="NOO ESP", variable=self.productType, value=1)
        self.R_ESP.pack(expand=0,side= LEFT,anchor='w')  
        self.R_IB2=Radiobutton(self.frame_Product, text="NOO IB2", variable=self.productType, value=2)
        self.R_IB2.pack(expand=0,side= LEFT,anchor='w')

        #function choose
        self.fucntionStatus = {'AEB':IntVar()}
        self.fucntionStatus['AEB'] = IntVar() 
        self.fucntionStatus['ABP'] = IntVar()
        self.fucntionStatus['AWB'] = IntVar()
        self.fucntionStatus['ABA'] = IntVar()
        self.fucntionStatus['ACC'] = IntVar() #checked is 1,unchecked is 0
        self.fucntionStatus['AVH'] = IntVar()
        self.fucntionStatus['BDW'] = IntVar()
        self.fucntionStatus['EBP'] = IntVar()        
        self.fucntionStatus['HBA'] = IntVar()
        self.fucntionStatus['HDC'] = IntVar()
        self.fucntionStatus['HFC'] = IntVar() #checked is 1,unchecked is 0
        self.fucntionStatus['HHC'] = IntVar()
        self.fucntionStatus['HRB'] = IntVar()
        self.fucntionStatus['SCM'] = IntVar()        
        self.fucntionStatus['Autoclosing'] = IntVar()
        self.fucntionStatus['HBB'] = IntVar()
        self.fucntionStatus['APA'] = IntVar()
        self.fucntionStatus['DST'] = IntVar()
        self.functionControlBytes = [0x00,0x00,0x0]

        self.MASK_AEB = 0x80  # VAF setting is in variant data Byte8,Bit7
        self.MASK_ABP = 0x40  # VAF setting is in variant data Byte8,Bit6
        self.MASK_AWB = 0x20  # VAF setting is in variant data Byte8,Bit5
        self.MASK_ABA = 0x10  # VAF setting is in variant data Byte8,Bit4
        self.MASK_ACC = 0x08  # VAF setting is in variant data Byte8,Bit3
        self.MASK_AVH = 0x04  # VAF setting is in variant data Byte8,Bit2
        self.MASK_BDW = 0x02  # VAF setting is in variant data Byte8,Bit1
        self.MASK_EBP = 0x01  # VAF setting is in variant data Byte8,Bit0
        self.MASK_HBA = 0x80  # VAF setting is in variant data Byte9,Bit7
        self.MASK_HDC = 0x40  # VAF setting is in variant data Byte9,Bit6
        self.MASK_HFC = 0x20  # VAF setting is in variant data Byte9,Bit5
        self.MASK_HHC = 0x10  # VAF setting is in variant data Byte9,Bit4
        self.MASK_HRB = 0x08  # VAF setting is in variant data Byte9,Bit3
        self.MASK_SCM = 0x04  # VAF setting is in variant data Byte9,Bit2
        self.MASK_Autoclosing  =  0x02  # VAF setting is in variant data Byte9,Bit1
        self.MASK_HBB = 0x01  # VAF setting is in variant data Byte9,Bit0
        self.MASK_APA = 0x80  # VAF setting is in variant data Byte10,Bit7
        self.MASK_DST = 0x40  # DST(dynamic steering torque) is controlled by Byte10,Bit6.         

        self.L_functionControledInByte08 = Label(self.frame_FunctionInByte08,text='Function InByte08:').pack(fill=Y,expand=0,side=TOP,anchor="nw")
        self.L_functionControledInByte09 = Label(self.frame_FunctionInByte09,text='Function InByte09:').pack(fill=Y,expand=0,side=TOP,anchor="nw")
        self.L_functionControledInByte10 = Label(self.frame_FunctionInByte10,text='Function InByte10:').pack(fill=Y,expand=0,side=TOP,anchor="nw")

        self.checkboxDict = {'AEB':Checkbutton(self.frame_FunctionInByte08)}
        for i in range(8):
            functionName = list(self.fucntionStatus.keys())[i]            
            cmd = 'Checkbutton(self.frame_FunctionInByte08,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack)
        for i in range(8,16):
            functionName = list(self.fucntionStatus.keys())[i]
            
            cmd = 'Checkbutton(self.frame_FunctionInByte09,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack)
        for i in range(16,len(self.fucntionStatus.keys())):
            functionName = list(self.fucntionStatus.keys())[i]
            cmd = 'Checkbutton(self.frame_FunctionInByte10,text=%r, variable=self.fucntionStatus[%r],\
            command=self.getFunctionControlBytes)' % (functionName,functionName)
            cmd_pack = 'self.checkboxDict[functionName].pack(fill=Y,side=TOP,expand=0,anchor="nw")'
            self.checkboxDict[functionName]= eval(cmd)
            eval(cmd_pack)                
        self.checkboxDict['AVH']["text"] = "AVH"

        self.VehicleTypeSet = ("ES6+6","ES6+12","ES8+24")
        self.L_VehicleType = Label(self.frame_VehicleVariant,text='Pls choose vehicle type: ')
        self.L_VehicleType.pack(expand=0,side= LEFT,anchor='w')        
        self.B_VehChoosen = ttk.Combobox (self.frame_VehicleVariant, width = 12, height = 8,)
        self.B_VehChoosen["values"]=(self.VehicleTypeSet)
        self.B_VehChoosen.current("0")
        self.B_VehChoosen.configure(state = "readonly")
        self.B_VehChoosen.pack(expand=0,side= LEFT,anchor='w')

		#set domesticMask to 0x00, no need to use AVH bit flag to distinguish vehicles to be domestic or not as customer request v20190508.
        self.domesticMask=0x00
        self.customerVarcodeStr = StringVar()
        self.customerVarcodeList = [0x08,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x0,0x00,0x0,0x0,0x0,0x0,0x0]
        self.L_customerVarcode = Label(self.frame_F101Value,text='Customer Varcode F101 value: ')
        self.L_customerVarcode.pack(expand=0,side= LEFT,anchor='w')
        self.lebal_varcode = Entry(self.frame_F101Value, textvariable = self.customerVarcodeStr,width=80)
        self.lebal_varcode.pack(expand=0,side= LEFT,anchor='w')

        self.functionControlBytesStr = ""
        self.L_functionControlBytes = Label(self.frame_ControlBytesValue,text='Pls input functionControlByte 8,9,10 hex value(00-ff) in right 3 areas(eg:1f,a3,12): ')
        self.L_functionControlBytes.pack(expand=0,side= LEFT,anchor='w')
        self.lebal_functionControlByte_08 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_08.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_functionControlByte_09 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_09.pack(expand=0,side= LEFT,anchor='w',padx=10)
        self.lebal_functionControlByte_10 = Entry(self.frame_ControlBytesValue, textvariable = self.functionControlBytesStr,width=10)
        self.lebal_functionControlByte_10.pack(expand=0,side= LEFT,anchor='w',padx=10)

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
        for i in range(8):
            functionName = list(self.fucntionStatus.keys())[i]            
            cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
            self.functionControlBytes[0]= self.functionControlBytes[0]+eval(cmd)
        for i in range(8,16):
            functionName = list(self.fucntionStatus.keys())[i]            
            cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
            self.functionControlBytes[1]= self.functionControlBytes[1]+eval(cmd)
        for i in range(16,len(self.fucntionStatus.keys())):
            functionName = list(self.fucntionStatus.keys())[i]            
            cmd = 'self.fucntionStatus[%r].get()*self.MASK_%s' % (functionName,functionName)            
            self.functionControlBytes[2]= self.functionControlBytes[2]+eval(cmd)                         
        functionControlStr = " "
        for x in self.functionControlBytes:
             functionControlStr = functionControlStr + "  "+ str(hex(x))                                

    def genVarcodeList(self):
        if(self.productType.get()==1):
            self.customerVarcodeList[8] = self.functionControlBytes[0]
            self.customerVarcodeList[9] = self.functionControlBytes[1]
            self.customerVarcodeList[10] = self.functionControlBytes[2]
        else:
            self.customerVarcodeList[8] = self.functionControlBytes[0] & self.domesticMask
            self.customerVarcodeList[9] = 0
            self.customerVarcodeList[10] = 0         
        if (str(self.B_VehChoosen.get())=="ES6+6"):
            self.customerVarcodeList[13] =0x11
            self.customerVarcodeList[15] =0x01
        elif (str(self.B_VehChoosen.get())=="ES6+12"):
            self.customerVarcodeList[13] =0x01
            self.customerVarcodeList[15] =0x01
        elif (str(self.B_VehChoosen.get())=="ES8+24"):
            self.customerVarcodeList[13] =0x01
            self.customerVarcodeList[15] =0x00                        

    def genCRCByte(self):
        t_crc = np.uint8(0xFF)
        for i in range(16):
            l_temp = np.uint8(self.customerVarcodeList[i])
            t_crc = np.bitwise_xor(t_crc,l_temp)
            for j in range(8):
                if np.bitwise_and(t_crc,0x80) != 0 :
                    t_crc = np.left_shift(t_crc,1)
                    t_crc = np.uint8(t_crc)
                    t_crc = np.bitwise_and(t_crc,0xFF)
                    t_crc = np.uint8(t_crc)
                    t_crc = np.bitwise_xor(t_crc,0x1D)
                    t_crc = np.uint8(t_crc)
                else:
                    t_crc = np.left_shift(t_crc,1)
                t_crc = np.uint8(t_crc)
        t_crc = np.bitwise_not(t_crc)
        t_crc = np.uint8(t_crc) 
        self.customerVarcodeList[16] = t_crc 
        #print('t_crc: '+str(hex(t_crc)))

    def displayVarCode(self):
        l_VarcodeStr = ""
        self.genVarcodeList()
        self.genCRCByte()
        for v in self.customerVarcodeList:
            v_str=str(hex(v))
            if (len(v_str)!=4):
                l_VarcodeStr=l_VarcodeStr+" "+"0"+v_str[-1:] 
            else:    
                l_VarcodeStr=l_VarcodeStr+" "+v_str[-2:]            
        self.customerVarcodeStr.set(l_VarcodeStr)
    
    def decodeFunctionStatusFromVarcode(self):
        self.recievedControlBytes = [0x00,0x00,0x0]
        try:
            if eval('0x'+self.lebal_functionControlByte_08.get()) not in range(256):
                showwarning('Warning','Byte_08 value is not in the 1 bytehex value range(00-ff)')
            if eval('0x'+self.lebal_functionControlByte_09.get()) not in range(256):
                showwarning('Warning','Byte_09 value is not in the 1 byte hex value range(00-ff)')
            if eval('0x'+self.lebal_functionControlByte_10.get()) not in range(256):
                showwarning('Warning','Byte_10 value is not in the 1 byte hex value range(00-ff)')
            else:
                self.recievedControlBytes[0] = eval('0x'+self.lebal_functionControlByte_08.get())
                self.recievedControlBytes[1] = eval('0x'+self.lebal_functionControlByte_09.get())
                self.recievedControlBytes[2] = eval('0x'+self.lebal_functionControlByte_10.get())
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
                for i in range(16,len(self.fucntionStatus.keys())):
                    functionName = list(self.fucntionStatus.keys())[i]            
                    cmd_1 = 'self.MASK_%s == (self.recievedControlBytes[2]&self.MASK_%s)' % (functionName,functionName)            
                    cmd_2 = 'self.checkboxDict[%r].select()' %(functionName)
                    cmd_3 = 'self.checkboxDict[%r].deselect()' %(functionName)
                    if eval(cmd_1):
                        eval(cmd_2)
                    else:
                        eval(cmd_3)     
        except Exception :
            print(traceback.print_exc())
            showwarning('Warning','Pls input right hex value string(00-ff) of byte 8,9,10(eg:1f,a3,12)')

def main():
    NOOGetVarCode()
    
if __name__ =='__main__':
    main()