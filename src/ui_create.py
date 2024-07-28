# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_create_newrOjqnd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
        MainWindow.resize(886, 477)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(750, 430, 75, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(630, 430, 75, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 30, 241, 31))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 100, 241, 191))
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(580, 100, 194, 22))
        self.dateTimeEdit_2 = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(580, 150, 194, 22))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(150, 380, 68, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(510, 100, 71, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 40, 54, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 180, 71, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(510, 150, 54, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 380, 54, 16))
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(150, 320, 121, 22))
        #self.comboBox_3.setEditable(True)
        self.comboBox_3.currentIndexChanged.connect(self.on_combobox_changed)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 320, 54, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 410, 311, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(510, 250, 61, 16))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(510, 340, 141, 20))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(600, 250, 79, 20))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(660, 340, 42, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.initButton()

        #QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Begin Time", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Sport", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Work/Study", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Chores", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Others", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"The larger the number, the higher the priority.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Daily Task", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Estimated Hours Cost", None))
        self.checkBox.setText("")
    # retranslateUi


    def on_combobox_changed(self, index):
        if self.comboBox_3.currentText() == "Others":
            self.comboBox_3.setEditable(True)
        else:
            self.comboBox_3.setEditable(False)


    def initButton(self):
        self.pushButton_2.clicked.connect(self.clickCancelButton)
        self.pushButton.clicked.connect(self.clickOkButton)


    def clickCancelButton(self): #设置cancel按钮的行为，点击后关闭窗口
        self.close()


    def clickOkButton(self): #设置ok按钮的行为，具体来说是点击ok后，获取填的信息并导入数据库，将这几个框4的信息收集，删除当前名字的task并重新构建一个
        title = self.lineEdit.text()
        description = self.textEdit.toPlainText()
        style = self.comboBox_3.currentText()   #返回string类型
        begin_time_qt = self.dateTimeEdit.dateTime()   #返回是一个QDateTime对象，不想用这种形式可以toString或使用time()等方法获取具体时分秒
        deadline_qt = self.dateTimeEdit_2.dateTime()    
        begin_time = begin_time_qt.toPython()
        deadline = deadline_qt.toPython()
        daily_tf = self.checkBox.isChecked()
        if daily_tf:
            daily = 1
        else:
            daily = 0
        expection = self.spinBox.value()
        priority = self.comboBox_2.currentText()#返回string类型
        state = 0
        if (title == '' or description == '') or (begin_time > deadline):
            if title == '' or description == '':
                QMessageBox.information(self, "Falied", "Title and Description can not be blank.")
            else:
                #提示有字段未填写
                QMessageBox.information(self, "Falied", "Begin time must be earlier than deadline.")
                #self.informWindow = ui_inform_init()
                #self.informWindow.show()
        else: # 连接数据库，先通过title看有没有重复的，有就先删再加（提示用户），没有直接加
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