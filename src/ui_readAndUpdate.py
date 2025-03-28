# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creatNyPWdp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QTextEdit,
                               QWidget, QMessageBox, QDateTimeEdit, QSpinBox, QCheckBox)

from task import Task
from ui_inform import ui_inform_init
from datetime import datetime
from login import *
import globals

class Ui_ReadAndUpdate(QMainWindow):
    taskUpdated = Signal()
    def __init__(self, old_task):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.old_task = old_task

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 395)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setWindowIcon(QIcon('icon.ico'))

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

        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(20, 280, 291, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        #self.comboBox = QComboBox(self.horizontalLayoutWidget_6)
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.setObjectName(u"comboBox")

        #self.horizontalLayout_6.addWidget(self.comboBox)

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
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Update", None))
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

        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"The larger the number, the higher the priority", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Begin Time", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Sport", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Work/Study", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Chores", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Others", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Estimated Hours Cost", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Daily Task", None))
        self.checkBox.setText("")
        #self.label_5.setText(QCoreApplication.translate("MainWindow", u"State", None))
        #self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"unstarted", None))
        #self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ongoing", None))
        #self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"completed", None))
        #self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"expired", None))
    # retranslateUi


    def initButton(self):
        self.pushButton.clicked.connect(self.clickCancelButton)
        self.pushButton_2.clicked.connect(self.clickOkButton)


    def clickCancelButton(self): #设置cancel按钮的行为，点击后关闭窗口
        self.close()

    #TODO: state不应提供4种选项，编辑窗口中删除这项，在主页面每条task后加框，打钩后状态变为completed.
    def clickOkButton(self):  # 设置ok按钮的行为，具体来说是点击ok后，获取填的信息并导入数据库，将这几个框4的信息收集，删除当前名字的task并重新构建一个
        title = self.lineEdit.text()
        description = self.textEdit.toPlainText()
        style = self.comboBox_3.currentText()  # 返回string类型
        begin_time_qt = self.dateTimeEdit_2.dateTime()  # 返回是一个QDateTime对象，不想用这种形式可以toString或使用time()等方法获取具体时分秒
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
        #state_text = self.comboBox.currentText()
        #if state_text == 'unstarted':
        #    state = 0
        #elif state_text == 'ongoing':
        #    state = 1
        #elif state_text == 'completed':
        #    state = 2
        #else:
        #    state = 3
        state = self.old_task.state
        if (title == '' or description == '') or (begin_time > deadline):
            if title == '' or description == '':
                QMessageBox.information(self, "Falied", "Title and Description can not be blank.")
            else:
                # 提示有字段未填写
                QMessageBox.information(self, "Falied", "Begin time must be earlier than deadline.")
                # self.informWindow = ui_inform_init()
                # self.informWindow.show()
        else:  # 连接数据库，先通过title看有没有重复的，有就先删再加（提示用户），没有直接加
            reply = QMessageBox.question(self, 'Update confirm',
                                         "Are you sure to update this task?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            old_task = self.old_task
            new_task = Task(title, style, priority, daily, begin_time, deadline, expection, description, state)
            #if search_schedule_by_title(globals.login_user.get_username(), old_task.get_title()):
            #    delete_schedule(globals.login_user.get_username(), old_task)
            if old_task.get_title() == title:
                delete_schedule(globals.login_user.get_username(), old_task)
                result, msg = add_schedule(globals.login_user.get_username(), new_task)
            else:
                #新标题和旧的有重复
                if search_schedule_by_title(globals.login_user.get_username(), new_task.get_title()):
                    replace_reply = QMessageBox.question(self, 'Update confirm', "Task with the same title already exists. Do you want to replace it?",
                                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if replace_reply == QMessageBox.No:
                        return
                    delete_schedule(globals.login_user.get_username(), new_task)
                    result, msg = add_schedule(globals.login_user.get_username(), new_task)
                #没有重复
                else:
                    delete_schedule(globals.login_user.get_username(), old_task)
                    result, msg = add_schedule(globals.login_user.get_username(), new_task)
            if result:
                QMessageBox.information(self, "Success", "Successfully updated task!")
                self.taskUpdated.emit()
                self.close()
            else:
                QMessageBox.information(self, "Failed", "Failed to update task! " + msg)
                    


    def initWord(self, title, priority, deadline, begin, style, daily, expection, description, state): #在show之前调用，获取那几项要提前展示的内容并设置
        if state == 0:
            print_state = 'unstarted'
        elif state == 1:
            print_state = 'ongoing'
        elif state == 2:
            print_state = 'completed'
        else:
            print_state = 'expired'
        self.lineEdit.setText(title)
        self.textEdit.setText(description)
        deadline_qt = QDateTime.fromString(deadline, "yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit.setDateTime(deadline_qt)
        begin_qt = QDateTime.fromString(begin, "yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_2.setDateTime(begin_qt)
        #self.comboBox.setCurrentText(print_state)
        self.comboBox_2.setCurrentText(priority)
        self.comboBox_3.setCurrentText(style)
        self.spinBox.setValue(expection)
        self.checkBox.setChecked(daily)

# app = QApplication([])
# mainWindow = Ui_ReadAndUpdate()
# mainWindow.initWord('11','1','','','Sport',1,2,'111111','unstarted')
# mainWindow.show()
# app.exec()