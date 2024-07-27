#TODO: 与后端对接
class Task():
    def __init__(self, title, priority, deadline, description, state
                 #TODO: 添加更多任务信息
                 ) -> None:
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.description = description
        self.state = state

    def __str__(self) -> str:
        return f"{self.title} {self.priority} {self.deadline} {self.description} {self.state}"
    
    def get_title(self):
        return self.title