from fastapi import FastAPI
from pydantic import BaseModel
from myworkflow.loader import load_workflow
from myworkflow.engine import WorkflowEngine
from fastapi.staticfiles import StaticFiles
import os

BASE = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Multi-Agent工作流引擎")
app.mount("/static", StaticFiles(directory=os.path.join(BASE, "static")), name="static")

# 请求体: 用户传一个task
class RunRequest(BaseModel):
    task: str

@app.post("/run")
def run(req: RunRequest):
    # 1.从YAML加载默认工作流
    agents, flow = load_workflow("configs/workflow.yaml")
    # 2.把用户传的task塞进第一个干活节点的任务
    flow[0]["task"] = req.task
    # 3.跑引擎
    e = WorkflowEngine(agents, flow)
    result = e.run()
    return result

@app.get("/")
def home():
    return {"msg": "Multi-Agent工作流引擎已启动", "用法": "Post/run {task: '主题'}"}