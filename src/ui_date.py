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

class Ui_Date(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 412)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        __qtablewidgetitem.setBackground(QColor(213, 211, 185))
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 50, 541, 311))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 0, 221, 49))
        font2 = QFont()
        font2.setFamilies([u"Monotype Corsiva"])
        font2.setPointSize(22)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 562, 33))
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
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"priority", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"description", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"state", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tasks After the Day", None))
    # retranslateUi

    def getTaskList(self, task_list):
        self.tableWidget.setRowCount(len(task_list))
        # 逐行显示
        for row_idx, task in enumerate(task_list):
            self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(task.title))
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(task.priority)))
            self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(task.deadline)))
            self.tableWidget.setItem(row_idx, 3, QTableWidgetItem(task.description))
            self.tableWidget.setItem(row_idx, 4, QTableWidgetItem(str(task.state)))
        self.tableWidget.resizeColumnsToContents()  # 调整列宽以适应内容
        min_width = 50
        for i in range(self.tableWidget.columnCount()):  # 设置最小列宽
            self.tableWidget.setColumnWidth(i, max(min_width, self.tableWidget.columnWidth(i)))


def ui_date_init():
    return Ui_Date()
