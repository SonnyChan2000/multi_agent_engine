from myworkflow.tool import Tool
from myworkflow.agent import Agent

def add(a, b): return a + b
t = Tool(name="add", description="加法", func=add)
print(t.run(2, 4))

a = Agent(name="researcher",
          role="你是一名严谨的行业研究员",
          prompt="请收集并整理相关信息",
          )
print(a.name)
print(a.tools)
print(a.run("调研AI行业发展"))

a2 = Agent(name="X", role="Y", prompt="Z")
print(a2.tools)

from myworkflow.tool import Tool
from myworkflow.agent import Agent
from myworkflow.engine import WorkflowEngine

a1 = Agent("researcher", "研究员", "查资料")
a2 = Agent("analyst", "分析师", "做分析")
agents = {"researcher": a1, "analyst": a2}
flow = [{"name": "researcher", "task": "调研AI"}, {"name": "analyst", "task": "分析结果"}]

e = WorkflowEngine(agents, flow)
print(e.run())

