import yaml
from myworkflow.agents_builtin import Researcher, Analyst, Writer
from myworkflow.log_config import logger

class_registry = {
    "researcher": Researcher,
    "analyst": Analyst,
    "writer": Writer,
}

def load_workflow(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    agents = {}
    for name, info in cfg["agents"].items():
        cls = class_registry[info["type"]]
        agents[name] = cls(name, info["role"], info["prompt"])

    flow = cfg["flow"]
    logger.info(f"初始化工作流: {list(agents.keys())} Agent, {len(flow)}步")
    return agents, flow

