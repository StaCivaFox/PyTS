# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add Time PeriodsdqDxB.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_AddTimePeriod(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(362, 197)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 351, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dateTimeEdit = QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.dateTimeEdit_2 = QDateTimeEdit(self.verticalLayoutWidget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 362, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.initButton()

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Begin Time", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End Time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sport", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Work/Study", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Chores", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Others", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

    def on_combobox_changed(self, index):
        if self.comboBox.currentText() == "Others":
            self.comboBox.setEditable(True)
        else:
            self.comboBox.setEditable(False)

    def initButton(self):
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.add)

    def cancel(self):
        self.close()

    def add(self):
        beginTime = self.dateTimeEdit.dateTime()
        endTime = self.dateTimeEdit_2.dateTime()
        style = self.comboBox.currentText()
        pass

# app = QApplication([])
# mainWindow = Ui_AddTimePeriod()
# mainWindow.show()
# app.exec()