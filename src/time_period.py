from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

class TimePeriod():
    def __init__(self, begin, end, style) -> None:
        self.beginTime = begin
        self.endTime = end
        self.style = style


    def __str__(self) -> str:
        return f"{self.beginTime} {self.endTime} {self.style}"
    

    def get_beginTime(self):
        return self.beginTime
    
    def get_endTime(self):
        return self.endTime
    
    def get_style(self):
        return self.style
    
    def set_begin(self, begin):
        self.beginTime = begin

    def set_end(self, end):
        self.endTime = end

    def set_style(self, style):
        self.style = style

    def get_duration(self):
        return self.beginTime.secsTo(self.endTime)
    
    def toString(self):
        return f"{self.beginTime.toString()} - {self.endTime.toString()}"