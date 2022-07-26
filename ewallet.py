# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ewallet.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

conn = sqlite3.connect("ManageTransaction.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS TransactionTable (Id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT, Income INTEGER, Remarks_1 TEXT, Expense INTEGER, Remarks_2 TEXT)")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 540)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(-10, 0, 1321, 541))
        self.TabWidget.setAutoFillBackground(False)
        self.TabWidget.setObjectName("TabWidget")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setObjectName("HomeTab")
        self.HomeImageLabel = QtWidgets.QLabel(self.HomeTab)
        self.HomeImageLabel.setGeometry(QtCore.QRect(10, 0, 1031, 521))
        self.HomeImageLabel.setText("")
        self.HomeImageLabel.setPixmap(QtGui.QPixmap("HomeImage.jpg"))
        self.HomeImageLabel.setScaledContents(True)
        self.HomeImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HomeImageLabel.setObjectName("HomeImageLabel")
        self.TabWidget.addTab(self.HomeTab, "")
        self.ManageTab = QtWidgets.QWidget()
        self.ManageTab.setObjectName("ManageTab")
        self.line = QtWidgets.QFrame(self.ManageTab)
        self.line.setGeometry(QtCore.QRect(180, -10, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.ManageTab)
        self.line_2.setGeometry(QtCore.QRect(190, -10, 20, 521))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.ManageTab)
        self.line_4.setGeometry(QtCore.QRect(820, -10, 20, 521))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.ManageTab)
        self.line_3.setGeometry(QtCore.QRect(830, -10, 20, 521))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.DateLabel = QtWidgets.QLabel(self.ManageTab)
        self.DateLabel.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.DateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DateLabel.setObjectName("DateLabel")
        self.IncomeAmountLabel = QtWidgets.QLabel(self.ManageTab)
        self.IncomeAmountLabel.setGeometry(QtCore.QRect(20, 110, 151, 31))
        self.IncomeAmountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IncomeAmountLabel.setObjectName("IncomeAmountLabel")
        self.IncomeRemarksLabel = QtWidgets.QLabel(self.ManageTab)
        self.IncomeRemarksLabel.setGeometry(QtCore.QRect(20, 210, 151, 31))
        self.IncomeRemarksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IncomeRemarksLabel.setObjectName("IncomeRemarksLabel")
        self.ExpenseLabel = QtWidgets.QLabel(self.ManageTab)
        self.ExpenseLabel.setGeometry(QtCore.QRect(20, 310, 151, 31))
        self.ExpenseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ExpenseLabel.setObjectName("ExpenseLabel")
        self.ExpenseRemarksLabel = QtWidgets.QLabel(self.ManageTab)
        self.ExpenseRemarksLabel.setGeometry(QtCore.QRect(20, 410, 151, 31))
        self.ExpenseRemarksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ExpenseRemarksLabel.setObjectName("ExpenseRemarksLabel")
        self.DateText = QtWidgets.QLineEdit(self.ManageTab)
        self.DateText.setGeometry(QtCore.QRect(20, 50, 151, 31))
        self.DateText.setText("")
        self.DateText.setObjectName("DateText")
        self.IncomeAmountText = QtWidgets.QLineEdit(self.ManageTab)
        self.IncomeAmountText.setGeometry(QtCore.QRect(20, 150, 151, 31))
        self.IncomeAmountText.setObjectName("IncomeAmountText")
        self.IncomeRemarksText_2 = QtWidgets.QLineEdit(self.ManageTab)
        self.IncomeRemarksText_2.setGeometry(QtCore.QRect(20, 250, 151, 31))
        self.IncomeRemarksText_2.setObjectName("IncomeRemarksText_2")
        self.ExpenseRemarksText_2 = QtWidgets.QLineEdit(self.ManageTab)
        self.ExpenseRemarksText_2.setGeometry(QtCore.QRect(20, 350, 151, 31))
        self.ExpenseRemarksText_2.setObjectName("ExpenseRemarksText_2")
        self.ExpenseRemarkseText = QtWidgets.QLineEdit(self.ManageTab)
        self.ExpenseRemarkseText.setGeometry(QtCore.QRect(20, 450, 151, 31))
        self.ExpenseRemarkseText.setObjectName("ExpenseRemarkseText")
        self.tableWidget = QtWidgets.QTableWidget(self.ManageTab)
        self.tableWidget.setGeometry(QtCore.QRect(200, 160, 631, 341))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.EwalletHeaderText = QtWidgets.QLabel(self.ManageTab)
        self.EwalletHeaderText.setGeometry(QtCore.QRect(200, 0, 631, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EwalletHeaderText.setFont(font)
        self.EwalletHeaderText.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.EwalletHeaderText.setAlignment(QtCore.Qt.AlignCenter)
        self.EwalletHeaderText.setObjectName("EwalletHeaderText")
        self.AddButton = QtWidgets.QPushButton(self.ManageTab)
        self.AddButton.setGeometry(QtCore.QRect(420, 110, 75, 23))
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(self.ManageTab)
        self.DeleteButton.setGeometry(QtCore.QRect(540, 110, 75, 23))
        self.DeleteButton.setObjectName("DeleteButton")
        self.line_5 = QtWidgets.QFrame(self.ManageTab)
        self.line_5.setGeometry(QtCore.QRect(200, 80, 631, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.AnalyticsButton = QtWidgets.QPushButton(self.ManageTab)
        self.AnalyticsButton.setGeometry(QtCore.QRect(650, 110, 75, 23))
        self.AnalyticsButton.setObjectName("AnalyticsButton")
        self.TotalExpenditureText = QtWidgets.QLineEdit(self.ManageTab)
        self.TotalExpenditureText.setGeometry(QtCore.QRect(870, 200, 151, 31))
        self.TotalExpenditureText.setReadOnly(True)
        self.TotalExpenditureText.setObjectName("TotalExpenditureText")
        self.TotalIncomeLabel = QtWidgets.QLabel(self.ManageTab)
        self.TotalIncomeLabel.setGeometry(QtCore.QRect(870, 20, 151, 31))
        self.TotalIncomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalIncomeLabel.setObjectName("TotalIncomeLabel")
        self.FinalBalanceText = QtWidgets.QLineEdit(self.ManageTab)
        self.FinalBalanceText.setGeometry(QtCore.QRect(870, 390, 151, 31))
        self.FinalBalanceText.setReadOnly(True)
        self.FinalBalanceText.setObjectName("FinalBalanceText")
        self.TotalIncomeText = QtWidgets.QLineEdit(self.ManageTab)
        self.TotalIncomeText.setGeometry(QtCore.QRect(870, 60, 151, 31))
        self.TotalIncomeText.setText("")
        self.TotalIncomeText.setReadOnly(True)
        self.TotalIncomeText.setObjectName("TotalIncomeText")
        self.TotalExpenditureLabel = QtWidgets.QLabel(self.ManageTab)
        self.TotalExpenditureLabel.setGeometry(QtCore.QRect(870, 160, 151, 31))
        self.TotalExpenditureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalExpenditureLabel.setObjectName("TotalExpenditureLabel")
        self.FinalBalanceLabel = QtWidgets.QLabel(self.ManageTab)
        self.FinalBalanceLabel.setGeometry(QtCore.QRect(870, 350, 151, 31))
        self.FinalBalanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FinalBalanceLabel.setObjectName("FinalBalanceLabel")
        self.line_6 = QtWidgets.QFrame(self.ManageTab)
        self.line_6.setGeometry(QtCore.QRect(840, 250, 201, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.ManageTab)
        self.line_7.setGeometry(QtCore.QRect(840, 0, 201, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.ManageTab)
        self.line_8.setGeometry(QtCore.QRect(840, 470, 201, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.LoadDataButton = QtWidgets.QPushButton(self.ManageTab)
        self.LoadDataButton.setGeometry(QtCore.QRect(300, 110, 75, 23))
        self.LoadDataButton.setObjectName("LoadDataButton")
        self.TabWidget.addTab(self.ManageTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.HomeTab), _translate("MainWindow", "HOME"))
        self.DateLabel.setText(_translate("MainWindow", "Date"))
        self.IncomeAmountLabel.setText(_translate("MainWindow", "Income Amount"))
        self.IncomeRemarksLabel.setText(_translate("MainWindow", "Income Remarks"))
        self.ExpenseLabel.setText(_translate("MainWindow", "Expense Amount"))
        self.ExpenseRemarksLabel.setText(_translate("MainWindow", "Expense Remarks"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "INCOME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INCOME REMARKS"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "EXPENSE"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EXPENSE REMARKS"))
        self.EwalletHeaderText.setText(_translate("MainWindow", "ELECTRONIC WALLET"))
        self.AddButton.setText(_translate("MainWindow", "ADD"))
        self.DeleteButton.setText(_translate("MainWindow", "DELETE"))
        self.AnalyticsButton.setText(_translate("MainWindow", "ANALYTICS"))
        self.TotalIncomeLabel.setText(_translate("MainWindow", "TOTAL INCOME"))
        self.TotalExpenditureLabel.setText(_translate("MainWindow", "TOTAL EXPENDITURE"))
        self.FinalBalanceLabel.setText(_translate("MainWindow", "FINAL BALANCE"))
        self.LoadDataButton.setText(_translate("MainWindow", "LOAD"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.ManageTab), _translate("MainWindow", "MANAGE"))

        self.DeleteButton.clicked.connect(self.DeleteButtonClicked)
        self.LoadDataButton.clicked.connect(self.LoadDataButtonClicked)
        self.AddButton.clicked.connect(self.getter)
    
    def getter(self):
        a = self.DateText.text()
        b = self.IncomeAmountText.text()
        co = self.IncomeRemarksText_2.text()
        d = self.ExpenseRemarksText_2.text()
        e = self.ExpenseRemarkseText.text()
        
        self.c.execute("INSERT INTO TransactionTable (Id, Date, Income, Remarks_1, Expense, Remarks_2) VALUES(?,?,?,?,?,?)", (a,b,co,d,e))
        
        if conn:
            conn.commit()
            c.close()
            conn.close()
    
    def LoadDataButtonClicked(self):
        conn = sqlite3.connect("ManageTransaction.db")
        c = conn.cursor()
        table = c.execute("SELECT * FROM TransactionTable")
        
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(table):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        if conn:
            conn.commit()
            c.close()
            conn.close()
	
    def DeleteButtonClicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("E-WALLET")
        msg.setText("DO YOU REALLY WANT TO DELETE?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.MessageBoxButton)
        x = msg.exec_()       
    
    def MessageBoxButton(self, i):
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
