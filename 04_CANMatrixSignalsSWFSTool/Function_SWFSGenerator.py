# SWFSGeneratorFromSignalMappingTable.py
#!/usr/bin/env python
import log
import xlrd
import xlwt
import os

#logger = logging.getLogger(__name__)
logger = log.setup_logger()
# log.set_log_level(logger,0)


class SWFS_SignalInfo():
    def __init__(self, parent=None):
        self.signalSWFSInfoList = list()
        self.signalSWFSInfoDF = []
        self.signalDataTable_nrows = 0
        self.signalDataTable_nclos = 0
        self.filepath = ""


def LoadSignalMappingTable(inputFile):
    signalInfo_SWFS = SWFS_SignalInfo()
    signalDataTable = xlrd.open_workbook(inputFile).sheets()[0]
    signalInfo_SWFS.signalDataTable_nrows = signalDataTable.nrows
    signalInfo_SWFS.signalDataTable_ncols = signalDataTable.ncols
    # logger.debug(signalDataTable.nrows)
    # logger.debug(signalDataTable.ncols)
    # pd_table = pd.read_excel(filePathForWinOS,sheetname=1,header=0,skiprows=None,index_col=None)
    # signalInfo_SWFS.signalSWFSInfoDF = pd.DataFrame(pd_table)
    signalSWFSInfoEntryDict = dict()
    header_data = list()
    cell_data = ''
    # logger.debug(signalInfo_SWFS.signalSWFSInfoDF.head())
    # logger.debug(signalInfo_SWFS.signalSWFSInfoDF.values())
    for j in range(signalDataTable.ncols):
        header_data.append(str(signalDataTable.cell(0, j).value))
    for i in range(1, signalDataTable.nrows):

        for j in range(signalDataTable.ncols):
            logger.debug("i:"+str(i)+"j:"+str(j))
            cell_data = str(signalDataTable.cell(
                i, j).value)
            if cell_data is not None:
                logger.debug("header_data:" + header_data[j] +
                             ",cell_data:" + cell_data+'\n')
                if i >= 1:
                    signalSWFSInfoEntryDict[header_data[j]] = cell_data

        # need to change dict into str type, then add it into the List.
        # otherwise signalSWFSInfoList has the same x dict elements,the same as last dict.
        logger.debug('current SWFSInfoEntryDict:\n')
        logger.debug("i:" + str(i) + "j:" + str(j) + '\n')
        logger.debug(str(signalSWFSInfoEntryDict).encode('utf-8'))
        logger.debug('signalSWFSInfoList is updated:\n')
        signalInfo_SWFS.signalSWFSInfoList.append(str(signalSWFSInfoEntryDict))
    return signalInfo_SWFS


def DumpSWFSExcelSheet(signalInfo_SWFS, outputFolder):
    logger.info('GenerateSWFS clicked.')
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet_ASW = workbook.add_sheet('CAN Matrix SWFS for ASW')
    worksheet_SSP = workbook.add_sheet('CAN Matrix SWFS for SSP')
    worksheet_VAF = workbook.add_sheet('CAN Matrix SWFS for VAF')
    worksheet_Others = workbook.add_sheet('CAN Matrix SWFS for Others')
    worksheets = list()
    worksheets.append(worksheet_ASW)
    worksheets.append(worksheet_SSP)
    worksheets.append(worksheet_VAF)
    worksheets.append(worksheet_Others)
    for i in range(len(worksheets)):
        worksheets[i]._cell_overwrite_ok = True
        worksheets[i].col(0).width = 256*80
        worksheets[i].col(1).width = 256*40
        worksheets[i].col(2).width = 256*50
        worksheets[i].write(0, 0, 'CAN Matrix SWFS detail description')
        worksheets[i].write(0, 1, 'CAN Matrix signal name')
        worksheets[i].write(
            0, 2, 'CAN Matrix signal assigned FunctionOwner')
    swfsDictEntry_spec = ''

    style = xlwt.XFStyle()
    style.alignment.wrap = 1

    logger.info('signalDataTable_nrows: ' +
                str(signalInfo_SWFS.signalDataTable_nrows))
    a = b = c = d = 1
    for i in range(signalInfo_SWFS.signalDataTable_nrows-1):
        swfsDictEntryString = signalInfo_SWFS.signalSWFSInfoList[i]
        swfsDictEntry = dict()
        swfsDictEntry_spec = ''
        swfsDictEntry = eval(swfsDictEntryString)
        logger.debug('swfs record in generation fucntion:    ' +
                     str(swfsDictEntry.keys())+':::'+str(swfsDictEntry.keys()) + '\n')
        if swfsDictEntry.keys() is not None:
            for key in list(swfsDictEntry.keys())[0:20]:
                swfsDictEntry_spec = swfsDictEntry_spec +\
                    str(key)+':  '+str(swfsDictEntry[key])+'\n'
            # swfsDictEntry_spec always use the 1st element in the info List[]
            logger.info('swfs record string:    '+swfsDictEntry_spec+'\n')

            if 'ASW' in str(list(swfsDictEntry.values())[2]):
                worksheet_ASW.write(a, 0, str(swfsDictEntry_spec), style)
                worksheet_ASW.write(
                    a, 1, str(list(swfsDictEntry.values())[1]), style)
                worksheet_ASW.write(
                    a, 2, str(list(swfsDictEntry.values())[2]), style)
                a = a+1
            elif 'SSP' in str(list(swfsDictEntry.values())[2]):
                worksheet_SSP.write(b, 0, str(swfsDictEntry_spec), style)
                worksheet_SSP.write(
                    b, 1, str(list(swfsDictEntry.values())[1]), style)
                worksheet_SSP.write(
                    b, 2, str(list(swfsDictEntry.values())[2]), style)
                b = b+1
            elif 'VAF' in str(list(swfsDictEntry.values())[2]):
                worksheet_VAF.write(c, 0, str(swfsDictEntry_spec), style)
                worksheet_VAF.write(
                    c, 1, str(list(swfsDictEntry.values())[1]), style)
                worksheet_VAF.write(
                    c, 2, str(list(swfsDictEntry.values())[2]), style)
                c = c+1
            else:
                worksheet_Others.write(
                    d, 0, str(swfsDictEntry_spec), style)
                worksheet_Others.write(
                    d, 1, str(list(swfsDictEntry.values())[1]), style)
                worksheet_Others.write(
                    d, 2, str(list(swfsDictEntry.values())[2]), style)
                d = d+1

        else:
            logger.info('null pointer key is found!!')
    if os.path.exists(outputFolder+r'\Generated_CAN_Matrix_SWFS.xls'):
        os.remove(outputFolder+r'\Generated_CAN_Matrix_SWFS.xls')

    workbook.save(outputFolder+r'\Generated_CAN_Matrix_SWFS.xls')
    logger.info('Generation Result',
                'The SWFS used for ASW,VAF,SSP is generated succesfully!!.')


def DumpSWCSExcelSheet(signalInfo_SWFS, outputFolder):
    logger.info('GenerateSWCS clicked.')
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet_NET = workbook.add_sheet('CAN Matrix SWCS for NET')
    worksheet_DSW = workbook.add_sheet('CAN Matrix SWCS for DSW')
    worksheets = list()
    worksheets.append(worksheet_NET)
    worksheets.append(worksheet_DSW)
    for i in range(len(worksheets)):
        worksheets[i]._cell_overwrite_ok = True
        worksheets[i].col(0).width = 256*40
        worksheets[i].col(1).width = 256*40
        worksheets[i].col(2).width = 256*50
        worksheets[i].col(3).width = 256*50
        worksheets[i].write(0, 0, 'CAN Matrix net signal name')

    worksheet_NET.write(0, 1, 'CAN Matrix net signal attributes')
    worksheet_NET.write(
        0, 2, 'CAN Matrix interface and mapping relationship')
    worksheet_DSW.write(0, 1, 'CAN Matrix signal monitoring FW name')
    worksheet_DSW.write(0, 2, 'CAN Matrix signal DSW Node name')
    worksheet_DSW.write(0, 3, 'CAN Matrix signal DSW STM settings')

    style = xlwt.XFStyle()
    style.alignment.wrap = 1
    swcsSignalNetFWAttributes_str = dict()
    for i in range(signalInfo_SWFS.signalDataTable_nrows-1):
        swfsDictEntryString = signalInfo_SWFS.signalSWFSInfoList[i]
        swfsDictEntry = dict()
        swcsSignalNetAttributes = dict()
        swcsSignalAswIfAttributes = dict()
        swcsSignalNetAttributes_str = ''
        swcsSignalAswIfAttributes_str = ''
        swfsDictEntry = eval(swfsDictEntryString)
        for netInfoIndex in range(21, 27):
            netInfoHeader = list(swfsDictEntry.keys())[netInfoIndex]
            netInfoData = list(swfsDictEntry.values())[netInfoIndex]
            swcsSignalNetAttributes[netInfoHeader] = netInfoData

        temp = str(list(swfsDictEntry.values())[1])
        if temp.find('Message:') >=0 :
            swcsSignalNetFWAttributes_str[temp] = list(swfsDictEntry.values())[7]

        AswIfHeader = list(swfsDictEntry.keys())[4]
        AswIfData = list(swfsDictEntry.values())[4]
        swcsSignalAswIfAttributes[AswIfHeader] = AswIfData
        AswIfHeader = list(swfsDictEntry.keys())[5]
        AswIfData = list(swfsDictEntry.values())[5]
        swcsSignalAswIfAttributes[AswIfHeader] = AswIfData
        logger.debug('SWCS record in generation fucntion:    ' +
                     str(swcsSignalNetAttributes)+':::'+str(swcsSignalAswIfAttributes) + '\n')
        for key in swcsSignalNetAttributes.keys():
            key_1 = key
            key_1 = key_1[0: key_1.find('(')]
            swcsSignalNetAttributes_str = swcsSignalNetAttributes_str +\
                str(key_1)+':  '+str(swcsSignalNetAttributes[key])+'\n'
        for key in swcsSignalAswIfAttributes.keys():
            key_1 = key
            key_1 = key_1[0: key_1.find('(')]
            swcsSignalAswIfAttributes_str = swcsSignalAswIfAttributes_str +\
                str(key_1)+':  '+str(swcsSignalAswIfAttributes[key])+'\n'
        # swfsDictEntry_spec always use the 1st element in the info List[]
        logger.info('AswIfAttributes_spec record string:    ' +
                    swcsSignalAswIfAttributes_str+'\n')
        logger.info('SignalNetAttributes record string:    ' +
                    swcsSignalNetAttributes_str+'\n')
# output NET SWCS info into worksheet_NET
# start writing from line 2, keep the table header.
        if str(list(swfsDictEntry.values())[1]).find('CAN_Message:') >= 0:
            worksheet_NET.write(
                    i+1, 0, str(list(swfsDictEntry.values())[1]), style)#MessageName
        else:
            worksheet_NET.write(
                    i+1, 0, str('CAN_Signal: ' + list(swfsDictEntry.values())[1]), style)#SignalName
            worksheet_NET.write(
                    i+1, 1, swcsSignalNetAttributes_str, style)#SignalAttributes
            worksheet_NET.write(
                    i+1, 2, swcsSignalAswIfAttributes_str, style)#Mapping relationship
# output DSW SWCS info into worksheet_DSW
        worksheet_DSW.write(
            i+1, 0, str(list(swfsDictEntry.values())[1]), style)
        worksheet_DSW.write(
            i+1, 1, str(list(swfsDictEntry.values())[7]), style)
        worksheet_DSW.write(
            i+1, 2, str(list(swfsDictEntry.values())[8]), style)
        worksheet_DSW.write(
            i+1, 3, str(list(swfsDictEntry.values())[9]), style)

        #Write NET other Info.
        i = i+2
        #Write Message related monitoring
        worksheet_NET.write(i, 0, 'Frame-/Pdu Monitoring', style); i = i+1
        for key in swcsSignalNetFWAttributes_str.keys():
            worksheet_NET.write(i, 0, str(str(key) + ':\n' + swcsSignalNetFWAttributes_str[key]), style)
            i = i + 1

    if os.path.exists(outputFolder+r'\Generated_CAN_Matrix_SWCS.xls'):
        os.remove(outputFolder+r'\Generated_CAN_Matrix_SWCS.xls')

    workbook.save(outputFolder+r'\Generated_CAN_Matrix_SWCS.xls')
    logger.info('The SWCS for NET & DSW is generated succesfully!!.')


if __name__ == "__main__":
    inputFile = "Gen_CAN_Matrix_Function_Signal_Mapping_00.xls"
    #signalInfo_SWFS = SWFS_SignalInfo()
    #signalInfo_SWFS = LoadSignalMappingTable(inputFile)
    #DumpSWFSExcelSheet(signalInfo_SWFS, "./")
    #DumpSWCSExcelSheet(signalInfo_SWFS, "./")
