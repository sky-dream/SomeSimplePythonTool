#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyinstaller -F CANMatrixSignalsSWFSTool.py -w -i Panda_001.ico
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView, QApplication, QAction, QMessageBox, QMainWindow, QWidget, QDialog
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QHeaderView
from Pyqt_CANMatrixSignalsSWFSTool import Ui_MainWindow
import sys
import Function_getSWFS_DBC_RW
import Function_SWFSGenerator
from Function_SWFSGenerator import SWFS_SignalInfo
# import pandas as pd
import log
__Author__ = "By: Xueming"
__Copyright__ = "Copyright (c) 2019 Xueming."
__Version__ = "Version 1.0"

logger = log.setup_logger()
log.set_log_level(logger,2)#2:debug
logger.info('Start')

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.dBCInputFilePath = ""
        self.signalMappingTableFolderPath = ""
        self.signalMappingTableFilePath = ""
        self.sWFS_SWCSFolderPath = ""

    @pyqtSlot()
    def on_pushButton_DBCFileInput_clicked(self):
        """
        Slot documentation goes here.
        """
        logger.info('PushButton_DBCFileInput clicked.')
        DBCFile, supported_fileKinds = QFileDialog.getOpenFileName(
            self, u'Open the DBC file', u'./')
        logger.info(DBCFile)
        self.lineEdit_DBCFileIput.setText(DBCFile)
        filePathForWinOS = DBCFile.replace('/', '\\')
        if str(DBCFile)[-4:] == '.dbc' or str(DBCFile)[-4:] == '.DBC':
            logger.info(" -> NET import dbcFile path:", filePathForWinOS)
            # Create an instance of the parser
            self.dBCInputFilePath = filePathForWinOS

            QMessageBox.information(
                self, u'Tips', 'Successful imported from DBC file')
        else:
            QMessageBox.information(
                self, u'Tips', 'The file imported is not a DBC file.')

    @pyqtSlot()
    def on_pushButton_SignalMappingTableOutput_clicked(self):
        """
        Slot documentation goes here.
        """
        logger.info('PushButton_SignalMappingTableOutput clicked.')
        SignalMappingTableOutput, supported_fileKinds = QFileDialog.getOpenFileName(
            self, u'Select the output file', u'./')
        if str(SignalMappingTableOutput)[-4:] == '.xls'or str(SignalMappingTableOutput)[-5:] == '.xlsx':
            self.signalMappingTableFolderPath = SignalMappingTableOutput
            self.lineEdit_SignalMappingTable.setText(SignalMappingTableOutput)
        else:
            QMessageBox.information(
                self, u'Tips', 'Not a xls or xlsx file')

    @pyqtSlot()
    def on_pushButton_GenerateSignalMappingTable_clicked(self):
        """
        Slot documentation goes here.
        """
        logger.info('PushButton_GenerateSignalMappingTable clicked.')
        signalDescriptionFile = self.signalMappingTableFolderPath
        logger.info(signalDescriptionFile)
        filePathForWinOS = signalDescriptionFile.replace('/', '\\')
        # Create an instance of the parser
        NetRE_Parser = Function_getSWFS_DBC_RW.DbcParserClass(self.dBCInputFilePath, filePathForWinOS)
        # Feature 1
        # convert messages and their signals to csv file from dbc file
        i = NetRE_Parser.NetRE_ParsedInformation()
        if i == True:
            QMessageBox.information(
                self, u'Tips', 'Successfully, Gen_Function_Mapping.xls was generated.')
        else:
            QMessageBox.information(
                self, u'Tips', 'Generate Template file failed')

    @pyqtSlot()
    def on_pushButton_SignalMappingTableInput_clicked(self):
        """
        Slot documentation goes here.
        """
        logger.info('PushButton_SignalMappingTableInput  clicked.')
        signalDescriptionFile, supported_fileKinds = QFileDialog.getOpenFileName(
            self, u'Select an excel file', u'./')
        logger.info(signalDescriptionFile)
        filePathForWinOS = signalDescriptionFile.replace('/', '\\')
        if str(signalDescriptionFile)[-4:] == '.xls'or str(signalDescriptionFile)[-5:] == '.xlsx':
            self.signalMappingTableFilePath = filePathForWinOS
            self.lineEdit_SignalMappingTableInput.setText(signalDescriptionFile)
        else:
            QMessageBox.information(
                self, u'Tips', 'The file opened is not an excel file.')

    @pyqtSlot()
    def on_pushButton_SWFS_Output_clicked(self):
        """
        Slot documentation goes here.
        logger.info('pushButton_SWFS_Output_clicked clicked.')
        """
        SWFSOutputFolder = QFileDialog.getExistingDirectory(
            self, u'select the output file folder', u'./')
        self.sWFS_SWCSFolderPath = SWFSOutputFolder
        self.lineEdit_SWFS_Output.setText(SWFSOutputFolder)

    @pyqtSlot()
    def on_pushButton_GenerateSWFSExcelSheet_clicked(self):
        """
        Slot documentation goes here.
        logger.info('pushButton_GenerateSWFSExcelSheet clicked.')
        """
        signalInfo_SWFS = SWFS_SignalInfo()
        signalInfo_SWFS = Function_SWFSGenerator.LoadSignalMappingTable(self.signalMappingTableFilePath)
        Function_SWFSGenerator.DumpSWFSExcelSheet(signalInfo_SWFS,self.sWFS_SWCSFolderPath)
        Function_SWFSGenerator.DumpSWCSExcelSheet(signalInfo_SWFS,self.sWFS_SWCSFolderPath)
        QMessageBox.information(self, u'Tips', 'SWFS SWCS table successfully generated.')



if __name__ == "__main__":
    #resolve Kernel died problem
    if not QtWidgets.QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    app.setApplicationName("CAN Matrix SWFS SWCS Generation Tool")
    window = MainWindow()
    window.setWindowTitle('CAN Matrix SWFS SWCS Generation Tool')
    window.show()
    #sys.exit(app.exec_())
    app.exec_()
