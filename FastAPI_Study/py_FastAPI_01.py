from fastapi import FastAPI
from pydantic import BaseModel


# 创建 FastAPI 应用实例
# 创建 post 请求


app= FastAPI(
    title="商品管理 API",
    description="这是一个用于学习 FastAPI 的商品接口示例",
    version="1.0.0",
    contact={
        "name": "张三",
        "email": "zhangsan@example.com",
    },
)

# 禁用文档
# app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 定义请求体数据模型
class Item(BaseModel):
    name: str   # 必填：商品名称
    description: str| None = None   # 可选：商品描述
    price: float    # 必填：商品价格
    tax: float | None = None     # 可选：税费

# 定义根路径的GET路由
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
@app.get(
    "/items/{item_id}",
    summary="获取商品信息",
    description="根据商品 ID 查询商品详情",
    tags=["商品管理"],
)
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "苹果"}
# 定义路径POST路由

@app.post("/items/")
async def create_item(item: Item):
    """创建新商品，接收 JSON 请求体"""
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """更新指定商品，同时使用路径参数和请求体"""
    return {"item_id": item_id, "item": item}


# 使用tags分组 tags 参数可以将相关的路由归为一组，在文档中更清晰地展示
@app.get("/users/",tags=["用户管理"])
async def read_users():
    return [{"username": "张杰"},{"username":"李娜"}]

@app.get("/itemsd/", tags=["商品管理"])
async def read_items():
    return [{"name": "Foo"}, {"name": "Bar"}]