+++
title = "Python异步编程指南：asyncio从入门到精通(Python 3.10+)"
description = "Python异步编程重要概念"
date = 2025-03-06
draft = false

[taxonomies]
tags = ["Python"]

[extra]
toc = true

+++



## 一、基础概念层

### 1. 同步与异步编程
**解释**：同步编程是按顺序执行的代码，而异步编程允许程序在等待某个操作完成时继续执行其他操作。
**示例**：
```python
# 同步代码
def sync_function():
    result = expensive_operation()  # 程序在这里阻塞等待
    return result

# 异步代码
async def async_function():
    result = await expensive_operation()  # 等待操作完成时可以执行其他任务
    return result
```

### 2. 协程 (Coroutine)
**解释**：协程是可以在执行过程中暂停和恢复的函数，是Python异步编程的基本单位。
**示例**：
```python
async def simple_coroutine():
    print("开始执行")
    await asyncio.sleep(1)  # 暂停协程执行
    print("恢复执行")
```

**连接**：协程是实现异步编程的基础机制，通过`async/await`语法定义和使用。

### 3. async/await 语法
**解释**：Python 3.5+引入的语法，用于定义和调用协程。`async`定义协程函数，`await`用于等待协程执行结果。
**示例**：
```python
async def fetch_data():
    print("开始获取数据")
    await asyncio.sleep(2)  # 模拟I/O操作
    print("数据获取完成")
    return {"data": "value"}

async def main():
    result = await fetch_data()  # 等待fetch_data协程执行完成
    print(result)
```

**连接**：是使用协程的核心语法，与协程和事件循环紧密相关。

### 4. 事件循环 (Event Loop)
**解释**：事件循环是异步编程的核心，负责协调和调度协程的执行。每个线程只能有一个活动事件循环。

**工作原理**：
- 事件循环维护一个就绪任务队列和一个等待中的任务注册表
- 当协程通过`await`暂停执行时，控制权返回给事件循环
- 事件循环继续执行其他就绪任务，并监控等待中的操作
- 当等待的操作完成后，相关协程被放回就绪队列

**示例**：
```python
import asyncio

async def hello():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("Hello again!")

# Python 3.10+推荐方法
asyncio.run(hello())  # 创建新事件循环，运行协程，完成后关闭循环

# 手动管理事件循环（不推荐但有助于理解）
async def manual_loop_example():
    loop = asyncio.get_running_loop()  # 在 3.10+ 中获取当前运行的事件循环
    print(f"当前事件循环: {loop}")
    print(f"事件循环运行状态: {loop.is_running()}")
    
    # 创建future对象
    future = loop.create_future()
    
    # 安排一个回调在1秒后设置future结果
    loop.call_later(1, lambda: future.set_result("完成"))
    
    # 等待future完成
    result = await future
    print(f"Future结果: {result}")

# asyncio.run(manual_loop_example())
```

**高级特性**：
- Python 3.10+支持更好的任务取消和超时控制
- 支持事件循环策略（event loop policy）定制
- 可与uvloop等第三方实现替换，提升性能
- 调试模式：`asyncio.run(coro, debug=True)`可启用事件循环调试

**连接**：事件循环是运行所有异步代码的环境，与协程和任务密切相关。

### 5. 阻塞与非阻塞I/O
**解释**：阻塞I/O会使程序等待操作完成，而非阻塞I/O允许程序在等待期间执行其他任务。
**示例**：
```python
# 阻塞I/O
import time
def blocking_io():
    time.sleep(1)  # 阻塞整个程序

# 非阻塞I/O
async def non_blocking_io():
    await asyncio.sleep(1)  # 不阻塞事件循环
```

**连接**：是理解异步编程价值的基础概念，与协程和事件循环共同工作。

## 二、asyncio基础层

### 6. asyncio.run()
**解释**：Python 3.7+引入的高级API，用于运行协程并管理事件循环。在Python 3.10+中得到进一步优化，提供更完善的错误处理。
**示例**：
```python
import asyncio

async def main():
    print("开始执行main")
    await asyncio.sleep(1)
    print("main执行完成")
    return "结果"

# Python 3.10+支持debug模式和任务名称
result = asyncio.run(main(), debug=True)  # 创建新事件循环，运行协程，完成后关闭循环
print(result)
```

**连接**：是启动异步程序的推荐方式，内部管理事件循环。

### 7. 任务 (Task)
**解释**：任务是协程的高级封装，代表事件循环正在跟踪的一个操作。Python 3.10+提供了更完善的任务命名和任务组功能。
**示例**：
```python
import asyncio

async def background_task():
    print("后台任务开始")
    await asyncio.sleep(2)
    print("后台任务完成")
    return "后台任务结果"

async def main():
    # 创建任务并命名（Python 3.8+）
    task = asyncio.create_task(background_task(), name="背景任务")
    
    # 获取任务名称（Python 3.8+）
    print(f"任务名称: {task.get_name()}")
    
    # 做其他事情
    print("主函数继续执行")
    await asyncio.sleep(1)
    
    # 等待任务完成
    result = await task
    print(f"获取到结果: {result}")

asyncio.run(main())
```

**连接**：任务是协程的包装器，允许并发执行多个协程。

### 8. asyncio.gather()
**解释**：并发运行多个协程并等待所有协程完成，返回所有结果的列表。Python 3.10+提供更好的错误处理。
**示例**：
```python
import asyncio

async def fetch(id):
    await asyncio.sleep(id)
    return f"结果 {id}"

async def main():
    # 并发执行三个协程
    results = await asyncio.gather(
        fetch(1),
        fetch(2),
        fetch(3),
        return_exceptions=True  # 错误会被作为结果返回而非引发异常
    )
    print(results)  # ['结果 1', '结果 2', '结果 3']

asyncio.run(main())
```

**连接**：与任务相关，是并发执行多个协程的主要方法。

### 9. asyncio.wait_for()
**解释**：给协程设置超时时间，超时后抛出`asyncio.TimeoutError`异常。
**示例**：
```python
import asyncio

async def long_operation():
    await asyncio.sleep(5)
    return "完成"

async def main():
    try:
        # 等待协程，但最多等待2秒
        result = await asyncio.wait_for(long_operation(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("操作超时")

asyncio.run(main())  # 输出: 操作超时
```

**连接**：超时控制机制，确保异步操作不会无限等待。

### 10. asyncio.sleep()
**解释**：异步等待指定的秒数，不会阻塞事件循环。Python 3.10+版本性能有所优化。
**示例**：
```python
import asyncio

async def main():
    print("开始")
    await asyncio.sleep(1)  # 非阻塞休眠
    print("1秒后")

asyncio.run(main())
```

**连接**：是模拟I/O操作和创建延迟的基础工具。

## 三、并发原语层

### 11. Future对象
**解释**：表示尚未完成的计算结果，是Task的底层实现基础。
**示例**：
```python
import asyncio

async def set_future_result(future):
    await asyncio.sleep(1)
    future.set_result("Future完成了")

async def main():
    # 创建Future对象
    future = asyncio.Future()
    
    # 创建任务设置future结果
    asyncio.create_task(set_future_result(future))
    
    # 等待future完成
    result = await future
    print(result)

asyncio.run(main())
```

**连接**：是Task的底层实现，代表异步操作的最终结果。

### 12. asyncio.Lock()
**解释**：异步锁，用于保护共享资源，防止多个协程同时访问。
**示例**：
```python
import asyncio

async def protected_resource(lock, name):
    async with lock:  # 获取锁
        print(f"{name} 获得了锁")
        await asyncio.sleep(1)  # 模拟工作
        print(f"{name} 释放了锁")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(
        protected_resource(lock, "协程1"),
        protected_resource(lock, "协程2"),
        protected_resource(lock, "协程3")
    )

asyncio.run(main())
```

**连接**：是并发控制的基本工具，确保资源访问的串行化。

### 13. asyncio.Semaphore()
**解释**：信号量，限制同时运行的协程数量。
**示例**：
```python
import asyncio

async def worker(semaphore, id):
    async with semaphore:
        print(f"工作者 {id} 开始")
        await asyncio.sleep(1)
        print(f"工作者 {id} 完成")

async def main():
    # 限制最多2个协程同时执行
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(worker(semaphore, i) for i in range(5)))

asyncio.run(main())
```

**连接**：高级并发控制工具，与Lock相关但更加灵活。

### 14. asyncio.Event()
**解释**：事件对象，用于在协程之间发送通知。
**示例**：
```python
import asyncio

async def waiter(event):
    print("等待事件...")
    await event.wait()  # 等待事件被设置
    print("事件已被设置，继续执行")

async def setter(event):
    print("等待3秒后设置事件")
    await asyncio.sleep(3)
    event.set()  # 设置事件，通知所有等待者

async def main():
    event = asyncio.Event()
    # 创建一个等待者和一个设置者
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())
```

**连接**：是协程间通信和同步的机制。

### 15. asyncio.Queue()
**解释**：异步队列，用于在不同协程之间安全地传递数据。
**示例**：
```python
import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(f"项目 {i}")
        print(f"生产了项目 {i}")

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"消费了 {item}")
        queue.task_done()
        await asyncio.sleep(2)

async def main():
    queue = asyncio.Queue()
    # 创建生产者和消费者任务
    producers = asyncio.create_task(producer(queue))
    consumers = asyncio.create_task(consumer(queue))
    
    # 等待生产者完成
    await producers
    
    # 等待队列处理完成
    await queue.join()
    
    # 取消消费者
    consumers.cancel()

asyncio.run(main())
```

**连接**：实现生产者-消费者模式的关键工具。

## 四、高级概念与模式层

### 16. 上下文管理器与async with
**解释**：用于资源管理的异步上下文管理器，使用`async with`语法。
**示例**：
```python
import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("进入上下文")
        await asyncio.sleep(1)
        return "上下文资源"
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
        await asyncio.sleep(1)

async def main():
    async with AsyncContextManager() as resource:
        print(f"使用资源: {resource}")

asyncio.run(main())
```

**连接**：是异步资源管理的标准方法，常用于锁和其他需要清理的资源。

### 17. 异步迭代器与async for
**解释**：可以在`async for`循环中使用的对象，允许异步迭代。
**示例**：
```python
import asyncio

class AsyncIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        
    def __aiter__(self):
        return self
        
    async def __anext__(self):
        if self.counter < self.limit:
            self.counter += 1
            await asyncio.sleep(0.5)
            return self.counter
        else:
            raise StopAsyncIteration

async def main():
    async for number in AsyncIterator(5):
        print(number)

asyncio.run(main())
```

**连接**：与异步生成器相关，用于异步数据流处理。

### 18. 异步生成器
**解释**：使用`async def`和`yield`定义的函数，可以异步生成值序列。在Python 3.10+中，异步生成器性能得到优化，提供更强大的异步数据流处理能力。

**工作原理**：
- 异步生成器结合了协程和生成器的特性
- 当执行到`yield`语句时，它会产生一个值并暂停执行
- 与普通生成器不同，异步生成器可以在`yield`前使用`await`表达式
- 调用者使用`async for`迭代或手动使用`asend()`, `anext()`, `athrow()`方法

**高级用法**：
```python
import asyncio

# 定义异步生成器
async def async_generator(start, end):
    for i in range(start, end):
        # 可以在yield前使用await
        await asyncio.sleep(0.1)
        yield i
        print(f"继续生成器执行，刚生成了 {i}")

async def main():
    # 使用async for迭代
    print("使用async for循环:")
    async for i in async_generator(1, 4):
        print(f"收到值: {i}")
    
    print("\n手动迭代:")
    # 手动迭代异步生成器
    gen = async_generator(5, 7)
    
    # 获取第一个值
    item = await gen.__anext__()
    print(f"手动迭代第一个值: {item}")
    
    # 发送值给生成器(类似yield from)
    try:
        item = await gen.asend(None)
        print(f"使用asend获取的下一个值: {item}")
    except StopAsyncIteration:
        print("生成器已结束")

asyncio.run(main())
```

**异步迭代协议**：
- `__aiter__()`: 返回异步迭代器
- `__anext__()`: 返回一个awaitable，获取下一个值或引发StopAsyncIteration

**与普通生成器的区别**：
1. 异步生成器用`async def`定义，普通生成器用`def`定义
2. 异步生成器可以在内部使用`await`，普通生成器不能
3. 异步生成器用`async for`迭代，普通生成器用`for`迭代
4. 异步生成器支持`asend()`、`athrow()`和`aclose()`方法

**连接**：是异步迭代器的一种便捷实现方式，提供流式数据处理能力。

### 19. 取消与超时处理
**解释**：控制和取消长时间运行的异步操作。Python 3.10+提供了更完善的取消和超时机制。
**示例**：
```python
import asyncio

async def cancelable_operation():
    try:
        print("开始长时间操作")
        await asyncio.sleep(10)
        print("操作完成")  # 如果被取消，不会执行到这里
    except asyncio.CancelledError:
        print("操作被取消")
        raise  # 重新抛出异常

async def main():
    # 创建任务
    task = asyncio.create_task(cancelable_operation())
    
    # 等待1秒
    await asyncio.sleep(1)
    
    # 取消任务
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("主函数捕获到取消异常")

asyncio.run(main())
```

**连接**：与任务管理和错误处理紧密相关。

### 20. 异步上下文变量 (contextvars)
**解释**：在异步代码中安全地存储和访问上下文相关的状态。
**示例**：
```python
import asyncio
import contextvars

# 创建上下文变量
request_id = contextvars.ContextVar('request_id', default=None)

async def process_request():
    # 获取当前请求ID
    current_id = request_id.get()
    print(f"处理请求 {current_id}")

async def handle_request(id):
    # 设置此协程上下文中的请求ID
    token = request_id.set(id)
    try:
        await process_request()
    finally:
        # 恢复之前的值
        request_id.reset(token)

async def main():
    # 并发处理多个请求
    await asyncio.gather(
        handle_request("req-1"),
        handle_request("req-2"),
        handle_request("req-3")
    )

asyncio.run(main())
```

**连接**：解决异步程序中的上下文传递问题，类似于线程本地存储。

## 五、实际应用层

### 21. 异步网络I/O
**解释**：使用asyncio进行网络操作，如HTTP请求和套接字通信。

**优劣对比**：

| 库 | 优点 | 缺点 | 适用场景 |
|---|---|---|---|
| aiohttp | 成熟稳定，功能完整 | API较复杂 | 复杂网络应用 |
| httpx | 现代API，支持同步/异步 | 相对较新 | 简单HTTP请求 |
| requests-async | 类似requests的熟悉API | 不再积极维护 | 简单迁移需求 |

**示例** (使用最新的httpx):
```python
import asyncio
import httpx

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://github.com"
    ]
    
    # 并发获取多个URL
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    for url, html in zip(urls, results):
        print(f"{url}: 获取了 {len(html)} 字节")

# asyncio.run(main())
```

**连接**：展示了异步编程在网络I/O中的实际应用。

### 22. 异步文件I/O
**解释**：使用`aiofiles`库进行异步文件操作。

**优劣对比**：

| 方案 | 优点 | 缺点 | 适用场景 |
|---|---|---|---|
| aiofiles | 完全异步API | 需要额外依赖 | 需要非阻塞文件I/O |
| anyio | 统一同步/异步接口 | 抽象层可能有开销 | 跨异步框架应用 |
| 线程池+内置open | 无需额外依赖 | 使用复杂 | 简单文件操作 |

**示例**：
```python
import asyncio
import aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, mode='r') as f:
        contents = await f.read()
        return contents

async def write_file(filename, content):
    async with aiofiles.open(filename, mode='w') as f:
        await f.write(content)

async def main():
    # 写入文件
    await write_file('test.txt', '这是异步写入的内容')
    
    # 读取文件
    content = await read_file('test.txt')
    print(f"读取到内容: {content}")

# asyncio.run(main())
```

**连接**：展示了异步I/O在文件操作中的应用。

### 23. 异步数据库操作
**解释**：使用异步数据库驱动进行数据库操作。

**优劣对比**：

| 驱动 | 支持数据库 | 优点 | 缺点 |
|---|---|---|---|
| asyncpg | PostgreSQL | 高性能，原生异步 | 仅支持PostgreSQL |
| aiomysql | MySQL | MySQL官方支持 | 性能一般 |
| aiosqlite | SQLite | 轻量级，无需服务器 | 不适合高并发 |
| SQLAlchemy 2.0 | 多种数据库 | ORM支持，统一接口 | 学习曲线高 |

**示例** (使用现代SQLAlchemy 2.0异步API):
```python
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, select

# 定义模型
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

async def example_db_operations():
    # 创建异步引擎
    engine = create_async_engine(
        "sqlite+aiosqlite:///test.db", 
        echo=True
    )
    
    # 创建表
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # 创建会话
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    # 插入数据
    async with async_session() as session:
        user = User(name="John Doe", email="john@example.com")
        session.add(user)
        await session.commit()
    
    # 查询数据
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        for user in users:
            print(f"User: {user.name}, Email: {user.email}")
    
    # 关闭引擎
    await engine.dispose()

# asyncio.run(example_db_operations())
```

**连接**：展示了异步编程在数据库操作中的应用。

### 24. 异步Web服务器
**解释**：使用现代异步Web框架创建高性能Web服务。

**框架优劣对比**：

| 框架 | 优点 | 缺点 | 特色 |
|---|---|---|---|
| FastAPI | 现代、高性能、自动文档 | 依赖Starlette和Pydantic | 类型提示、OpenAPI集成 |
| aiohttp | 成熟稳定，客户端/服务器 | API较复杂 | 完整的HTTP库 |
| Sanic | 超高性能 | 生态相对较小 | 专注速度 |
| Starlette | 轻量级，高性能 | 功能较少 | ASGI标准实现 |
| Quart | Flask兼容API | 生态较小 | Flask项目迁移友好 |

**示例** (使用FastAPI):
```python
from fastapi import FastAPI, BackgroundTasks
import asyncio
import uvicorn

app = FastAPI()

# 后台任务
async def process_data(data: str):
    await asyncio.sleep(2)  # 模拟长时间处理
    print(f"处理完成: {data}")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: dict, background_tasks: BackgroundTasks):
    # 添加后台任务异步处理
    background_tasks.add_task(process_data, item.get("data", ""))
    return {"status": "accepted", "message": "处理中"}

# 使用uvicorn运行（命令行）: uvicorn example:app --reload
# 代码中运行:
# if __name__ == "__main__":
#     uvicorn.run("example:app", host="127.0.0.1", port=8000, reload=True)
```

**连接**：展示了如何构建异步Web应用程序。

### 25. 异步与多进程结合
**解释**：将CPU密集型任务放在单独的进程中执行，同时使用asyncio处理I/O密集型任务。

**不同并发方案对比**：

| 方案 | 适用场景 | 优点 | 缺点 |
|---|---|---|---|
| 纯asyncio | I/O密集型 | 低开销，高并发 | 不适合CPU密集型 |
| 多线程+asyncio | 混合I/O密集型 | 较简单实现 | 受GIL限制 |
| 多进程+asyncio | 混合CPU密集型 | 最大利用多核CPU | 进程间通信复杂 |
| uvloop+asyncio | I/O密集型 | 接近C性能 | 特定平台限制 |

**示例**：
```python
import asyncio
import concurrent.futures
import time
import math

# CPU密集型任务
def cpu_bound_task(n):
    print(f"计算第 {n} 个素数")
    start = time.time()
    # 计算第n个素数
    count = 0
    num = 2
    while count < n:
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            count += 1
        num += 1
    result = num - 1
    print(f"第 {n} 个素数是 {result}，耗时 {time.time() - start:.2f} 秒")
    return result

# I/O密集型任务
async def io_bound_task(n):
    print(f"I/O任务 {n} 开始")
    await asyncio.sleep(1)  # 模拟I/O操作
    print(f"I/O任务 {n} 完成")
    return f"I/O结果 {n}"

async def main():
    # 创建进程池
    with concurrent.futures.ProcessPoolExecutor() as pool:
        # 在进程池中执行CPU密集型任务
        loop = asyncio.get_running_loop()
        cpu_tasks = [
            loop.run_in_executor(pool, cpu_bound_task, i*1000)
            for i in range(1, 5)
        ]
        
        # 同时处理I/O密集型任务
        io_tasks = [io_bound_task(i) for i in range(1, 5)]
        
        # 并发执行所有任务
        all_results = await asyncio.gather(
            *cpu_tasks,
            *io_tasks
        )
        
        print(f"所有结果: {all_results}")

# asyncio.run(main())
```

**前沿优化** (Python 3.11+):
```python
import asyncio
import multiprocessing
from multiprocessing import shared_memory
import numpy as np

# 使用共享内存进行高效进程间通信
def process_data_in_process(shm_name, shape, dtype, start_idx, end_idx):
    # 连接到共享内存
    shm = shared_memory.SharedMemory(name=shm_name)
    # 创建NumPy数组视图
    data = np.ndarray(shape, dtype=dtype, buffer=shm.buf)
    
    # 处理数据
    for i in range(start_idx, end_idx):
        # 进行CPU密集型计算
        data[i] = data[i] ** 2
    
    # 关闭共享内存
    shm.close()
    return start_idx, end_idx

async def main():
    # 创建示例数据
    data = np.ones(1000000, dtype=np.float64)
    
    # 创建共享内存
    shm = shared_memory.SharedMemory(create=True, size=data.nbytes)
    shared_data = np.ndarray(data.shape, dtype=data.dtype, buffer=shm.buf)
    shared_data[:] = data[:]  # 复制数据到共享内存
    
    # 创建进程池
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 划分工作
        chunk_size = len(data) // multiprocessing.cpu_count()
        futures = []
        
        loop = asyncio.get_running_loop()
        
        # 提交任务到进程池
        for i in range(multiprocessing.cpu_count()):
            start = i * chunk_size
            end = start + chunk_size if i < multiprocessing.cpu_count() - 1 else len(data)
            
            # 异步提交到进程池
            future = loop.run_in_executor(
                executor, 
                process_data_in_process,
                shm.name, data.shape, data.dtype, start, end
            )
            futures.append(future)
        
        # 等待所有进程完成
        results = await asyncio.gather(*futures)
        print(f"处理完成: {results}")
        
        # 验证结果
        print(f"结果示例: {shared_data[:5]}")
    
    # 清理共享内存
    shm.close()
    shm.unlink()

# asyncio.run(main())
```

**连接**：展示了如何结合使用异步编程和多进程以获得最佳性能。



