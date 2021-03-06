# -*- coding: utf-8 -*-
"""
销售功能模块
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot, QDate, QDateTime
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel  # 数据库模型视图

import pymysql
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.DataTableView import DataTableWidget
import pandas as pd
# from sqlalchemy import create_engine
import numpy as np
from decimal import Decimal
import time

from sale.Ui_quote_check import Ui_Quote_check
from sale.Ui_quote import Ui_Fquote
from sale.Ui_offer import Ui_offer_Form

from tools.mysql_conn import myMdb, connectDB
# from lib.RMB import * #人民币大写转换


class Order(QWidget, Ui_offer_Form): # 订单
    def __init__(self, parent=None):
        super(Order, self).__init__(parent)
        self.setupUi(self)
        self.offer()

    def offer(self): # 订单
        # self.offerwidget = DataTableWidget()
        widget = self.offerwidget
        widget.resize(600, 500) # 如果对部件尺寸大小不满意可以在这里设置

        self.model = DataFrameModel() # 设置新的模型
        widget.setViewModel(self.model)
        
        # conn = pymysql.connect(host='localhost', port=3308,user='root',password='root',db='mrp',charset='utf8')
        # # 通过sqlalchemy.create_engine建立连接引擎
        # engine = create_engine('mysql+pymysql://root:root@localhost:3308/mrp')
        # sql = 'select * from quote'
        # self.df = pd.read_sql(sql, con=conn)#MySQL法连接数据库,读取数据需要转换
        # self.df = pd.read_sql(sql, engine)#SQLAlchemy法可以直接创建dataframe
        # self.df.to_sql(name='user',con=engine,if_exists='append',index=False)  写入数据库
        # df.to_sql(目标表名,con=engine, schema=数据库名, index=False, index_label=False, if_exists='append', chunksize=1000)
        # pd.io.sql.to_sql(df,table_name,con=conn,schema='w_analysis',if_exists='append') 两个语句???

        self.df = pd.read_excel(r'C:/Users/Administrator/Desktop/报价模板.xlsx',encoding='utf-8')
        # self.df_original = self.df.copy() # 备份原始数据
        self.model.setDataFrame(self.df)

        # d = self.df.loc[:,'num'].sum()
        d = sum(self.df['单重'])
        print('d' +str(d))
        # self.df.apply(sum)
        # column_sum = self.df.iloc[:,j].sum()

        # dtypedict = {}
        # for i, j in zip(self.df.columns, self.df.dtypes):
        #     # if "object" in str(j):
        #     #     dtypedict.update({i: VARCHAR(256)})
        #     # if "float" in str(j):
        #     #     dtypedict.update({i: NUMBER(19,8)})
        #     if "int" in str(j):
        #         dtypedict.update({i: VARCHAR(19)})
        # return dtypedict
        # print(dtypedict)

        """
        # 查询数据并转为pandas.DataFrame，指定DataFrame的index为数据库中的id字段
        df = pd.read_sql('SELECT * FROM students', engine, index_col='id')
        print(df)
        # 修改DataFrame中的数据（移除age列）
        dft = df.drop(['age'], axis=1)
        # 将修改后的数据追加至原表,index=False代表不插入索引，因为数据库中id字段为自增字段
        dft.to_sql('students', engine, index=False, if_exists='append')
        """

    # 定义函数，自动输出DataFrme数据写入mysql的数类型字典表,配合to_sql方法使用(注意，其类型只能是SQLAlchemy type )
    # @pyqtSlot()
    # def on_pushButton_2_clicked(self):
    # def mapping_df_types(df):
    # """自动获取DataFrme各列的数据类型，生成字典。"""
        # dtypedict = {}
        # for i, j in zip(df.columns, df.dtypes):
        #     if "object" in str(j):
        #         dtypedict.update({i: VARCHAR(256)})
        #     if "float" in str(j):
        #         dtypedict.update({i: NUMBER(19,8)})
        #     if "int" in str(j):
        #         dtypedict.update({i: VARCHAR(19)})
        # return dtypedict
        # print(dtypedict)

        #data_base.to_sql('stock_class',engine,index=False,if_exists='append',dtype=dtypedict,chunksize=100)参考

        # @pyqtSlot()
        # def on_pushButton_clicked(self):
        #     """
        #     初始化pandas
        #     """
        #     self.model.setDataFrame(self.df_original)
        
        # @pyqtSlot()
        # def on_pushButton_2_clicked(self):
        #     """
        #     保存数据
        #     """
        #     # self.df.to_excel(r'./data/fund_data_new.xlsx')
        #     engine = create_engine('mysql+pymysql://root:root@localhost:3308/mrp')
        #     self.df.to_sql(name='test',con=engine,if_exists='append',index=False)#index=False自增型关键字用false默认为True，指定DataFrame的index是否一同写入数据库
        #     # con.dispose() # engine.dispose()


class Quote(QWidget, Ui_Fquote): # 报价
    """报价类"""
    def __init__(self, parent=None):
        super(Quote, self).__init__(parent)
        self.setupUi(self)
        #设置报价lneedit文本框显示当前日期
        self.quotedate.setText(time.strftime("%Y-%m-%d", time.localtime()))

        #公司名称下拉列表框
        result = myMdb().fetchall(field='公司名称', table='客户资料表')
        # vol = len(result[0])
        # 循环取元祖数据,转为列表
        col_lst = [tup[0] for tup in result]
        self.CBcorporate.insertItem(0, "请选择公司名称")
        self.CBcorporate.addItems(col_lst)

        #设置表格设置初始11行
        self.TWquote.setRowCount(500)
        # 设置标题
        # self.TWquote.setHorizontalHeaderLabels(input_table_header)
        # 设置每格为空值
        for i in range(500):
            for j in range(15):
                new_item = QTableWidgetItem("")
                new_item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                self.TWquote.setItem(i, j, new_item)
        #表格格式设置
        self.TWquote.horizontalHeader().setStyleSheet('QHeaderView::section{background:skyblue}')
        self.TWquote.setContextMenuPolicy(Qt.CustomContextMenu)            # 允许右键产生菜单
        self.TWquote.customContextMenuRequested.connect(self.right_menu)    # 将右键绑定到槽
        # self.TWquote.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.TWquote.verticalHeader().setVisible(False)                    # 左垂直表头不显示
        # self.TWquote.setEditTriggers(QAbstractItemView.AnyKeyPressed)    # 设置表格任何时候都能修改
        self.TWquote.horizontalHeader().setStretchLastSection(True)        #最后一列对齐边框
        # self.TWquote.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # self.TWquote.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #占满屏幕,平均分配列宽
        self.TWquote.resizeColumnsToContents()                             # 自适应列宽度
        # self.TWquote.resizeRowsToContents()                              # 自适应行高
        # self.autoadd()                                                   # 自动编序号
        # self.TWquote.hideColumn(0)                                       # 隐藏第一列
        # self.TWquote.showColumn(0)                                       # 显示第一列
        #设置文本框无边框
        styleSheet = "background:transparent;border-width:0;border-style:outset"
        self.quotationNo.setStyleSheet(styleSheet)
        self.contact.setStyleSheet(styleSheet)
        self.lineEdit_5.setStyleSheet(styleSheet)
        self.lineEdit_6.setStyleSheet(styleSheet)
        self.lineEdit_8.setStyleSheet(styleSheet)
        self.lineEdit_9.setStyleSheet(styleSheet)
        self.quotedate.setStyleSheet(styleSheet)
        self.total_price.setStyleSheet(styleSheet)
        self.total_quantity.setStyleSheet(styleSheet)
        self.add_quote_No()

    #点击查询按钮事件
    @pyqtSlot()
    def on_PBquery_clicked(self):
        # 点击查询后计算单价总价
        self.calculate()

    # 单价/总价计算
    def calculate(self):
        rows = self.TWquote.rowCount()                                       # 保存时有空行的情况用总行数.
        # 判断有数据的行数h,空值就退出循环
        for h in range(rows+1):
            if not self.TWquote.item(h, 0):
                break #跳出循环
            elif self.TWquote.item(h, 0).text() == "":
                break
        for i in range(h):
            quantity = int(self.TWquote.item(i, 5).text())                     # 数量quantity
            if self.TWquote.item(i, 10).text() == "":
                weight = 0
            else:
                weight = Decimal(str(self.TWquote.item(i, 10).text()))        # 单重unit weight
            if self.TWquote.item(i, 11).text() == "":
                weight_price = 0
            else:
                weight_price = Decimal(str(self.TWquote.item(i, 11).text()))   # 公斤价weight price
            if self.TWquote.item(i, 12).text() == "":
                cost = 0
            else:
                cost = Decimal(str(self.TWquote.item(i, 12).text()))            # 加工费cost
            if self.TWquote.item(i, 13).text() == "":
                expenses = 0
            else:
                expenses = Decimal(str(self.TWquote.item(i, 13).text()))        # 其他费用expenses
            # 计算单价    单价=单重*公斤价+加工费+其他费用
            if self.TWquote.item(i, 11).text() == "":
                price = Decimal(str(self.TWquote.item(i, 8).text()))
            else:
                price = weight*weight_price+cost+expenses
            self.TWquote.setItem(i, 8, QTableWidgetItem(str('%.2f' % price)))    #设置单价小数点2位
            amount = Decimal(quantity*price)                                     #总价amount=数量*单价
            self.TWquote.setItem(i, 9, QTableWidgetItem(str('%.2f' % amount))) 
            count_1 = self.sum_amount(5)
            self.total_quantity.setText(str(count_1.quantize(Decimal('0'))))   # 添加计算结果到总数量栏,0位小数
            count_2 = self.sum_amount(9)
            self.total_price.setText(str(count_2.quantize(Decimal('0.00'))))    # 添加计算结果到总价栏,2位小数

    # 计算列值总数函数
    def sum_amount(self, l):
        """计算所选列的总数,l为列数"""
        count = 0
        # 获取表格中的总行数,考虑到保存时有空行的情况用总行数.
        rows = self.TWquote.rowCount()
        for i in range(rows):
            # 判断不存在和空值,并设为0值
            if not self.TWquote.item(i,l):
                count += 0
            elif self.TWquote.item(i,l).text()=="":
                count += 0
            else:
                count += Decimal(self.TWquote.item(i,l).text())
        return count

    # 单元格变更事件
    @pyqtSlot(int, int, int, int)
    def on_TWquote_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        """指定列值变更重新计算数量和总价"""
        # if previousColumn == 5:                                                #改动后的列索引=数量列
        #     count_1 = self.sum_amount(5)                                       #计算第5列数量
        #     self.total_quantity.setText(str(count_1.quantize(Decimal('0'))))   # 添加计算结果到总数量栏,0位小数
        #     # self.money.setText(str(cncurrency(int(count_2))))                # 添加人民币大写

    # 自动增加序号
    def autoadd(self):
        """序号自动编号"""
        rows = self.TWquote.rowCount()                                    # 获取表格中的总行数
        for i in range(rows):
            xh = '%d'% (i+1)
            self.TWquote.setItem(i, 0, QTableWidgetItem(xh))

    # 右键菜单
    def right_menu(self, pos):
        """右键菜单def contextMenuEvent(self, event):"""
        pmenu = QMenu(self)
        pInsertAct = QAction(u"插入行", self.TWquote)
        pInsertsAct = QAction(u"插入多行", self.TWquote)
        pDeleteAct = QAction(u"删除行", self.TWquote)
        pHideAct = QAction(u"隐藏列", self.TWquote)
        pMergeAct = QAction(u"合并单元格", self.TWquote)
        pmenu.addAction(pInsertAct)
        pmenu.addAction(pInsertsAct)
        pmenu.addAction(pDeleteAct)
        pmenu.addAction(pHideAct)
        pmenu.addAction(pMergeAct)
        pmenu.popup(QtGui.QCursor.pos())  #在鼠标光标位置显示pmenu.popup(self.mapToGlobal(event.pos()))
        pInsertAct.triggered.connect(self.add_onerow)
        pInsertsAct.triggered.connect(self.add_rows)
        pDeleteAct.triggered.connect(self.ondelselect)
        pHideAct.triggered.connect(self.onhide)
        pMergeAct.triggered.connect(self.onmergecolumn)

    # 当前位置插入一行
    def add_onerow(self):
        r = self.TWquote.currentIndex().row()
        # print('r=' +str(r))
        self.TWquote.insertRow(r) #在r位置插入一空行
        for j in range(15):# 给插入的行设置空值
            newItem = QTableWidgetItem(0)
            newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.TWquote.setItem(r, j, newItem)

    # 插入多行=======??????
    def add_rows(self):
        """清除数据"""
        rows = self.TWquote.rowCount()# 获取表格中的总行数
        for i in self.TWquote.selectionModel().selection().indexes():
            rownum = i.row()
        #在末尾插入空行
        self.TWquote.setRowCount(rows + rownum)

    # 清除所选的数据,待改进====================================???????
    def del_select(self):
        """清除数据"""
        ret = QMessageBox.warning(self.TWquote, u'警告', u'是否删除所选行?', QMessageBox.Yes|QMessageBox.No)
        if ret == QMessageBox.Yes:
            for rg in self.TWquote.selectedRanges():
                new_item = QTableWidgetItem("")
                for i in range(rg.topRow(), rg.bottomRow()+1):
                    print('top' +str(rg.topRow()))
                    print(rg.bottomRow())
                    self.TWquote.setItem(i, 3, new_item)

    # 删除所选行
    def ondelselect(self):
        """删除所选行及数据"""
        ret = QMessageBox.warning(self.TWquote, u'警告', u'是否删除所选行?', QMessageBox.Yes|QMessageBox.No)
        if ret == QMessageBox.Yes:
            select_rows = set()
            for rg in self.TWquote.selectedRanges():
                for i in range(rg.topRow(), rg.bottomRow()+1):
                    select_rows.add(i)
            select_rows = list(select_rows)
            # print('r' +str(select_rows))
            select_rows.sort(reverse=True)  # 分类反转
            for index in select_rows:
                self.TWquote.removeRow(index)
        else:
            return

    # 隐藏列 还要增加还原隐藏的功能==================================????
    def onhide(self):
        """隐藏列"""
        c = self.TWquote.currentIndex().column()
        print('隐藏' +str(c) +'列')
        self.TWquote.hideColumn(c) #隐藏c列

    # 合并单元格
    def onmergecolumn(self):
        """合并单元格"""
        print('合并' +'单元格')

    # 生成报价单号
    def add_quote_No(self):
        """自动生成报价单号"""
        # 格式化当前日期+后两位
        date = time.strftime("%y%m%d", time.localtime()) + "00"
        bj = myMdb().fetchone(field='max(报价单号)', table='quote', where="报价单号>"+date)
        if bj[0] is None:
            bjdh = int(date) + 1
        else:
            bjdh = bj[0] + 1
        self.quotationNo.setText(str(bjdh))

    # 保存报价
    @pyqtSlot()
    def on_PBsave_clicked(self):
        """保存报价明细和汇总"""
        if self.CBcorporate.currentText() == "请选择公司名称":
            QMessageBox.warning(self, '警告', '公司名称未选择')
            return
        # 保存报价明细
        rows = self.TWquote.rowCount()  # 总行数
        cols = self.TWquote.columnCount()  # 总列数
        for h in range(rows+1):
            if not self.TWquote.item(h, 0):  # 从0行开始找出空值所在行
                break # 跳出循环
            elif self.TWquote.item(h, 0).text() == "":  #从0行开始找出空值所在行
                break
        preSql = "insert into quote ("  # 前一段拼接字段
        subSql = "values("              # 后一段拼接字段
        # exc = ()   # 作为execute的参数值，这是一个tuble类型
        preSql += "公司名称" + ","
        subSql += "%s,"
        preSql += "报价单号" + ","
        subSql += "%s,"
        for i in range(cols):  # 取出每一个子json的key和value值
            x = self.TWquote.horizontalHeaderItem(i).text()  # 列表头值
            preSql += x + ","  # 拼接前面sql的key值
            subSql += "%s,"   # 拼接后面sql的value数量
        preSql = preSql[0:preSql.__len__()-1] + ")"  # 去掉后面的“，”再添加“）”
        subSql = subSql[0:subSql.__len__()-1] + ")"  # 去掉后面的“，”再添加“）”
        sql = preSql+subSql  # 前后相加成一个完整的sql
        param = []  # 建传入值的列表
        for k in range(h):
            value_list = []
            value_list.append(self.CBcorporate.currentText())  # 公司名称加入数组
            value_list.append(self.quotationNo.text())
            for i in range(cols):
                if i in (10, 11, 12, 13) and self.TWquote.item(k, i).text() == "":
                    value_list.append("0")  # 把空值的数字格设为0值
                else:
                    value_list.append(self.TWquote.item(k, i).text())
            param.append(value_list)
        rowcount = myMdb().insert_many(sql, param)  # 执行SQL,返回插入的条数
        # 保存报价汇总==============================================================
        myMdb().insert(
            table='报价基本信息',
            公司名称=self.CBcorporate.currentText(),
            报价单号=self.quotationNo.text(),
            总数量=self.total_quantity.text(),
            总价=self.total_price.text(),
            业务员=self.contact.text(),
            报价日期=self.quotedate.text(),
            状态='待审核')
        QMessageBox.about(self, "保存成功", "保存了"+str(rowcount)+"条报价记录")

    # 导入excel文件
    @pyqtSlot()
    def on_PBnew_clicked(self):
        """打开Excel文件,导入到报价明细表中"""
        self.TWquote.clear
        #需要增加先清除原来数据代码
        openfile_name = QFileDialog.getOpenFileName(
            self, '选择文件', 'C:/Users/Administrator/Desktop/', 'Excel files(*.xlsx , *.xls)')
        global path_openfile_name                      # 把打开的文件名当全局变量,传导给读取表格用
        path_openfile_name = openfile_name[0]
        ###===========读取表格，转换表格，===========================================
        if len(path_openfile_name) > 0:
            df = pd.read_excel(path_openfile_name)
            input_table = df
            # input_table = df.fillna(0)                  # pandas将NaN替换为0
            # input_table = df.where(df.notnull(), None)# 将NaN替换为None
            input_table_rows = input_table.shape[0]     # numpy函数中shape函数读取矩阵第一维度的长度
            input_table_colunms = input_table.shape[1]
            # input_table_header = input_table.columns.values.tolist() # 读取标题
        ###======================给tablewidget设置行列表头============================
            # self.TWquote.setColumnCount(input_table_colunms)
            self.TWquote.setRowCount(input_table_rows)            #设置和导入数据相同行数
            # self.TWquote.setHorizontalHeaderLabels(input_table_header) # 设置标题
        ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]   # iloc：通过行和列的下标来访问数据
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
        ###==============将遍历的元素添加到tablewidget中并显示=======================
                    input_table_items = str(input_table_items_list)
                    if input_table_items == 'nan':
                        input_table_items = 0
                    newItem = QTableWidgetItem(input_table_items)
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    # print('newitem=' +input_table_items)
                    self.TWquote.setItem(i, j, newItem)  
        else:
            self.centralWidget.show()   #  ==============?????????????
        self.TWquote.resizeColumnsToContents()#根据内容自动调整所有列的列宽


class QuoteExamine(QWidget, Ui_Quote_check):  # 报价审核
    """报价审核类"""
    def __init__(self, parent=None):
        super(QuoteExamine, self).__init__(parent)
        self.setupUi(self)
        self.quotelist()

        #连接槽
        self.Quote_list.itemClicked.connect(self.querydetail)  # 点击报价目录,显示选择的报价明细
        self.Button_query.clicked.connect(self.querylist)    # 点击查询查报价清单

    def quotelist(self):  # 默认显示报价清单
        data = myMdb().fetchall(table='报价基本信息', where="状态!='已审核'")
        # col_lst = [tup[0] for tup in cur.description]  # 数据列字段名 tup:数组 #description:种类
        row = len(data)     # 获得data的行数
        vol = len(data[0])  # 获得data的列数.cur.description或len(data[0]) 
        # 插入表格
        # self.Quote_list = QTableWidget(row, vol)             # 设置row行vol列的表格
        self.Quote_list.setRowCount(row)
        font = QtGui.QFont('微软雅黑', 9)
        self.Quote_list.horizontalHeader().setFont(font)      # 设置行表头字体
        # self.Quote_list.setHorizontalHeaderLabels(col_lst)    # 设置标题
        self.Quote_list.verticalHeader().setVisible(False)    # 左垂直表头不显示
        # 加单元格下拉列表框
        comBox = QComboBox()
        comBox.addItems(['审核通过', '退回重报'])
        # comBox.setStyleSheet('QComboBox{margin:3px}')
        self.Quote_list.setCellWidget(0, 6, comBox)

        # 设置表格颜色             
        self.Quote_list.horizontalHeader().setStyleSheet('QHeaderView::section{background:skyblue}')
        # self.Quote_list.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右键产生菜单
        # self.Quote_list.customContextMenuRequested.connect(self.generateMenu)  # 将右键绑定到槽
        self.Quote_list.setEditTriggers(QAbstractItemView.NoEditTriggers)   # 设置表格禁止编辑
        self.Quote_list.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)                  # 设置分割条
        self.Quote_list.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        # 构建表格插入数据
        for i in range(row):                                      # i到row-1的数量
            for j in range(vol):
                temp_data = data[i][j]                            # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))          # 转换后可插入表格
                self.Quote_list.setItem(i, j, data1)
        # self.Quote_list.resizeColumnsToContents()             # 自适应宽度
        self.Quote_list.resizeRowsToContents()                  # 自适应行高,放最后可以等数据写入后自动适应表格数据宽度
        self.Quote_list.horizontalHeader().setStretchLastSection(True)  # 最后一列对齐边框
        splitter.addWidget(self.Quote_list)
        self.verticalLayout.addWidget(splitter)
        self.QuoteDetail()

    def QuoteDetail(self):
        """审核报价明细区域"""
        db = connectDB()

        self.tablemodel = QSqlTableModel()
        self.Quote_detail.setModel(self.tablemodel)
        self.tablemodel.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.tablemodel.setTable("quote")
        self.tablemodel.select()
        self.tablemodel.setHeaderData(0, Qt.Horizontal, "公司名称")
        self.tablemodel.setHeaderData(1, Qt.Horizontal, "报价单号")
        self.tablemodel.setHeaderData(2, Qt.Horizontal, "序号")
        self.tablemodel.setHeaderData(3, Qt.Horizontal, "作者")
        self.tablemodel.setHeaderData(4, Qt.Horizontal, "出版单位")
        self.tablemodel.setHeaderData(5, Qt.Horizontal, "图书分类")
        self.tablemodel.setHeaderData(6, Qt.Horizontal, "定价")

        # data_3 = myMdb().fetchall(table='报价基本信息')
        # # col_lst_3 = [tup[0] for tup in cur_3.description]
        # vol_3 = len(data_3[0])                                     # 获得data的列数.cur.description  len(data[0]) 
        # # self.Quote_detail = QTableWidget(0, vol_3)                 # 初始界面显示标题不用显示明细数据,所以QTableWidget(0,vol_3)
        # self.Quote_detail.setRowCount(500)
        # font = QtGui.QFont('微软雅黑', 9)
        # self.Quote_detail.horizontalHeader().setFont(font)         # 设置行表头字体
        # # self.Quote_detail.setHorizontalHeaderLabels(col_lst_3)     # 设置标题
        # self.Quote_detail.verticalHeader().setVisible(False)       # 左垂直表头不显示
        # self.Quote_detail.setObjectName("报价明细")
        # self.Quote_detail.horizontalHeader().setStyleSheet(
        #     'QHeaderView::section{background:skyblue}')
        # self.Quote_detail.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        # self.Quote_detail.resizeColumnsToContents()                # 自适应宽度
        # self.Quote_list.resizeRowsToContents()
        # # self.Quote_detail.horizontalHeader().setStretchLastSection(True)  # 最后一列对齐边框
        # self.Quote_detail.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        # splitter.addWidget(self.Quote_detail)
        # self.verticalLayout.addWidget(splitter)
        # # self.setLayout(self.verticalLayout)                      # 加这行后查询后可以更新,不用再addwidget,待搞明白?

    def querylist(self):  # 查询报价清单
        self.Quote_list.clearContents                    # clearContents清除内容,clear清空表格中所有内容（包含表头）
        lsearch = self.Line_search.text()                    # 搜索框
        # sql = "SELECT * FROM 报价基本信息 WHERE 公司名称 LIKE '%"+lsearch+"%'"   #'%"+bjdh+"%'"
        if lsearch == "":
            data_2 = myMdb().fetchall(table='报价基本信息', where="状态!='已审核'")
        else:
            data_2 = myMdb().fetchall(
                table='报价基本信息',
                where="公司名称="+"'"+lsearch+"'" + "and 状态!='已审核'")
        # col_lst_2 = [tup[0] for tup in curr.description]
        # print(data_2)
        row_2 = len(data_2)                                 #获得data的行数
        vol_2 = len(data_2[0])                      #获得data的列数.cur.description  len(data[0]) 
        self.Quote_list.setRowCount(row_2)                  #取查询到数据的行数,设表格行数
        for i in range(row_2):                              #i到row-2的数量
            for j in range(vol_2):
                temp_data = data_2[i][j]                    # 临时记录，不能直接插入表格
                data2 = QTableWidgetItem(str(temp_data))    # 转换后可插入表格
                self.Quote_list.setItem(i, j, data2)

    def querydetail(self):  # 查询报价明细
        h = self.Quote_list.currentIndex().row()       # 找到所选行的行数h
        bjdh = self.Quote_list.item(h, 1).text()       # 找到所选h行的第2列报价单号
        # sql = "SELECT * FROM 报价明细 WHERE 报价单号 LIKE '%"+bjdh+"%'"   #'%"+bjdh+"%'"
        self.Quote_detail.clearContents()  # 清除报价明细表内数据
        data_3 = myMdb().fetchall(table='quote', where="报价单号=" +bjdh)
        # col_lst_3 = [tup[0] for tup in cur_3.description]
        # print(data_3)
        row_3 = len(data_3)                                          #获得data的行数
        vol_3 = len(data_3[0])                         #获得data的列数.cur.description len(data[0])
        self.Quote_detail.setRowCount(row_3)
        # self.Quote_detail.setColumnCount(0)
        #构建表格插入数据
        for i in range(row_3):                                     #i到row-1的数量
            for j in range(vol_3):
                temp_data = data_3[i][j]                           # 临时记录，不能直接插入表格
                data3 = QTableWidgetItem(str(temp_data))           # 转换后可插入表格
                self.Quote_detail.setItem(i, j, data3)
        # 适应列宽/行高/最后一列对齐边框
        self.Quote_detail.resizeColumnsToContents()
        self.Quote_detail.resizeRowsToContents()
        self.Quote_detail.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()  # 报价审核通过
    def on_Button_pass_clicked(self):
        h = self.Quote_list.currentIndex().row()          # 找到所选行的行数h
        bjdh = self.Quote_list.item(h, 1).text()          # 找到所选h行的1位报价单号
        # cur_4.execute("UPDATE 报价基本信息 SET 状态='通过' WHERE 报价单号 = '"+bjdh+"'")
        myMdb().update(table='报价基本信息', 状态='已审核', where="报价单号="+bjdh)
        QMessageBox.information(QWidget(), "标题", "审核成功")
        self.Quote_list.clearContents()
        self.Quote_detail.clearContents()
        self.querylist()
