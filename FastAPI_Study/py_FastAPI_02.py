# 请求和Cookie
from fastapi import Header,Cookie
# 使用 Header 和 Cookie 类型注解获取请求头和 Cookie 数据。

from fastapi import FastAPI



app = FastAPI(
title="学习的 API",
    description="这是一个用于学习 FastAPI 的样式接口示例",
    version="1.0.0",
    contact={
        "name": "张三",
        "email": "zhangsan@example.com",
    },
)

@app.get("/items/")
def read_item(user_agent: str = Header(None), session_token: str = Cookie(None)):
    return {"User-Agent": user_agent, "Session-Token": session_token}