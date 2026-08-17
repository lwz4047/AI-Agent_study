# FastAPI 学习笔记

本文档记录 `py_FastAPI_01.py` 中已经学习和使用的 FastAPI 基础知识，包括项目启动、路由、参数传递、请求体、自动接口文档和常见错误。

## 1. 启动 FastAPI 项目

进入 `FastAPI_Study` 目录后执行：

```powershell
uvicorn py_FastAPI_01:app --reload
```

命令各部分的含义：

- `uvicorn`：运行 FastAPI 应用的 Web 服务器。
- `py_FastAPI_01`：Python 文件名，不需要写 `.py` 后缀。
- `app`：文件中通过 `app = FastAPI()` 创建的应用对象。
- `--reload`：代码保存后自动重启服务器，适合开发阶段使用。

如果在项目根目录 `D:\pyProject\py_project` 中启动，需要写完整的模块路径：

```powershell
uvicorn FastAPI_Study.py_FastAPI_01:app --reload
```

启动成功后可以访问：

- 接口地址：<http://127.0.0.1:8000>
- Swagger 文档：<http://127.0.0.1:8000/docs>
- ReDoc 文档：<http://127.0.0.1:8000/redoc>
- OpenAPI 数据：<http://127.0.0.1:8000/openapi.json>

## 2. 创建 FastAPI 应用

```python
from fastapi import FastAPI

# 创建 FastAPI 应用对象，变量名 app 要与 uvicorn 命令中的 :app 对应
app = FastAPI()
```

`FastAPI()` 创建整个 Web 应用。所有接口都注册到这个 `app` 对象上。

一个文件中通常只创建一次 `app = FastAPI()`。如果后面再次赋值，会创建一个新应用，前面注册的配置或路由可能丢失。

## 3. 配置接口文档信息

```python
from fastapi import FastAPI

app = FastAPI(
    title="商品管理 API",  # 显示在接口文档顶部的标题
    description="这是一个用于学习 FastAPI 的商品接口示例",  # 项目说明
    version="1.0.0",  # 当前 API 版本
    contact={
        "name": "张三",  # 联系人姓名
        "email": "zhangsan@example.com",  # 联系邮箱
    },
)
```

这些配置主要用于 `/docs`、`/redoc` 和 `/openapi.json`，不会直接改变接口的业务逻辑。它们可以帮助前端、测试人员和其他开发者理解 API 的用途与版本。

如果不希望公开自动生成的文档，可以这样配置：

```python
from fastapi import FastAPI

# 关闭 Swagger 和 ReDoc 文档页面
app = FastAPI(docs_url=None, redoc_url=None)
```

## 4. 创建 GET 路由

```python
@app.get("/")  # 接收访问根路径 / 的 GET 请求
async def root():
    # Python 字典会自动转换成 JSON 响应
    return {"message": "Hello World"}
```

访问 <http://127.0.0.1:8000/> 后会得到：

```json
{
  "message": "Hello World"
}
```

`@app.get()` 是路由装饰器，用于指定请求方法和请求路径。浏览器地址栏默认发送的就是 GET 请求。

## 5. 使用路径参数

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # item_id 来自 URL，并且会被 FastAPI 校验为整数
    return {"item_id": item_id, "name": "苹果"}
```

请求地址：

```text
http://127.0.0.1:8000/items/5
```

响应结果：

```json
{
  "item_id": 5,
  "name": "苹果"
}
```

路径中的 `{item_id}` 必须与函数参数 `item_id` 同名。`item_id: int` 表示只接受能够转换为整数的值；如果传入字母，FastAPI 会自动返回参数校验错误。

## 6. 使用查询参数

查询参数位于 URL 中的 `?` 后面，例如 `?q=苹果`。

```python
@app.get("/search/")
async def search_item(q: str | None = None):
    # q 是可选查询参数，不传时值为 None
    return {"keyword": q}
```

请求示例：

```text
http://127.0.0.1:8000/search/?q=苹果
```

查询参数适合搜索关键词、分页页码、排序方式等简单数据。

## 7. 使用 Pydantic 定义请求体

POST 和 PUT 请求通常需要发送一组 JSON 数据。FastAPI 使用 Pydantic 模型描述和校验这些数据。

```python
from pydantic import BaseModel


class Item(BaseModel):
    name: str  # 必填字段：商品名称必须是字符串
    description: str | None = None  # 可选字段：默认值为 None
    price: float  # 必填字段：商品价格必须是数字
    tax: float | None = None  # 可选字段：商品税费
```

字段没有默认值时必须传递；字段类型包含 `None` 并且默认值为 `None` 时可以不传。

符合该模型的 JSON 示例：

```json
{
  "name": "苹果",
  "description": "红富士苹果",
  "price": 9.9,
  "tax": 0.5
}
```

## 8. 创建 POST 路由

```python
@app.post("/items/")
async def create_item(item: Item):
    # item 是经过 Item 模型校验后的请求体数据
    return item
```

POST 请求用于创建数据。不能直接在浏览器地址栏中测试，因为地址栏发送的是 GET 请求。

最方便的测试方式是访问 <http://127.0.0.1:8000/docs>：

1. 展开 `POST /items/`。
2. 点击 `Try it out`。
3. 修改请求体中的 JSON。
4. 点击 `Execute` 发送请求。

也可以在 PowerShell 中测试：

```powershell
$body = @{
    name = "苹果"            # 商品名称
    description = "红富士"  # 商品描述
    price = 9.9              # 商品价格
    tax = 0.5                # 税费
} | ConvertTo-Json

# 发送 POST 请求，ContentType 表示请求体使用 JSON 格式
Invoke-RestMethod `
    -Uri "http://127.0.0.1:8000/items/" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

## 9. 创建 PUT 路由

```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # item_id 来自 URL 路径，item 来自 JSON 请求体
    return {"item_id": item_id, "item": item}
```

PUT 请求通常用于更新已有数据。这个接口同时接收两种参数：

- `item_id`：路径参数，例如 `/items/5` 中的 `5`。
- `item`：请求体参数，也就是发送的 JSON 商品数据。

## 10. 设置路由文档信息

```python
@app.get(
    "/items/{item_id}",
    summary="获取商品信息",  # 文档中的接口简短标题
    description="根据商品 ID 查询商品详情",  # 接口详细说明
    tags=["商品管理"],  # 在接口文档中把接口放入指定分组
)
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "苹果"}
```

这些参数让自动生成的接口文档更清楚：

- `summary`：简短说明接口做什么。
- `description`：详细描述接口用途。
- `tags`：按照业务模块给接口分组。

## 11. 使用 tags 对接口分组

```python
@app.get("/users/", tags=["用户管理"])
async def read_users():
    # 返回用户列表
    return [
        {"username": "张杰"},
        {"username": "李娜"},
    ]


@app.get("/items-list/", tags=["商品管理"])
async def read_items():
    # 返回商品列表
    return [
        {"name": "Foo"},
        {"name": "Bar"},
    ]
```

设置 `tags` 后，Swagger 文档会将接口展示在“用户管理”和“商品管理”等分组中。它只影响文档展示，不会改变请求路径和业务结果。

## 12. GET、POST 和 PUT 的区别

| 请求方法 | 常见用途 | 数据通常放在哪里 | 能否直接用浏览器地址栏测试 |
| --- | --- | --- | --- |
| GET | 查询数据 | 路径参数、查询参数 | 可以 |
| POST | 创建数据 | JSON 请求体 | 不可以 |
| PUT | 更新数据 | 路径参数、JSON 请求体 | 不可以 |

同一个路径可以定义不同的请求方法。例如，`GET /items/` 和 `POST /items/` 是两个不同的接口。

## 13. 常见错误

### 13.1 `404 Not Found`

响应内容：

```json
{"detail": "Not Found"}
```

表示请求路径没有匹配到任何路由。常见原因：

- URL 路径写错。
- 路由装饰器中的路径写错。
- 请求末尾 `/` 与定义不一致。
- Uvicorn 启动了另一个 Python 文件中的应用。

例如路径参数必须完整写成：

```python
@app.get("/items/{item_id}")  # 左右花括号必须完整
```

### 13.2 `405 Method Not Allowed`

响应内容：

```json
{"detail": "Method Not Allowed"}
```

表示路径存在，但请求方法不匹配。例如只定义了：

```python
@app.post("/items/")
async def create_item(item: Item):
    return item
```

此时在浏览器地址栏访问 `/items/` 会发送 GET 请求，而接口只允许 POST，所以返回 405。应使用 `/docs`、Postman、curl 或 PowerShell 发送 POST 请求。

### 13.3 无法导入模块

如果出现 `Could not import module`，通常是启动目录和模块路径不对应。

在 `FastAPI_Study` 目录中执行：

```powershell
uvicorn py_FastAPI_01:app --reload
```

在项目根目录中执行：

```powershell
uvicorn FastAPI_Study.py_FastAPI_01:app --reload
```

## 14. 当前完整示例

```python
from fastapi import FastAPI
from pydantic import BaseModel


# 创建应用并配置自动接口文档信息
app = FastAPI(
    title="商品管理 API",
    description="这是一个用于学习 FastAPI 的商品接口示例",
    version="1.0.0",
    contact={
        "name": "张三",
        "email": "zhangsan@example.com",
    },
)


# 定义商品请求体的数据结构和校验规则
class Item(BaseModel):
    name: str  # 商品名称，必填
    description: str | None = None  # 商品描述，可选
    price: float  # 商品价格，必填
    tax: float | None = None  # 商品税费，可选


@app.get("/", tags=["基础接口"])
async def root():
    # 返回欢迎信息
    return {"message": "Hello World"}


@app.get(
    "/items/{item_id}",
    summary="获取商品信息",
    description="根据商品 ID 查询商品详情",
    tags=["商品管理"],
)
async def read_item(item_id: int):
    # item_id 由 URL 路径传入
    return {"item_id": item_id, "name": "苹果"}


@app.post("/items/", tags=["商品管理"])
async def create_item(item: Item):
    # item 由 JSON 请求体传入，并经过 Item 模型校验
    return item


@app.put("/items/{item_id}", tags=["商品管理"])
async def update_item(item_id: int, item: Item):
    # 同时返回路径中的商品 ID 和请求体中的商品数据
    return {"item_id": item_id, "item": item}


@app.get("/users/", tags=["用户管理"])
async def read_users():
    # 返回模拟的用户列表
    return [
        {"username": "张杰"},
        {"username": "李娜"},
    ]
```

## 15. 本阶段已经学到的内容

- 使用 Uvicorn 启动 FastAPI 项目。
- 创建 FastAPI 应用并配置文档信息。
- 使用 `/docs` 和 `/redoc` 查看、测试接口。
- 使用 GET、POST、PUT 创建不同类型的接口。
- 使用路径参数和查询参数传值。
- 使用 Pydantic 模型接收并校验 JSON 请求体。
- 使用 `tags`、`summary` 和 `description` 整理接口文档。
- 理解并排查 404、405 和模块导入错误。

