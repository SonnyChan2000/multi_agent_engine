from myworkflow.log_config import logger
import time

class WorkflowEngine:
    def __init__(self, agents, flow):
        self.agents = agents   # 专家字典 {"researcher": agent实例, ...}
        self.flow = flow       # 流程列表（干活节点 + 分支节点混排）
        self.state = {}        # 每步结果进度表
        self.last_value = ""

    def run(self):
        i = 0
        while i < len(self.flow):
            step = self.flow[i]

            # ---- 干活节点：唤醒Agent执行，结果存state ----
            if "name" in step:
                name = step["name"]
                task = step["task"]
                logger.info(f"执行Agent: {name}, 任务: {task}")
                t0 = time.time()
                result = self.agents[name].run(f"{task}\n\n【上一步结果】\n{self.last_value}")
                self.last_value = result
                cost = time.time() - t0
                self.state[name] = result
                logger.info(f"{name}完成, 耗时{cost:.2f}s, 长度{len(result)}字")
                i += 1

            # ---- 分支节点：看某步结果，就地执行选中的分支 ----
            elif "branch" in step:
                b = step["branch"]
                target = b["target"]                      # 看哪步结果
                prev = self.state.get(target, "")         # 取出那步结果
                if b["contains"] in prev:
                    chosen = b["then"]
                    logger.info(f"分支{target}命中'{b['contains']}' -> 走then: {chosen['name']}")
                else:
                    chosen = b["else"]
                    logger.info(f"分支{target}未命中 -> 走else: {chosen['name']}")
                # chosen 是 {"name":..., "task":...}，直接当场执行它
                name = chosen["name"]
                task = chosen["task"]

                logger.info(f"执行Agent: {name}, 任务: {task}")
                t0 = time.time()
                result = self.agents[name].run(f"{task}\n\n【上一步结果】\n{self.last_value}")
                self.last_value = result
                cost = time.time() - t0
                self.state[name] = result
                logger.info(f"{name}完成, 耗时 {cost:.2f}s, 长度{len(result)}字")
                i += 1

            # ---- 兜底：跳过不认识的结构，防崩 ----
            else:
                i += 1

        return self.state

