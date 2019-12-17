import xml.etree.ElementTree as etree
import os
def get_DTC_name_value(fileName):
	try:
		tree = etree.parse(fileName)
		root = tree.getroot()
		allDTCList = root.find('DTCS').findall('DTC')
		fp = open('z'+fileName.split('.')[-2].split('\\')[-1]+".csv",'w')
		fp.write("")
		fp.write('DTC_name'+';'+ 'DTC_value'+ ';'+ 'DTC_description'+'\n')
		for object_DTC in allDTCList:
			print ('dtc name: '+object_DTC.find('SHORT-NAME').text +';'+ 'DTC value: '+ object_DTC.find('DTC_VALUE').text+'\n')
			fp.write(object_DTC.find('SHORT-NAME').text +';' + object_DTC.find('DTC_VALUE').text+';' + object_DTC.find('DESC').text+'\n')    
		fp.close()
	except:
		print('exception occured in ' + object_DTC.find('SHORT-NAME').text +';')
def getFileNameInCurrentFolder():
	try:	
		fileNameList = []
		#current,subfolder = os.walk(os.getcwd())
		for root, dirs, files in os.walk('.'):
			print('files:  '+str(files)+ '\n')		
			for i in range(len(files)):
				print('root:  '+str(root)+', dirs:  '+str(dirs)+', files:  '+str(files[i])+ '\n')
				fileNameList.append(root+"\\"+files[i])
		#$fileNameList = 	files				
		return 	fileNameList
	except:
		print('exception occured in ' + object_DTC.find('SHORT-NAME').text +';')	
def main():
	try:	
		#filename= 'Diamant__DTC__RB__iBooster.xml'
		#get_DTC_name_value(filename)
		fileNameList = getFileNameInCurrentFolder()
		print('fileNameList: '+str(fileNameList))	
		dtcFileNameList = []
		for i in range(len(fileNameList)):
			if 'Diamant__DTC__' in str(fileNameList[i]) and '.xml' in str(fileNameList[i]):
				dtcFileNameList.append(fileNameList[i])

		for i in range(len(dtcFileNameList)):
				print('dtcFileNameList;  '+str(dtcFileNameList[i]))				
				get_DTC_name_value(dtcFileNameList[i])
	except:
		print('exception occured in ' + object_DTC.find('SHORT-NAME').text +';')			
if __name__=='__main__':
	 main()   