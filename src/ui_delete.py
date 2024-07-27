# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_uiBzjUIW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from login import *


class Ui_Delete(QMainWindow):
    taskCreated = Signal()

    def __init__(self, task_list, name):
        super().__init__()
        self.name = name
        self.task_list = task_list
        self.selected_tasks = []
        self.setupUi(self)

    def setupUi(self, Delete_Window):
        # 检查Delete对象是否有对象名，如果没有，则设置对象名为"Delete"
        if not Delete_Window.objectName():
            Delete_Window.setObjectName(u"Delete")
        # 设置窗口大小
        Delete_Window.resize(533, 322)
        # 创建中央小部件并设置其对象名
        self.centralwidget = QWidget(Delete_Window)
        self.centralwidget.setObjectName(u"centralwidget")

        # 创建任务表格，并确保其至少有5列
        self.task_table = QTableWidget(self.centralwidget)
        if self.task_table.columnCount() < 5:
            self.task_table.setColumnCount(5)

        # 支持多选
        self.task_table.setSelectionBehavior(QTableWidget.SelectRows)

        self.task_table.setRowCount(len(self.task_list))
        # 为表格设置水平表头项
        __qtablewidgetitem = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        # 设置表格的几何形状和网格样式
        self.task_table.setObjectName(u"task_table_widget")
        self.task_table.setGeometry(QRect(15, 11, 511, 261))
        self.task_table.setGridStyle(Qt.PenStyle.SolidLine)
        # 禁用表格的自动排序功能
        self.task_table.setSortingEnabled(False)

        # 逐行显示
        self.task_table.clear()
        for row_idx, task in enumerate(self.task_list):
            self.task_table.setItem(row_idx, 0, QTableWidgetItem(task.title))
            self.task_table.setItem(row_idx, 1, QTableWidgetItem(str(task.priority)))
            self.task_table.setItem(row_idx, 2, QTableWidgetItem(str(task.deadline)))
            self.task_table.setItem(row_idx, 3, QTableWidgetItem(task.description))
            self.task_table.setItem(row_idx, 4, QTableWidgetItem(str(task.state)))
        self.task_table.resizeColumnsToContents()  # 调整列宽以适应内容
        min_width = 50
        for i in range(self.task_table.columnCount()):  # 设置最小列宽
            self.task_table.setColumnWidth(i, max(min_width, self.task_table.columnWidth(i)))

        # 创建水平布局的小部件，并设置其对象名
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        # 设置布局小部件的位置和大小
        self.horizontalLayoutWidget.setGeometry(QRect(350, 280, 171, 41))
        # 创建水平布局，并设置其对象名和内容边距
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # 创建确定按钮，设置其对象名，并连接点击事件到delete_selected_tasks函数
        self.Ok_Button = QPushButton(self.horizontalLayoutWidget)
        self.Ok_Button.setObjectName(u"Ok_Button")
        self.Ok_Button.clicked.connect(self.delete_selected_tasks)
        # 将确定按钮添加到水平布局中
        self.horizontalLayout.addWidget(self.Ok_Button)

        # 创建取消按钮，设置其对象名，并连接点击事件到cancel_delete_tasks函数
        self.Cancel_Button = QPushButton(self.horizontalLayoutWidget)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.clicked.connect(self.cancel_delete_tasks)
        # 将取消按钮添加到水平布局中
        self.horizontalLayout.addWidget(self.Cancel_Button)

        # 创建标签，提示用法
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 280, 341, 41))
        self.label.setFrameShape(QFrame.Shape.WinPanel)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        # 设置中央小部件为Delete窗口的中央部件
        Delete_Window.setCentralWidget(self.centralwidget)

        # 翻译UI界面文本
        self.retranslateUi(Delete_Window)

        # 连接UI界面的槽函数
        QMetaObject.connectSlotsByName(Delete_Window)

    # setupUi

    def cancel_delete_tasks(self):
        self.close()

    def delete_selected_tasks(self):
        # 获取选择模型
        selection_model = self.task_table.selectionModel()

        # 获取所有选中的索引
        selected_indexes = [index.row() for index in selection_model.selectedRows()]

        # 根据索引获取选中的任务标题
        selected_titles = []
        for index in selected_indexes:
            item = self.task_table.item(index, 0)
            if item:
                selected_titles.append(item.text())

        # 打印选中的任务标题
        # print("Selected task titles:", selected_titles)

        # 在数据库中根据title删除选中的任务
        conn, cursor = make_connect()
        name = self.name
        for title in selected_titles:
            sql = "SELECT * FROM {} where title = '{}'".format(name, title)
            cursor.execute(sql)  # 执行查询操作
            result = cursor.fetchall()  # 获取查询结果，返回元组
            if len(result) == 0:
                print(f'No title named {title} in table {name}')
            else:
                sql = "DELETE FROM {} where title = '{}'".format(name, title)
                cursor.execute(sql)
                conn.commit()
                print(f'user {name} delete task<{title}> successfully')
        break_connect(conn, cursor)  # 关闭游标和连接

        # scan_schedule(self.name)  # 删除后任务列表
        self.taskCreated.emit()
        self.close()

    def retranslateUi(self, Delete_Window):
        Delete_Window.setWindowTitle(QCoreApplication.translate("Delete", u"DeleteWindow", None))
        ___qtablewidgetitem = self.task_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Delete", u"title", None))
        ___qtablewidgetitem1 = self.task_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Delete", u"priority", None))
        ___qtablewidgetitem2 = self.task_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Delete", u"deadline", None))
        ___qtablewidgetitem3 = self.task_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Delete", u"description", None))
        ___qtablewidgetitem4 = self.task_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Delete", u"state", None))
        self.Ok_Button.setText(QCoreApplication.translate("Delete", u"Ok", None))
        self.Cancel_Button.setText(QCoreApplication.translate("Delete", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Delete", u"Select the task you want to delete by clicking the mouse, Ctrl+ click to achieve multiple selection", None))
    # retranslateUi
