# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creatMZJhLV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

from ui_inform import ui_inform_init
from login import *
from datetime import datetime
from user import *
from task import *
import globals


class Ui_Create(QMainWindow):
    taskCreated = Signal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 395)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(380, 330, 231, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 20, 291, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 80, 291, 101))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(314, 130, 311, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.dateTimeEdit = QDateTimeEdit(self.horizontalLayoutWidget_4)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 230, 291, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_5.addWidget(self.comboBox_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 230, 301, 51))
        font = QFont()
        font.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(314, 80, 311, 51))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.dateTimeEdit_2 = QDateTimeEdit(self.horizontalLayoutWidget_7)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.horizontalLayout_7.addWidget(self.dateTimeEdit_2)

        self.horizontalLayoutWidget_8 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(314, 20, 311, 51))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_8)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.comboBox_3 = QComboBox(self.horizontalLayoutWidget_8)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.currentIndexChanged.connect(self.on_combobox_changed)

        self.horizontalLayout_8.addWidget(self.comboBox_3)

        self.horizontalLayoutWidget_9 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(314, 180, 311, 51))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.spinBox = QSpinBox(self.horizontalLayoutWidget_9)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_9.addWidget(self.spinBox)

        self.horizontalLayoutWidget_10 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(20, 180, 291, 51))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget_10)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.checkBox = QCheckBox(self.horizontalLayoutWidget_10)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_10.addWidget(self.checkBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 641, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.initButton()
        # QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title       ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"The larger the number, the higher the priority", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Begin time", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Sport", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Work/Study", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Chores", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Others", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Estimated Hours Cost", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Daily Task", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi

    def on_combobox_changed(self, index):
        if self.comboBox_3.currentText() == "Others":
            self.comboBox_3.setEditable(True)
        else:
            self.comboBox_3.setEditable(False)

    def initButton(self):
        self.pushButton.clicked.connect(self.clickCancelButton)
        self.pushButton_2.clicked.connect(self.clickOkButton)

    def clickCancelButton(self):  # 设置cancel按钮的行为，点击后关闭窗口
        self.close()

    def clickOkButton(self):  # 设置ok按钮的行为，具体来说是点击ok后，获取填的信息并导入数据库，将这几个框4的信息收集，删除当前名字的task并重新构建一个
        title = self.lineEdit.text()
        description = self.textEdit.toPlainText()
        style = self.comboBox_3.currentText()  # 返回string类型
        begin_time_qt = (self.dateTimeEdit_2.dateTime())  # 返回是一个QDateTime对象，不想用这种形式可以toString或使用time()等方法获取具体时分秒
        deadline_qt = self.dateTimeEdit.dateTime()
        begin_time = begin_time_qt.toPython()
        deadline = deadline_qt.toPython()
        daily_tf = self.checkBox.isChecked()
        if daily_tf:
            daily = 1
        else:
            daily = 0
        expection = self.spinBox.value()
        priority = self.comboBox_2.currentText()  # 返回string类型
        state = 0
        if (title == '' or description == '') or (begin_time > deadline):
            if title == '' or description == '':
                QMessageBox.information(self, "Falied", "Title and Description can not be blank.")
            else:
                # 提示有字段未填写
                QMessageBox.information(self, "Falied", "Begin time must be earlier than deadline.")
                # self.informWindow = ui_inform_init()
                # self.informWindow.show()
        else:  # 连接数据库，先通过title看有没有重复的，有就先删再加（提示用户），没有直接加
            new_task = Task(title, style, priority, daily, begin_time, deadline, expection, description, state)
            result, msg = add_schedule(globals.login_user.get_username(), new_task)
            if result:
                QMessageBox.information(self, "Success", "Successfully add task!")
                self.taskCreated.emit()
                self.close()
            else:
                reply = QMessageBox.question(self, 'Task Exists',
                                             "Task already exists. Do you want to replace it?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    delete_schedule(globals.login_user.get_username(), new_task)
                    result, msg = add_schedule(globals.login_user.get_username(), new_task)
                    if result:
                        QMessageBox.information(self, "Success", "Successfully replaced task!")
                        self.taskCreated.emit()
                        self.close()
                    else:
                        QMessageBox.information(self, "Failed", "Failed to replace task!")
                else:
                    QMessageBox.information(self, "Cancelled", "Task replacement cancelled.")


def ui_create_init():
    return Ui_Create()
