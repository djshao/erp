# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\erp\wxxd\sale\quote.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wgt_quote(object):
    def setupUi(self, wgt_quote):
        wgt_quote.setObjectName("wgt_quote")
        wgt_quote.resize(1024, 768)
        wgt_quote.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_2 = QtWidgets.QGridLayout(wgt_quote)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 2, 7, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(678, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cbo_state = QtWidgets.QComboBox(wgt_quote)
        self.cbo_state.setMinimumSize(QtCore.QSize(0, 26))
        self.cbo_state.setCurrentText("")
        self.cbo_state.setObjectName("cbo_state")
        self.horizontalLayout.addWidget(self.cbo_state)
        self.btn_check = QtWidgets.QPushButton(wgt_quote)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/myImage/images/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_check.setIcon(icon)
        self.btn_check.setObjectName("btn_check")
        self.horizontalLayout.addWidget(self.btn_check)
        self.PBnew = QtWidgets.QPushButton(wgt_quote)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/png/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBnew.setIcon(icon1)
        self.PBnew.setObjectName("PBnew")
        self.horizontalLayout.addWidget(self.PBnew)
        self.PBquery = QtWidgets.QPushButton(wgt_quote)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/png/images/file_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBquery.setIcon(icon2)
        self.PBquery.setObjectName("PBquery")
        self.horizontalLayout.addWidget(self.PBquery)
        self.PBexport = QtWidgets.QPushButton(wgt_quote)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/png/images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBexport.setIcon(icon3)
        self.PBexport.setObjectName("PBexport")
        self.horizontalLayout.addWidget(self.PBexport)
        self.PBsave = QtWidgets.QPushButton(wgt_quote)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/png/images/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PBsave.setIcon(icon4)
        self.PBsave.setObjectName("PBsave")
        self.horizontalLayout.addWidget(self.PBsave)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.CBcorporate = QtWidgets.QComboBox(wgt_quote)
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
        self.label_12 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.quotationNo = QtWidgets.QLineEdit(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.quotationNo.setFont(font)
        self.quotationNo.setStatusTip("")
        self.quotationNo.setFrame(True)
        self.quotationNo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.quotationNo.setClearButtonEnabled(True)
        self.quotationNo.setObjectName("quotationNo")
        self.horizontalLayout_2.addWidget(self.quotationNo)
        self.horizontalLayout_2.setStretch(2, 3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.tblwgt_quote = QtWidgets.QTableWidget(wgt_quote)
        self.tblwgt_quote.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblwgt_quote.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tblwgt_quote.setShowGrid(True)
        self.tblwgt_quote.setObjectName("tblwgt_quote")
        self.tblwgt_quote.setColumnCount(0)
        self.tblwgt_quote.setRowCount(0)
        self.gridLayout_2.addWidget(self.tblwgt_quote, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(wgt_quote)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 5, 1, 1)
        self.total_quantity = QtWidgets.QLineEdit(wgt_quote)
        self.total_quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.total_quantity.setObjectName("total_quantity")
        self.gridLayout.addWidget(self.total_quantity, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(wgt_quote)
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
        self.lineEdit_6 = QtWidgets.QLineEdit(wgt_quote)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 5, 1, 1)
        self.total_price = QtWidgets.QLineEdit(wgt_quote)
        self.total_price.setAlignment(QtCore.Qt.AlignCenter)
        self.total_price.setObjectName("total_price")
        self.gridLayout.addWidget(self.total_price, 0, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(wgt_quote)
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
        self.contact = QtWidgets.QLineEdit(wgt_quote)
        self.contact.setAlignment(QtCore.Qt.AlignCenter)
        self.contact.setObjectName("contact")
        self.gridLayout.addWidget(self.contact, 1, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(wgt_quote)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(wgt_quote)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 7, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(wgt_quote)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 2, 8, 1, 1)
        self.quotedate = QtWidgets.QLineEdit(wgt_quote)
        self.quotedate.setAlignment(QtCore.Qt.AlignCenter)
        self.quotedate.setObjectName("quotedate")
        self.gridLayout.addWidget(self.quotedate, 1, 8, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(6, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.label_7.setBuddy(self.lineEdit_6)
        self.label_3.setBuddy(self.total_quantity)
        self.label_9.setBuddy(self.lineEdit_8)
        self.label_5.setBuddy(self.contact)
        self.label_6.setBuddy(self.lineEdit_5)
        self.label_10.setBuddy(self.lineEdit_9)
        self.label_4.setBuddy(self.total_price)

        self.retranslateUi(wgt_quote)
        QtCore.QMetaObject.connectSlotsByName(wgt_quote)

    def retranslateUi(self, wgt_quote):
        _translate = QtCore.QCoreApplication.translate
        wgt_quote.setWindowTitle(_translate("wgt_quote", "报价单"))
        self.cbo_state.setToolTip(_translate("wgt_quote", "审核情况"))
        self.btn_check.setToolTip(_translate("wgt_quote", "审核"))
        self.btn_check.setText(_translate("wgt_quote", "审核"))
        self.PBnew.setText(_translate("wgt_quote", "导入"))
        self.PBquery.setText(_translate("wgt_quote", "查询"))
        self.PBexport.setText(_translate("wgt_quote", "导出"))
        self.PBsave.setText(_translate("wgt_quote", "保存"))
        self.label.setText(_translate("wgt_quote", "无锡市星达石化配件有限公司报价单"))
        self.label_11.setText(_translate("wgt_quote", "公司名称:"))
        self.label_12.setText(_translate("wgt_quote", "报价单号:"))
        self.quotationNo.setToolTip(_translate("wgt_quote", "报价单号"))
        self.quotationNo.setPlaceholderText(_translate("wgt_quote", "输入报价单号"))
        self.lineEdit_5.setInputMask(_translate("wgt_quote", "0000_00000000"))
        self.lineEdit_5.setText(_translate("wgt_quote", "0510_85591538"))
        self.label_7.setText(_translate("wgt_quote", "传真:"))
        self.label_3.setText(_translate("wgt_quote", "总数量:"))
        self.label_9.setText(_translate("wgt_quote", "交货期:"))
        self.label_5.setText(_translate("wgt_quote", "联系人:"))
        self.label_6.setText(_translate("wgt_quote", "电话:"))
        self.lineEdit_6.setInputMask(_translate("wgt_quote", "0000_00000000"))
        self.lineEdit_6.setText(_translate("wgt_quote", "0510_85591761"))
        self.label_10.setToolTip(_translate("wgt_quote", "报价有效期"))
        self.label_10.setText(_translate("wgt_quote", "报价有效期:"))
        self.label_8.setText(_translate("wgt_quote", "日期:"))
        self.contact.setText(_translate("wgt_quote", "马萍"))
        self.lineEdit_8.setText(_translate("wgt_quote", "30天"))
        self.label_4.setText(_translate("wgt_quote", "总价:"))
        self.lineEdit_9.setText(_translate("wgt_quote", "5天"))
        self.quotedate.setInputMask(_translate("wgt_quote", "0000-00-00"))

import erp_rc
import myImage_rc
