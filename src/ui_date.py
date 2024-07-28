# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dateKchDiw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
from login import *
import globals


class Ui_Date(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 497)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        __qtablewidgetitem6.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        __qtablewidgetitem7.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        __qtablewidgetitem8.setBackground(QColor(213, 211, 185));
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 50, 751, 391))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(81)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 71, 41))
        font2 = QFont()
        font2.setFamilies([u"Monotype Corsiva"])
        font2.setPointSize(22)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 768, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"title", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"deadline", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"begin", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"expection", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"priority", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"style", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"daily", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"description", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"state", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
    # retranslateUi


    def initDateWindow(self, date):
        self.tableWidget.setRowCount(0)
        task_list = search_schedule_by_date(globals.login_user.get_username(), date)
        taskList = sort_schedules_by_deadline(task_list)
        task_list1 = []
        for task in taskList:
            if task.begin.datetime() <= date <= task.deadline.datetime():
                task_list1.append(task)
        self.tableWidget.setRowCount(len(task_list1))
        # 逐行显示
        for row_idx, task in enumerate(task_list1):
            self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(task.title))
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(task.deadline.strftime("%Y-%m-%d %H:%M:%S")))
            self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(task.begin.strftime("%Y-%m-%d %H:%M:%S")))
            self.tableWidget.setItem(row_idx, 3, QTableWidgetItem(task.expection))
            self.tableWidget.setItem(row_idx, 4, QTableWidgetItem(str(task.priority)))
            self.tableWidget.setItem(row_idx, 5, QTableWidgetItem(task.style))
            if task.daily == 1:
                self.tableWidget.setItem(row_idx, 6, QTableWidgetItem('Yes'))
            else:
                self.tableWidget.setItem(row_idx, 6, QTableWidgetItem('No'))
            self.tableWidget.setItem(row_idx, 7, QTableWidgetItem(task.description))
            self.tableWidget.setItem(row_idx, 8, QTableWidgetItem(str(task.state)))
        self.tableWidget.resizeColumnsToContents()  # 调整列宽以适应内容
        min_width = 50
        for i in range(self.tableWidget.columnCount()):  # 设置最小列宽
            self.tableWidget.setColumnWidth(i, max(min_width, self.tableWidget.columnWidth(i)))
