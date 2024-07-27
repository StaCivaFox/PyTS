from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QApplication, QPushButton,
                               QListWidgetItem, QLabel, QHBoxLayout, QDateEdit, QTableWidget, QTableWidgetItem)
from PySide6.QtGui import QColor, QFont
from datetime import datetime
from task import Task
from datetime import date

class ReminderWidget(QWidget):
    def __init__(self):
        super().__init__()
        #self.task_list = task_list
        self.init_ui()

    def change_tasks(self, tasks):
        self.task_list = tasks

    def init_ui(self):
        layout = QVBoxLayout()

        # 添加 QLabel 显示当前日期
        self.date_label = QLabel()
        today = datetime.now().strftime('%Y-%m-%d')
        self.date_label.setText(f"Today's Date: {today}")
        layout.addWidget(self.date_label)

        # 用户选择日期
        layout2 = QHBoxLayout()
        self.input_label = QLabel()
        self.input_label.setText("Select a date:")
        layout2.addWidget(self.input_label)
        self.date_edit = QDateEdit(QDate.fromString(datetime.now().strftime('%Y-%m-%d'), 'yyyy-MM-dd'), self)
        self.date_edit.setDateRange(QDate.fromString(datetime(2020, 1, 1).strftime('%Y-%m-%d'), 'yyyy-MM-dd'),
                                    QDate.fromString(datetime(2030, 12, 31).strftime('%Y-%m-%d'), 'yyyy-MM-dd'))
        layout2.addWidget(self.date_edit)
        layout.addLayout(layout2)

        # 触发显示任务按钮
        self.show_button = QPushButton("Show tasks before selected date")
        self.show_button.clicked.connect(self.update_table)
        layout.addWidget(self.show_button)

        # 表格显示任务
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['Title', 'Priority', 'Deadline', 'Description', 'State'])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

    def update_table(self):
        chosen_date = self.date_edit.date().toPython()
        self.table_widget.setRowCount(0)  # 清空表格
        selected_tasks = []
        # 筛选任务（今日及今日后，指定日期前）
        for task in self.task_list:
            if date.today() <= task.deadline.date() <= chosen_date:
                selected_tasks.append(task)
        # 按deadline升序，priority降序
        selected_tasks.sort(reverse=False, key=lambda task: (task.deadline, -task.priority))
        # 将任务添加到表格
        for task in selected_tasks:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            # 创建单元格并设置内容
            for column, content in enumerate(
                    [task.title, task.priority, task.deadline.strftime('%Y-%m-%d'), task.description, task.state]):
                item = QTableWidgetItem(str(content))
                if task.deadline.date() == date.today():
                    # 设置当日任务颜色
                    item.setBackground(self.get_priority_color(task.priority))
                else:
                    # 设置非当日任务的背景颜色为白色
                    item.setBackground(QColor(255, 255, 255))

                self.table_widget.setItem(row_position, column, item)

    def get_priority_color(self, priority):
        # 根据优先级返回颜色
        colors = {
            1: QColor(255, 255, 102),   # 黄色 - 低优先级
            2: QColor(255, 165, 0),     # 橙色 - 中等优先级
            3: QColor(255, 0, 0),       # 红色 - 高优先级
            4: QColor(156, 0, 0)        # 深红色 - 紧急优先级
        }
        return colors.get(priority, QColor(255, 255, 255))  # 默认颜色为白色

############################################### test #############################################################
# tasks = [
#     Task("Task1", 4, datetime.strptime("2024-07-27", '%Y-%m-%d'), "This is an urgent task", "Not Started"),
#     Task("Task3", 1, datetime.strptime("2024-07-27", '%Y-%m-%d'), "This is a low priority task", "Completed"),
#     Task("Task5", 2, datetime.strptime("2024-07-28", '%Y-%m-%d'), "This is a medium priority task", "In Progress"),
#     Task("Task7", 1, datetime.strptime("2024-07-28", '%Y-%m-%d'), "This is a low priority task", "In Progress"),
#     Task("Task6", 3, datetime.strptime("2024-07-28", '%Y-%m-%d'), "This is a high priority task", "In Progress"),
#     Task("Task2", 3, datetime.strptime("2024-07-27", '%Y-%m-%d'), "This is a high priority task", "In Progress"),
#     Task("Task4", 2, datetime.strptime("2024-07-27", '%Y-%m-%d'), "This is a medium priority task", "In Progress"),
# ]
#
# app = QApplication([])
# reminder_page = ReminderWidget(tasks)
# reminder_page.show()
# app.exec()
############################################### test #############################################################
