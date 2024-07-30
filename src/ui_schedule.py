# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleEEjvWW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import itertools
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *
from windowsInUi_schedule.ui_addTasks import Ui_AddTasks
from windowsInUi_schedule.ui_addTimePeriod import Ui_AddTimePeriod
from windowsInUi_schedule.ui_viewSelectedTime import Ui_ViewSelectedTime
from windowsInUi_schedule.ui_viewSelectedTasks import Ui_ViewSelectedTasks
import windowsInUi_schedule.schedule_globals as schedule_globals
import globals

class Ui_Schedule(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(965, 590)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 921, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.tableWidget.setColumnWidth(0, 150)  # Set width for the first column

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        self.initButton()

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Add Time Period", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add Task", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Selected Time Period", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Selected Tasks", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Schedule", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Time Period", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Title", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Style", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Priority", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Description", None));
    # retranslateUi

    def initButton(self):
        self.pushButton_2.clicked.connect(self.addTime)
        self.pushButton.clicked.connect(self.addTasks)
        self.pushButton_4.clicked.connect(self.viewTime)
        self.pushButton_3.clicked.connect(self.viewTasks)
        self.pushButton_5.clicked.connect(self.schedule)

    def addTime(self):
        self.addTimeWindow = Ui_AddTimePeriod()
        self.addTimeWindow.show()

    def addTasks(self):
        #print(globals.tasks)
        self.addTaskWindow = Ui_AddTasks()
        self.addTaskWindow.show()

    def viewTime(self):
        self.viewTimeWindow = Ui_ViewSelectedTime()
        self.viewTimeWindow.show()

    def viewTasks(self):
        self.viewTaskWindow = Ui_ViewSelectedTasks()
        self.viewTaskWindow.show()

    def showSchedule(self, time_period_to_tasks):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for time_period, tasks in time_period_to_tasks.items():
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(time_period.toString()))
            for task in tasks:
                self.tableWidget.setItem(row, 1, QTableWidgetItem(task.get_title()))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(task.get_style()))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(task.get_priority())))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(task.get_description()))
                if task.get_style() != time_period.get_style():
                    self.tableWidget.item(row, 1).setBackground(QColor(255, 255, 200))
                    self.tableWidget.item(row, 2).setBackground(QColor(255, 255, 200))
                    self.tableWidget.item(row, 3).setBackground(QColor(255, 255, 200))
                    self.tableWidget.item(row, 4).setBackground(QColor(255, 255, 200))


    def schedule(self):
        if schedule_globals.selected_tasks == [] or schedule_globals.selected_periods == []:
            QMessageBox.information(self, "Schedule", "Please add tasks and time periods first! Neither of them can be empty.")
            return
        time_period_to_tasks = {}
        for time_period in schedule_globals.selected_periods:
            time_period_to_tasks[time_period] = []
        sorted_tasks = sorted(schedule_globals.selected_tasks, key=lambda task: (task.deadline, task.priority), reverse=True)
        for task in itertools.chain(sorted_tasks):
            time_cost = task.get_expection() * 3600
            task_style = task.get_style()
            while time_cost > 0:
                flag = 0
                for time_period in schedule_globals.selected_periods:
                    if time_period.get_style() == task_style and time_period.get_duration() > 0 and time_period_to_tasks[time_period] == []:
                        time_period_to_tasks[time_period].append(task)
                        time_cost -= time_period.get_duration()
                        flag = 1
                        break
                if flag == 0:
                    break
            if time_cost <= 0:
                sorted_tasks.remove(task)

        self.showSchedule(time_period_to_tasks)
        if sorted_tasks == []:
            QMessageBox.information(self, "Schedule", "Schedule successfully!")
        else:
            reply = QMessageBox.question(self, "Schedule", "There are still some tasks not scheduled, probably due to styles not matching. Do you want to continue scheduling anyway?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            for task in itertools.chain(sorted_tasks):
                time_cost = task.get_expection() * 3600
                while time_cost > 0:
                    flag = 0
                    for time_period in schedule_globals.selected_periods:
                        if time_period.get_duration() > 0 and time_period_to_tasks[time_period] == []:
                            time_period_to_tasks[time_period].append(task)
                            time_cost -= time_period.get_duration()
                            flag = 1
                            break
                    if flag == 0:
                        break
                if time_cost <= 0:
                    sorted_tasks.remove(task)
            self.showSchedule(time_period_to_tasks)
            if sorted_tasks == []:
                QMessageBox.information(self, "Schedule", "Schedule successfully! Yellow backgrounds, if any, indicate that the style of the task does not match the style of the time period.")
            else:
                QMessageBox.information(self, "Schedule", "Schedule failed! Please add more time periods or delete some tasks from scheduling.")
        


# app = QApplication([])
# mainWindow = Ui_Schedule()
# mainWindow.show()
# app.exec()
