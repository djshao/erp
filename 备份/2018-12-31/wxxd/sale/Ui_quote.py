# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\erp\wxxd\sale\quote.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fquote(object):
    def setupUi(self, Fquote):
        Fquote.setObjectName("Fquote")
        Fquote.resize(1024, 768)
        Fquote.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_2 = QtWidgets.QGridLayout(Fquote)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 2, 7, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(678, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.PBnew = QtWidgets.QPushButton(Fquote)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBnew.setIcon(icon)
        self.PBnew.setObjectName("PBnew")
        self.horizontalLayout.addWidget(self.PBnew)
        self.PBquery = QtWidgets.QPushButton(Fquote)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/png/images/file_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBquery.setIcon(icon1)
        self.PBquery.setObjectName("PBquery")
        self.horizontalLayout.addWidget(self.PBquery)
        self.PBexport = QtWidgets.QPushButton(Fquote)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/png/images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBexport.setIcon(icon2)
        self.PBexport.setObjectName("PBexport")
        self.horizontalLayout.addWidget(self.PBexport)
        self.PBsave = QtWidgets.QPushButton(Fquote)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/png/images/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBsave.setIcon(icon3)
        self.PBsave.setObjectName("PBsave")
        self.horizontalLayout.addWidget(self.PBsave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.CBcorporate = QtWidgets.QComboBox(Fquote)
        self.CBcorporate.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.CBcorporate.setFont(font)
        self.CBcorporate.setEditable(True)
        self.CBcorporate.setCurrentText("")
        self.CBcorporate.setObjectName("CBcorporate")
        self.horizontalLayout_2.addWidget(self.CBcorporate)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_12 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.quotationNo = QtWidgets.QLineEdit(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.quotationNo.setFont(font)
        self.quotationNo.setStatusTip("")
        self.quotationNo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.quotationNo.setObjectName("quotationNo")
        self.horizontalLayout_2.addWidget(self.quotationNo)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.TWquote = QtWidgets.QTableWidget(Fquote)
        self.TWquote.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.TWquote.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.TWquote.setShowGrid(True)
        self.TWquote.setObjectName("TWquote")
        self.TWquote.setColumnCount(15)
        self.TWquote.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.TWquote.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWquote.setHorizontalHeaderItem(14, item)
        self.gridLayout_2.addWidget(self.TWquote, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(Fquote)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 5, 1, 1)
        self.total_quantity = QtWidgets.QLineEdit(Fquote)
        self.total_quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.total_quantity.setObjectName("total_quantity")
        self.gridLayout.addWidget(self.total_quantity, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 6, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Fquote)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 5, 1, 1)
        self.total_price = QtWidgets.QLineEdit(Fquote)
        self.total_price.setAlignment(QtCore.Qt.AlignCenter)
        self.total_price.setObjectName("total_price")
        self.gridLayout.addWidget(self.total_price, 0, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 4)
        self.contact = QtWidgets.QLineEdit(Fquote)
        self.contact.setAlignment(QtCore.Qt.AlignCenter)
        self.contact.setObjectName("contact")
        self.gridLayout.addWidget(self.contact, 1, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(Fquote)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Fquote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 7, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(Fquote)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 2, 8, 1, 1)
        self.quotedate = QtWidgets.QLineEdit(Fquote)
        self.quotedate.setAlignment(QtCore.Qt.AlignCenter)
        self.quotedate.setObjectName("quotedate")
        self.gridLayout.addWidget(self.quotedate, 1, 8, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(6, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.label_7.setBuddy(self.lineEdit_6)
        self.label_3.setBuddy(self.total_quantity)
        self.label_9.setBuddy(self.lineEdit_8)
        self.label_5.setBuddy(self.contact)
        self.label_6.setBuddy(self.lineEdit_5)
        self.label_10.setBuddy(self.lineEdit_9)
        self.label_4.setBuddy(self.total_price)

        self.retranslateUi(Fquote)
        QtCore.QMetaObject.connectSlotsByName(Fquote)

    def retranslateUi(self, Fquote):
        _translate = QtCore.QCoreApplication.translate
        Fquote.setWindowTitle(_translate("Fquote", "报价单"))
        self.PBnew.setText(_translate("Fquote", "新建"))
        self.PBquery.setText(_translate("Fquote", "查询"))
        self.PBexport.setText(_translate("Fquote", "导出"))
        self.PBsave.setText(_translate("Fquote", "保存"))
        self.label.setText(_translate("Fquote", "无锡市星达石化配件有限公司报价单"))
        self.label_11.setText(_translate("Fquote", "公司名称:"))
        self.label_12.setText(_translate("Fquote", "报价单号:"))
        self.quotationNo.setToolTip(_translate("Fquote", "报价单号"))
        self.quotationNo.setInputMask(_translate("Fquote", "99999999"))
        self.quotationNo.setPlaceholderText(_translate("Fquote", "输入报价单号"))
        item = self.TWquote.horizontalHeaderItem(0)
        item.setText(_translate("Fquote", "序号"))
        item = self.TWquote.horizontalHeaderItem(1)
        item.setText(_translate("Fquote", "名称"))
        item = self.TWquote.horizontalHeaderItem(2)
        item.setText(_translate("Fquote", "制造标准"))
        item = self.TWquote.horizontalHeaderItem(3)
        item.setText(_translate("Fquote", "规格型号"))
        item = self.TWquote.horizontalHeaderItem(4)
        item.setText(_translate("Fquote", "材质"))
        item = self.TWquote.horizontalHeaderItem(5)
        item.setText(_translate("Fquote", "数量"))
        item = self.TWquote.horizontalHeaderItem(6)
        item.setText(_translate("Fquote", "工作令号"))
        item = self.TWquote.horizontalHeaderItem(7)
        item.setText(_translate("Fquote", "件号"))
        item = self.TWquote.horizontalHeaderItem(8)
        item.setText(_translate("Fquote", "单价"))
        item = self.TWquote.horizontalHeaderItem(9)
        item.setText(_translate("Fquote", "总价"))
        item = self.TWquote.horizontalHeaderItem(10)
        item.setText(_translate("Fquote", "单重"))
        item = self.TWquote.horizontalHeaderItem(11)
        item.setText(_translate("Fquote", "公斤价"))
        item = self.TWquote.horizontalHeaderItem(12)
        item.setText(_translate("Fquote", "加工费"))
        item = self.TWquote.horizontalHeaderItem(13)
        item.setText(_translate("Fquote", "其他费用"))
        item = self.TWquote.horizontalHeaderItem(14)
        item.setText(_translate("Fquote", "备注"))
        self.lineEdit_5.setInputMask(_translate("Fquote", "0000_00000000"))
        self.lineEdit_5.setText(_translate("Fquote", "0510_85591538"))
        self.label_7.setText(_translate("Fquote", "传真:"))
        self.label_3.setText(_translate("Fquote", "总数量:"))
        self.label_9.setText(_translate("Fquote", "交货期:"))
        self.label_5.setText(_translate("Fquote", "联系人:"))
        self.label_6.setText(_translate("Fquote", "电话:"))
        self.lineEdit_6.setInputMask(_translate("Fquote", "0000_00000000"))
        self.lineEdit_6.setText(_translate("Fquote", "0510_85591761"))
        self.label_10.setToolTip(_translate("Fquote", "报价有效期"))
        self.label_10.setText(_translate("Fquote", "报价有效期:"))
        self.label_8.setText(_translate("Fquote", "日期:"))
        self.contact.setText(_translate("Fquote", "马萍"))
        self.lineEdit_8.setText(_translate("Fquote", "30天"))
        self.label_4.setText(_translate("Fquote", "总价:"))
        self.lineEdit_9.setText(_translate("Fquote", "5天"))
        self.quotedate.setInputMask(_translate("Fquote", "0000-00-00"))

import erp_rc
