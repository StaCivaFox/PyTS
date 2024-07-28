from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout, QLabel
from PyQt6.QtGui import QColor

class ColorPickerDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.color_label = QLabel('Selected Color: None', self)
        self.layout.addWidget(self.color_label)

        self.btn = QPushButton('Pick a Color', self)
        self.btn.clicked.connect(self.showColorDialog)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.setWindowTitle('Color Picker Demo')
        self.show()

    def showColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_label.setText(f'Selected Color: {color.name()} (RGB: {color.red()}, {color.green()}, {color.blue()})')
            self.color_label.setStyleSheet(f'background-color: {color.name()};')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = ColorPickerDemo()
    sys.exit(app.exec())