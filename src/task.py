#TODO: 与后端对接
import datetime

class Task():
    def __init__(self, title, style, priority, daily, begin, deadline, expection, description, state
                 #TODO: 添加更多任务信息
                 ) -> None:
        self.title = title
        self.style = style
        self.priority = priority
        self.daily = daily
        self.begin = begin
        self.deadline = deadline
        self.expection = expection
        self.description = description
        self.state = state

    def __str__(self) -> str:
        return f"{self.title} {self.style} {self.priority} {self.daily} {self.begin} {self.deadline} {self.expection} {self.description} {self.state}"
    
    
    def get_title(self):
        return self.title

    def get_style(self):
        return self.style
    
    def get_priority(self):
        return self.priority
    
    def get_daily(self):
        return self.daily
    
    def get_begin(self):
        return self.begin
    
    def get_deadline(self):
        return self.deadline
    
    def get_expection(self):
        return self.expection
    
    def get_description(self):
        return self.description
    
    def get_state(self):
        return self.state
    
    def deep_clone(self):
        return Task(self.title, self.style, self.priority, self.daily, self.begin, self.deadline, self.expection, self.description, self.state)
    
    def available_for_schedule(self):
        today_date = datetime.datetime.now()
        if self.state != 2 and self.begin <= today_date:
            return True
        return False