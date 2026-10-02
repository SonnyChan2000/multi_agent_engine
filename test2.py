import os
from myworkflow.tool import Tool
from myworkflow.agent import Agent
from myworkflow.engine import WorkflowEngine
from myworkflow.agents_builtin import Researcher, Analyst, Writer
from myworkflow.loader import load_workflow


# class FakeResearcher(Agent):
#     def run(self, task):
#         return "调研" + task + ": 失败, 未找到相关数据"

# class FakeAnalyst(Agent):
#     def run(self, task):
#         return "分析" + task + ": 成功, 得出3条结论"

# class FakeWriter(Agent):
#     def run(self, task):
#         return f"{task}：报告写好了"

# agents = {
#     "researcher": Researcher("researcher", "研究员", "查资料"),
#     "analyst": Analyst("analyst", "分析师", "做分析"),
#      "writer": Writer("writer", "写手", "写报告"),
# }

# flow = [
#     {"name": "researcher", "task": "AI行业"},
#     {"branch": {
#         "target": "researcher",
#         "contains": "失败",
#         "then": {"name": "researcher", "task": "换个关键词重查"},
#         "else": {"name": "analyst", "task": "分析结果"}
#     }},
#     {"name": "writer", "task": "写报告"},
# ]

# e = WorkflowEngine(agents, flow)
# print(e.run())
agents, flow = load_workflow("configs/workflow.yaml")
e = WorkflowEngine(agents, flow)
result = e.run()
print(result)