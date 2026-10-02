import os
from dotenv import load_dotenv
from myworkflow.agent import Agent
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

class Researcher(Agent):
    def run(self, task):
        resp = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": f"{self.prompt}\n任务: {task}"}]
        )
        return resp.choices[0].message.content

class Analyst(Agent):
    def run(self, task):
        resp = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": f"{self.prompt}\n任务: {task}"}]
        )
        return resp.choices[0].message.content

class Writer(Agent):
    def run(self, task):
        resp = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": f"{self.prompt}\n任务: {task}"}]
        )
        return resp.choices[0].message.content