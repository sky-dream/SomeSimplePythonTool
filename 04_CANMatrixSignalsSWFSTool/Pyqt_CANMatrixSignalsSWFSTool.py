# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pyqt_CANMatrixSignalsSWFSTool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 350))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_SignalMappingTable = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_SignalMappingTable.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_SignalMappingTable.setReadOnly(True)
        self.lineEdit_SignalMappingTable.setObjectName("lineEdit_SignalMappingTable")
        self.horizontalLayout_5.addWidget(self.lineEdit_SignalMappingTable)
        self.pushButton_SignalMappingTableOutput = QtWidgets.QPushButton(self.tab)
        self.pushButton_SignalMappingTableOutput.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(12)
        self.pushButton_SignalMappingTableOutput.setFont(font)
        self.pushButton_SignalMappingTableOutput.setObjectName("pushButton_SignalMappingTableOutput")
        self.horizontalLayout_5.addWidget(self.pushButton_SignalMappingTableOutput)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_DBCFileIput = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_DBCFileIput.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_DBCFileIput.setReadOnly(True)
        self.lineEdit_DBCFileIput.setObjectName("lineEdit_DBCFileIput")
        self.horizontalLayout_4.addWidget(self.lineEdit_DBCFileIput)
        self.pushButton_DBCFileInput = QtWidgets.QPushButton(self.tab)
        self.pushButton_DBCFileInput.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(12)
        self.pushButton_DBCFileInput.setFont(font)
        self.pushButton_DBCFileInput.setObjectName("pushButton_DBCFileInput")
        self.horizontalLayout_4.addWidget(self.pushButton_DBCFileInput)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.label_title_01 = QtWidgets.QLabel(self.tab)
        self.label_title_01.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_title_01.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(22)
        self.label_title_01.setFont(font)
        self.label_title_01.setObjectName("label_title_01")
        self.gridLayout_2.addWidget(self.label_title_01, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_GenerateSignalMappingTable = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GenerateSignalMappingTable.sizePolicy().hasHeightForWidth())
        self.pushButton_GenerateSignalMappingTable.setSizePolicy(sizePolicy)
        self.pushButton_GenerateSignalMappingTable.setMinimumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(16)
        self.pushButton_GenerateSignalMappingTable.setFont(font)
        self.pushButton_GenerateSignalMappingTable.setObjectName("pushButton_GenerateSignalMappingTable")
        self.gridLayout_2.addWidget(self.pushButton_GenerateSignalMappingTable, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_title_2 = QtWidgets.QLabel(self.tab_2)
        self.label_title_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_title_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(22)
        self.label_title_2.setFont(font)
        self.label_title_2.setObjectName("label_title_2")
        self.gridLayout_3.addWidget(self.label_title_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_SignalMappingTableInput = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_SignalMappingTableInput.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_SignalMappingTableInput.setReadOnly(True)
        self.lineEdit_SignalMappingTableInput.setObjectName("lineEdit_SignalMappingTableInput")
        self.horizontalLayout_6.addWidget(self.lineEdit_SignalMappingTableInput)
        self.pushButton_SignalMappingTableInput = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_SignalMappingTableInput.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(12)
        self.pushButton_SignalMappingTableInput.setFont(font)
        self.pushButton_SignalMappingTableInput.setObjectName("pushButton_SignalMappingTableInput")
        self.horizontalLayout_6.addWidget(self.pushButton_SignalMappingTableInput)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_SWFS_Output = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_SWFS_Output.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_SWFS_Output.setReadOnly(True)
        self.lineEdit_SWFS_Output.setObjectName("lineEdit_SWFS_Output")
        self.horizontalLayout_7.addWidget(self.lineEdit_SWFS_Output)
        self.pushButton_SWFS_Output = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_SWFS_Output.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(12)
        self.pushButton_SWFS_Output.setFont(font)
        self.pushButton_SWFS_Output.setObjectName("pushButton_SWFS_Output")
        self.horizontalLayout_7.addWidget(self.pushButton_SWFS_Output)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.pushButton_GenerateSWFSExcelSheet = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GenerateSWFSExcelSheet.sizePolicy().hasHeightForWidth())
        self.pushButton_GenerateSWFSExcelSheet.setSizePolicy(sizePolicy)
        self.pushButton_GenerateSWFSExcelSheet.setMinimumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(16)
        self.pushButton_GenerateSWFSExcelSheet.setFont(font)
        self.pushButton_GenerateSWFSExcelSheet.setObjectName("pushButton_GenerateSWFSExcelSheet")
        self.gridLayout_3.addWidget(self.pushButton_GenerateSWFSExcelSheet, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Signal Mapping Tabel Folder:"))
        self.pushButton_SignalMappingTableOutput.setText(_translate("MainWindow", "Select"))
        self.label.setText(_translate("MainWindow", "DBC File Input: "))
        self.pushButton_DBCFileInput.setText(_translate("MainWindow", "Select"))
        self.label_title_01.setText(_translate("MainWindow", "Generate Signal Mapping Table From DBC"))
        self.pushButton_GenerateSignalMappingTable.setText(_translate("MainWindow", "Generate Signal Mapping Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "GenerateSignalMappingTableFromDBC"))
        self.label_title_2.setText(_translate("MainWindow", "Generate SWFS From Signal Mapping Table"))
        self.label_3.setText(_translate("MainWindow", "Signal Mapping Table Input: "))
        self.pushButton_SignalMappingTableInput.setText(_translate("MainWindow", "Select"))
        self.label_4.setText(_translate("MainWindow", "SWFS Output Folder:"))
        self.pushButton_SWFS_Output.setText(_translate("MainWindow", "Select"))
        self.pushButton_GenerateSWFSExcelSheet.setText(_translate("MainWindow", "Generate SWFS SWCS Excel Sheet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "GenerateSWFSFromSignalMappingTable"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())