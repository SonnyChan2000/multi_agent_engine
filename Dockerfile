# 用Python 3.11 作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR / app

# 把依赖文件拷进来
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝整个项目代码
COPY . .

# 暴露端口(FastAPI 默认 8000)
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
