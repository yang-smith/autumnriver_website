+++
title = "FastAPI教程：20个核心概念从入门到happy使用"
description = "FastAPI教程：20个核心概念从入门到happy使用"
date = 2025-03-06
draft = false

[taxonomies]
tags = ["FastAPI"]

[extra]
toc = true

+++

<!-- toc -->


FastAPI 是一个现代、高性能的 Python Web 框架。它的与众不同之处在于：原生支持异步处理提升并发性能；利用 Python 类型提示实现自动数据校验；自动生成 API 文档；以及接近 Go 语言级别的高吞吐量。来看看它的核心概念。

## 一、基础结构

### 1. 路由（Routing）
就是定义接口的入口。通过装饰器告诉 FastAPI 这个函数对应哪个 URL。
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # 装饰器指定这是个 GET 请求，路径是根目录
def read_root():
    return {"message": "Hello World"}
```

### 2. 子应用挂载（Sub-Applications）
让你把大应用拆成小模块，各自独立又能组合使用。
```python
from fastapi import FastAPI

app = FastAPI()
users_app = FastAPI()

@users_app.get("/")
def read_users():
    return {"users": ["John", "Jane"]}

app.mount("/users", users_app)  # 访问 /users/ 时会转到 users_app 处理
```

## 二、请求处理

### 3. 路径参数（Path Parameters）
从 URL 中提取变量，比如获取用户 ID。
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):  # 自动转换为整数
    return {"item_id": item_id}
```

### 4. 查询参数（Query Parameters）
处理 URL 中 ? 后面的参数，常用于过滤和分页。
```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, q: str = None):
    # 例如：/items/?skip=20&limit=30&q=搜索词
    return {"skip": skip, "limit": limit, "q": q}
```

### 5. 请求体（Request Body）
处理客户端发来的 JSON 数据。
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None  # 可选字段

@app.post("/items/")
def create_item(item: Item):  # 自动解析 JSON 到对象
    return {"item_name": item.name, "price": item.price}
```

### 6. 表单数据（Form Data）
处理普通的表单提交，比如登录表单。
```python
from fastapi import Form

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    # Form(...) 表示必填字段
    return {"username": username}
```

### 7. 文件上传（File Uploads）
接收上传的文件。
```python
from fastapi import File, UploadFile

@app.post("/files/")
async def create_file(file: bytes = File(...)):  # 适合小文件
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):  # 适合大文件，有更多操作
    return {"filename": file.filename}
```

## 三、数据处理与验证

### 8. Pydantic 模型
用来定义数据结构和验证规则，告别手动检查数据。
```python
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    email: str
    age: int = Field(..., gt=0, lt=120)  # 验证年龄在 1-119 之间
    
@app.post("/users/")
def create_user(user: User):  # 数据已经过验证
    return user
```

### 9. 数据验证（Data Validation）
自动检查数据是否合法，错误时返回清晰的提示。
```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr  # 自动验证邮箱格式
    password: str

@app.post("/users/")
def create_user(user: UserCreate):
    # 数据已经过验证，可以放心使用
    return {"username": user.username, "email": user.email}
```

### 10. 状态码（Status Codes）
控制 API 返回的 HTTP 状态码。
```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)  # 201 表示创建成功
def create_item(item: Item):
    return item
```

## 四、安全与中间件

### 11. 安全和认证（Security & Authentication）
处理用户登录和权限验证。
```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # 获取当前登录用户信息
    return {"token": token, "user_id": "current_user"}
```

### 12. 依赖注入系统（Dependency Injection）
解决组件之间的依赖关系，让代码更整洁。
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db  # 提供数据库会话
    finally:
        db.close()  # 确保会话关闭

@app.get("/users/{user_id}")
def read_user(user_id: int, db = Depends(get_db)):
    # 自动获取数据库连接
    user = db.query(User).filter(User.id == user_id).first()
    return user
```

### 13. 中间件（Middleware）
在请求处理前后执行代码，比如记录请求时间。
```python
import time

@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)  # 添加处理时间到响应头
    return response
```

### 14. CORS（跨域资源共享）
允许其他网站调用你的 API。
```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的请求头
)
```

## 五、文档与测试

### 15. OpenAPI 文档
自动为你的 API 生成文档，告诉别人怎么用。
```python
app = FastAPI(
    title="我的 API",
    description="这是一个示例 API",
    version="0.1.0",
)

@app.get("/items/", tags=["items"])
def read_items():
    """
    获取所有商品
    
    返回所有可用商品的列表
    """
    return [{"name": "商品1"}, {"name": "商品2"}]
```

### 16. Swagger UI
提供可交互的 API 文档界面，直接在浏览器测试 API。
```python
# 默认访问地址：/docs
# 自定义配置:
app = FastAPI(docs_url="/api-docs", redoc_url=None)
```

### 17. ReDoc
另一种更整洁的 API 文档界面。
```python
# 默认访问地址：/redoc
# 自定义配置:
app = FastAPI(redoc_url="/api-docs", docs_url=None)
```

## 六、高级功能

### 18. 异步支持（Async Support）
用 Python 异步特性提升性能，处理更多并发请求。
```python
import asyncio

@app.get("/async-items/")
async def read_async_items():
    # 模拟异步数据库操作
    await asyncio.sleep(1)
    return [{"name": "异步商品1"}, {"name": "异步商品2"}]
```

### 19. 背景任务（Background Tasks）
响应完请求后在后台继续执行任务，比如发邮件。
```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # 先返回响应，然后在后台记录日志
    background_tasks.add_task(write_log, f"给 {email} 发送了通知")
    return {"message": "通知已发送"}
```

### 20. WebSockets 支持
实现实时双向通信，比如聊天应用或实时数据更新。

WebSocket 简单理解：
- HTTP 像发短信：发一条请求，等一个回复，每次都要重新开始
- WebSocket 像打电话：建立连接后，双方可以随时互相说话，一直保持连接

```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # 接受连接
    while True:
        data = await websocket.receive_text()  # 接收消息
        await websocket.send_text(f"收到消息: {data}")  # 发送消息
```

以上就是 FastAPI 的核心概念，掌握这些基本能满足大部分 API 开发需求了。FastAPI 的强大之处在于它把复杂的事情变简单，让你专注于业务逻辑而不是框架本身。
