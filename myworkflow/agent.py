class Agent:
    def __init__(self, name, role, prompt, tools=None):
        self.name = name
        self.role = role
        self.prompt = prompt
        self.tools = tools if tools is not None else []

    def run(self, task):
        return f"[{self.name}] 待实现, 任务: {task}"