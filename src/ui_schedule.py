# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleEEjvWW.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from windowsInUi_schedule.ui_addTasks import Ui_AddTasks
from windowsInUi_schedule.ui_addTimePeriod import Ui_AddTimePeriod
from windowsInUi_schedule.ui_viewSelectedTime import Ui_ViewSelectedTime
from windowsInUi_schedule.ui_viewSelectedTasks import Ui_ViewSelectedTasks

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
        self.addTaskWindow = Ui_AddTasks()
        self.addTaskWindow.show()

    def viewTime(self):
        self.viewTimeWindow = Ui_ViewSelectedTime()
        self.viewTimeWindow.show()

    def viewTasks(self):
        self.viewTaskWindow = Ui_ViewSelectedTasks()
        self.viewTaskWindow.show()

    def schedule(self):
        pass

# app = QApplication([])
# mainWindow = Ui_Schedule()
# mainWindow.show()
# app.exec()
