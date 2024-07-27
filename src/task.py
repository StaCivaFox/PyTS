#TODO: 与后端对接
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