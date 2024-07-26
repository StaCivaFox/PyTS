# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design(1)ePBWrY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_create import Ui_Create
from ui_readAndUpdate import Ui_ReadAndUpdate


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 643)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalFrame.setAutoFillBackground(False)

        self.verticalFrame1 = QFrame(self.verticalFrame)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalFrame1.setMaximumSize(QSize(100, 16777215))
        self.verticalFrame1.setAutoFillBackground(False)

        #init stack and page
        self.stackedWidget = QStackedWidget(self.verticalFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.initCalendar()
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.stackedWidget.setCurrentIndex(1)

        self.verticalFrame2 = QFrame(self.page_4)
        self.verticalFrame2.setObjectName("verticalFrame2")
        self.verticalFrame2.setGeometry(QRect(0, 10, 821, 571))

        self.horizontalFrame = QFrame(self.verticalFrame2)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 30))

        self.initLabel()
        self.initHomeTable()
        self.initLayout()
        self.initButton()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def initButton(self):
        self.homeButton = QPushButton(self.verticalFrame1)
        self.homeButton.setObjectName("homeButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.homeButton.setIcon(icon)
        self.verticalLayout_2.addWidget(self.homeButton)

        self.calendarButton = QPushButton(self.verticalFrame1)
        self.calendarButton.setObjectName("calendarButton")
        self.verticalLayout_2.addWidget(self.calendarButton)

        self.reminderButton = QPushButton(self.verticalFrame1)
        self.reminderButton.setObjectName("reminderButton")
        self.verticalLayout_2.addWidget(self.reminderButton)

        self.schedulerButton = QPushButton(self.verticalFrame1)
        self.schedulerButton.setObjectName("schedulerButton")
        self.verticalLayout_2.addWidget(self.schedulerButton)

        self.createButton = QPushButton(self.horizontalFrame)
        self.createButton.setObjectName("createButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.createButton.setIcon(icon1)
        self.horizontalLayout_2.addWidget(self.createButton)

        self.readButton = QPushButton(self.horizontalFrame)
        self.readButton.setObjectName("readButton")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.readButton.setIcon(icon2)
        self.horizontalLayout_2.addWidget(self.readButton)

        self.updateButton = QPushButton(self.horizontalFrame)
        self.updateButton.setObjectName("updateButton")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.updateButton.setIcon(icon3)
        self.horizontalLayout_2.addWidget(self.updateButton)

        self.deleteButton = QPushButton(self.horizontalFrame)
        self.deleteButton.setObjectName("deleteButton")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.deleteButton.setIcon(icon4)
        self.horizontalLayout_2.addWidget(self.deleteButton)
        #实现button与其他行为的关联
        self.createButton.clicked.connect(self.clickCreateButton)
        self.deleteButton.clicked.connect(self.clickDeleteButton)
        self.homeButton.clicked.connect(self.switchPage)
        self.calendarButton.clicked.connect(self.switchPage)

    def initLayout(self):
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QHBoxLayout(self.verticalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.verticalFrame1)
        self.verticalLayout_4.addWidget(self.horizontalFrame)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.verticalFrame)

    def initHomeTable(self):
        self.tableWidget = QTableWidget(self.verticalFrame2)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) #设置为整行选中
        self.tableWidget.clicked.connect(self.clickTable)

    def initLabel(self):
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")

    def initCalendar(self):
        self.calendarWidget = QCalendarWidget(self.page_3)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 10, 821, 571))
        self.calendarWidget.clicked.connect(self.clickCalendar)

    def clickCalendar(self):
        date = self.calendarWidget.selectedDate()
        #实现与数据库等待连接，将date传入，获得当天的日程
        print(date)
        pass

    def clickCreateButton(self):
        self.createWindow = Ui_Create()
        self.createWindow.show()

    #read 和 update功能直接合并，取消二者的按钮，直接再表格中选中点击实现查看修改功能
    def clickTable(self):
        row = self.tableWidget.currentRow()
        if row > -1:
            name = self.tableWidget.item(row, 0)#获取任务名字，从数据库中get相关信息并展示，展示一个类似create的弹窗
            # 使用name从数据库获取相关任务
            self.readAndUpdateWindow = Ui_ReadAndUpdate()
            # 下边这一行实现初始化显示，即read的功能
            self.readAndUpdateWindow.initWord()
            self.readAndUpdateWindow.show()

    #delete弹出新窗口，展示所有任务，在任务的右边显示check box， 选后点击确认将所有选中的任务删除，取消直接退出
    def clickDeleteButton(self):
        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">PyTS App</span></p></body></html>", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.reminderButton.setText(QCoreApplication.translate("MainWindow", u"Reminder", None))
        self.schedulerButton.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.readButton.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Required Time", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None))
    # retranslateUi

    def switchPage(self):
        btn = self.sender()
        if btn == self.homeButton: #点击的时候实现一次更新，将之前对task的操作同步到table上
            self.stackedWidget.setCurrentWidget(self.page_4)
            pass
        elif btn == self.calendarButton:
            self.stackedWidget.setCurrentWidget(self.page_3)
        elif btn == self.reminderButton:
            pass
        elif btn == self.schedulerButton:
            pass


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    app.exec()


