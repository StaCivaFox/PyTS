# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Selected TaksmmcJQS.ui'
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
from PySide6.QtWidgets import *

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from task import *
import windowsInUi_schedule.schedule_globals as schedule_globals
import globals

class Ui_ViewSelectedTasks(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showSelectedTasks()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 441)

        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setWindowIcon(QIcon('icon.ico'))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 681, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Lucida Calligraphy"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        #__qtablewidgetitem = QTableWidgetItem()
        #self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置为整行选中

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 689, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.initButton()

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selected Tasks", None))
        #___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        #___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Deleted", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Style", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Priority", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

    def initButton(self):
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.delete)

    def showSelectedTasks(self):
        self.tableWidget.setRowCount(len(schedule_globals.selected_tasks))
        for i in range(len(schedule_globals.selected_tasks)):
            task = schedule_globals.selected_tasks[i]
            item = QTableWidgetItem(task.get_title())
            self.tableWidget.setItem(i, 0, item)
            item = QTableWidgetItem(task.get_style())
            self.tableWidget.setItem(i, 1, item)
            item = QTableWidgetItem(str(task.get_priority()))
            self.tableWidget.setItem(i, 2, item)
            item = QTableWidgetItem(task.get_description())
            self.tableWidget.setItem(i, 3, item)
            item = QTableWidgetItem(str(task.get_expection()))
            self.tableWidget.setItem(i, 4, item)

    def cancel(self):
        self.close()

    def delete(self):
        selection_model = self.tableWidget.selectionModel()
        selected_indexes = [index.row() for index in selection_model.selectedRows()]
        selected_titles = []
        for index in selected_indexes:
            item = self.tableWidget.item(index, 0)
            if item:
                selected_titles.append(item.text())
        reply = QMessageBox.question(self, "Warning", "Are you sure you want to delete the selected task(s)? You can add them back for scheduling through the 'Add Tasks' button.",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        for title in selected_titles:
            for task in schedule_globals.selected_tasks:
                if task.get_title() == title:
                    schedule_globals.selected_tasks.remove(task)
        QMessageBox.information(self, "Success", "Successfully deleted task(s) from scheduling.")
        self.showSelectedTasks()


# app = QApplication([])
# mainWindow = Ui_ViewSelectedTasks()
# mainWindow.show()
# app.exec()