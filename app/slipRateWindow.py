# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Jun 22 21:45:30 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(670, 520)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(10, 51, 261, 181))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(310, 10, 20, 221))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.addOffsetMarkerButton = QtGui.QPushButton(self.centralWidget)
        self.addOffsetMarkerButton.setGeometry(QtCore.QRect(280, 150, 31, 31))
        self.addOffsetMarkerButton.setObjectName(_fromUtf8("addOffsetMarkerButton"))
        self.removeOffsetMarkerButton = QtGui.QPushButton(self.centralWidget)
        self.removeOffsetMarkerButton.setGeometry(QtCore.QRect(280, 190, 31, 31))
        self.removeOffsetMarkerButton.setObjectName(_fromUtf8("removeOffsetMarkerButton"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.nPiecesSpinBox = QtGui.QSpinBox(self.centralWidget)
        self.nPiecesSpinBox.setGeometry(QtCore.QRect(530, 130, 47, 24))
        self.nPiecesSpinBox.setMinimum(2)
        self.nPiecesSpinBox.setMaximum(2)
        self.nPiecesSpinBox.setProperty("value", 2)
        self.nPiecesSpinBox.setObjectName(_fromUtf8("nPiecesSpinBox"))
        self.nItersLineEdit = QtGui.QLineEdit(self.centralWidget)
        self.nItersLineEdit.setGeometry(QtCore.QRect(330, 50, 41, 21))
        self.nItersLineEdit.setObjectName(_fromUtf8("nItersLineEdit"))
        self.nItersLabel = QtGui.QLabel(self.centralWidget)
        self.nItersLabel.setGeometry(QtCore.QRect(380, 50, 59, 16))
        self.nItersLabel.setObjectName(_fromUtf8("nItersLabel"))
        self.zeroOffsetLineEdit = QtGui.QLineEdit(self.centralWidget)
        self.zeroOffsetLineEdit.setGeometry(QtCore.QRect(330, 80, 41, 21))
        self.zeroOffsetLineEdit.setObjectName(_fromUtf8("zeroOffsetLineEdit"))
        self.zeroOffsetLabel = QtGui.QLabel(self.centralWidget)
        self.zeroOffsetLabel.setGeometry(QtCore.QRect(380, 80, 101, 16))
        self.zeroOffsetLabel.setObjectName(_fromUtf8("zeroOffsetLabel"))
        self.randSeedCheckBox = QtGui.QCheckBox(self.centralWidget)
        self.randSeedCheckBox.setGeometry(QtCore.QRect(380, 110, 101, 20))
        self.randSeedCheckBox.setChecked(True)
        self.randSeedCheckBox.setObjectName(_fromUtf8("randSeedCheckBox"))
        self.randSeedLineEdit = QtGui.QLineEdit(self.centralWidget)
        self.randSeedLineEdit.setGeometry(QtCore.QRect(330, 110, 41, 21))
        self.randSeedLineEdit.setObjectName(_fromUtf8("randSeedLineEdit"))
        self.forceIncrCheckBox = QtGui.QCheckBox(self.centralWidget)
        self.forceIncrCheckBox.setGeometry(QtCore.QRect(330, 140, 121, 20))
        self.forceIncrCheckBox.setObjectName(_fromUtf8("forceIncrCheckBox"))
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(490, 50, 20, 131))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.slipRevCheckBox = QtGui.QCheckBox(self.centralWidget)
        self.slipRevCheckBox.setGeometry(QtCore.QRect(330, 160, 101, 20))
        self.slipRevCheckBox.setObjectName(_fromUtf8("slipRevCheckBox"))
        self.linearFitRadio = QtGui.QRadioButton(self.centralWidget)
        self.linearFitRadio.setGeometry(QtCore.QRect(510, 80, 71, 20))
        self.linearFitRadio.setChecked(True)
        self.linearFitRadio.setObjectName(_fromUtf8("linearFitRadio"))
        self.fitTypeButtonGroup = QtGui.QButtonGroup(MainWindow)
        self.fitTypeButtonGroup.setObjectName(_fromUtf8("fitTypeButtonGroup"))
        self.fitTypeButtonGroup.addButton(self.linearFitRadio)
        self.piecewiseFitRadio = QtGui.QRadioButton(self.centralWidget)
        self.piecewiseFitRadio.setGeometry(QtCore.QRect(510, 110, 131, 20))
        self.piecewiseFitRadio.setObjectName(_fromUtf8("piecewiseFitRadio"))
        self.fitTypeButtonGroup.addButton(self.piecewiseFitRadio)
        self.cubicFitRadio = QtGui.QRadioButton(self.centralWidget)
        self.cubicFitRadio.setGeometry(QtCore.QRect(510, 160, 101, 20))
        self.cubicFitRadio.setObjectName(_fromUtf8("cubicFitRadio"))
        self.fitTypeButtonGroup.addButton(self.cubicFitRadio)
        self.runButton = QtGui.QPushButton(self.centralWidget)
        self.runButton.setGeometry(QtCore.QRect(320, 190, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.runButton.setFont(font)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.line_3 = QtGui.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(330, 180, 321, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.cancelButton = QtGui.QPushButton(self.centralWidget)
        self.cancelButton.setGeometry(QtCore.QRect(440, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.importButton = QtGui.QPushButton(self.centralWidget)
        self.importButton.setGeometry(QtCore.QRect(440, 10, 115, 32))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.exportButton = QtGui.QPushButton(self.centralWidget)
        self.exportButton.setGeometry(QtCore.QRect(550, 10, 115, 32))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.line_4 = QtGui.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(10, 225, 651, 31))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(510, 50, 59, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.moveOffsetMarkerDownButton = QtGui.QPushButton(self.centralWidget)
        self.moveOffsetMarkerDownButton.setGeometry(QtCore.QRect(280, 90, 31, 31))
        self.moveOffsetMarkerDownButton.setObjectName(_fromUtf8("moveOffsetMarkerDownButton"))
        self.moveOffsetMarkerUpButton = QtGui.QPushButton(self.centralWidget)
        self.moveOffsetMarkerUpButton.setGeometry(QtCore.QRect(280, 50, 31, 31))
        self.moveOffsetMarkerUpButton.setObjectName(_fromUtf8("moveOffsetMarkerUpButton"))
        self.plotButton = QtGui.QPushButton(self.centralWidget)
        self.plotButton.setGeometry(QtCore.QRect(550, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 249, 651, 261))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "DATA INPUT", None))
        self.label_2.setText(_translate("MainWindow", "Offset Markers", None))
        self.addOffsetMarkerButton.setText(_translate("MainWindow", "+", None))
        self.removeOffsetMarkerButton.setText(_translate("MainWindow", "-", None))
        self.label_3.setText(_translate("MainWindow", "RUN CONFIG", None))
        self.nItersLineEdit.setText(_translate("MainWindow", "1000", None))
        self.nItersLabel.setText(_translate("MainWindow", "Iterations", None))
        self.zeroOffsetLineEdit.setText(_translate("MainWindow", "0.", None))
        self.zeroOffsetLabel.setText(_translate("MainWindow", "Zero offset age", None))
        self.randSeedCheckBox.setText(_translate("MainWindow", "random seed", None))
        self.randSeedLineEdit.setText(_translate("MainWindow", "69.", None))
        self.forceIncrCheckBox.setText(_translate("MainWindow", "force increasing", None))
        self.slipRevCheckBox.setText(_translate("MainWindow", "slip reversals", None))
        self.linearFitRadio.setText(_translate("MainWindow", "Linear", None))
        self.piecewiseFitRadio.setText(_translate("MainWindow", "Piecewise Linear", None))
        self.cubicFitRadio.setText(_translate("MainWindow", "Cubic Spline", None))
        self.runButton.setText(_translate("MainWindow", "Run", None))
        self.cancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.importButton.setText(_translate("MainWindow", "Import", None))
        self.exportButton.setText(_translate("MainWindow", "Export", None))
        self.label_4.setText(_translate("MainWindow", "Fit Type", None))
        self.moveOffsetMarkerDownButton.setText(_translate("MainWindow", "v", None))
        self.moveOffsetMarkerUpButton.setText(_translate("MainWindow", "^", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))

