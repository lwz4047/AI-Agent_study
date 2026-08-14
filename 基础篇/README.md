# Python 基础篇 — 学习笔记

## 目录

- [一、条件判断（py_if.py）](#一条件判断py_ifpy)
- [二、循环语句（py_for.py）](#二循环语句py_forpy)
- [三、函数（py_def.py）](#三函数py_defpy)
- [四、异常处理（py_try_cach.py）](#四异常处理py_try_cachpy)
- [五、学习要点速记](#五学习要点速记)

---

## 一、条件判断（py_if.py）

### 1. if 基本语法

- 条件成立时，执行**缩进**的代码块（可以一行或多行，多行缩进量必须一致）
- 与 `if` 同级的语句，不管条件是否成立都会执行

```python
num = 34
if num % 2 == 0:
    print("这个数为偶数")   # 条件成立才执行
print("判断结束")           # 同级代码，始终执行
```

### 2. 比较运算符

`==`、`!=`、`<`、`>`、`<=`、`>=`

> 注意：数字和字符串**不能**直接比较（如 `1 == "1"` 无意义）

### 3. 逻辑运算符

| 运算符 | 含义 | 示例场景 |
|--------|------|----------|
| `and` | 两边都成立才为 True | 登录验证：用户名和密码同时正确 |
| `or`  | 一边成立即为 True   | 判断水果：banana / apple / mango 任一匹配 |
| `not` | 取反               | 判断数字不为 0：`not num == 0` |

### 4. 隐式布尔值

非零数字（如 `10`）在条件中视为 `True`，可直接 `if 10:` 执行

### 5. 三元表达式

格式：`条件成立的结果 if 条件 else 条件不成立的结果`

```python
score = int(input("输入成绩："))
print("及格") if score >= 60 else print("不及格")
```

### 6. 多分支判断 if / elif / else

```python
score = int(input("输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 7. if 嵌套

外层判断是否为会员，内层根据金额分档打折：

```python
is_member = input("是否为会员：")
if is_member == "是":
    money = float(input("请输入金额："))
    print(f"会员打9.5折，应付金额：{money * 0.95}")
elif is_member == "否":
    money = float(input("请输入金额："))
    if money >= 100:
        print(f"满100打8.5折，应付金额：{money * 0.85}")
    elif money >= 50:
        print(f"满50打8折，应付金额：{money * 0.8}")
else:
    print("下次光临")
```

---

## 二、循环语句（py_for.py）

### 1. for 循环 + range()

- `range(n)` 生成 `0 ~ n-1` 的整数序列，循环执行 n 次
- `range(start, stop, step)` 支持起始值和步长，遵循**包前不包后**规则

```python
for i in range(5):
    print("你好")

for i in range(1, 10, 2):   # 输出 1 3 5 7 9
    print(i, end="\t")
```

### 2. while 循环

```python
# 计算 1~5 的和
i, total = 1, 0
while i <= 5:
    total += i
    i += 1
print(total)   # 15
```

### 3. 循环嵌套

```python
# 3排6列座位表
for i in range(1, 4):
    for j in range(1, 7):
        print(f"第{i}排 第{j}列", end="\t")
    print()
```

### 4. break 和 continue

- `break`：立即终止整个循环
- `continue`：跳过本次循环，继续下一次

```python
# 吃到第3个苹果就停止
for i in range(1, 6):
    if i == 3:
        print("吃饱了")
        break
    print(f"吃第{i}个苹果")
```

### 5. 循环 else

循环**未被 break 中断**时，else 块才会执行：

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("循环正常结束")   # 被 break 打断则不执行
```

### 6. 推导式

**列表推导式**：`[表达式 for 变量 in 列表 if 条件]`

```python
# 过滤长度 > 3 的名字并转大写
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_name = [name.upper() for name in names if len(name) > 3]

# 30以内被3整除的整数
num = [i for i in range(30) if i % 3 == 0]
```

**字典推导式**：`{key: value for item in collection}`

```python
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}   # {'Google': 6, ...}

squares = {x: x**2 for x in {2, 3, 4}}         # {2:4, 3:9, 4:16}
```

**集合推导式**：`{表达式 for item in Sequence}`

```python
number = {x**2 for x in {1, 2, 3}}             # {1, 4, 9}
```

**元组推导式**（生成器表达式）：

```python
a = (x for x in range(1, 11))
print(tuple(a))   # (1, 2, 3, ..., 10)
```

### 7. 迭代器

- 凡是可以用 `for` 遍历的对象都是**可迭代对象**
- 迭代器用 `iter()` 创建，用 `next()` 逐个访问，只能前进不能后退

```python
lst = [1, 2, 3, 4]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2

# 用 for 遍历迭代器
for i in iter(lst):
    print(i, end=",")
```

### 8. 斐波那契数列（综合练习）

```python
a, b = 0, 1
while b < 1000:
    a, b = b, a + b
    print(b)
```

---

## 三、函数（py_def.py）

### 1. 函数定义与调用

```python
def 函数名(参数列表):
    函数体
    return 返回值
```

```python
def hello():
    print("Hello World")

hello()   # 调用
```

### 2. 参数类型

| 参数类型 | 说明 | 示例 |
|----------|------|------|
| 必需参数 | 调用时数量、顺序必须与声明一致 | `def func(a, b)` |
| 关键字参数 | 调用时指定参数名，顺序可变 | `func(b=2, a=1)` |
| 默认参数 | 声明时赋默认值，未传则使用默认 | `def func(name, age=35)` |
| 不定长参数 `*args` | 收集多余位置参数，打包为**元组** | `def func(*args)` |
| 不定长参数 `**kwargs` | 收集关键字参数，打包为**字典** | `def func(**kwargs)` |

```python
# 默认参数
def printinfo(name, age=35):
    print("名字:", name, "年龄:", age)

printinfo(age=50, name="runoob")
printinfo(name="runoob")          # age 使用默认值 35
```

```python
# *args 不定长位置参数
def printinfo(arg1, *vartuple):
    print(arg1)
    print(vartuple)   # 以元组形式存储

printinfo(70, 60, 50)   # arg1=70, vartuple=(60,50)
```

```python
# **kwargs 不定长关键字参数
def printinfo(arg1, **vardict):
    print(arg1)
    print(vardict)   # 以字典形式存储

printinfo(1, a=2, b=3)   # arg1=1, vardict={'a':2,'b':3}
```

> `*` 单独出现时，其后的参数**必须以关键字形式**传参：
> ```python
> def f(a, b, *, c):
>     return a + b + c
> f(1, 2, c=3)   # c 必须用关键字传入
> ```

### 3. 返回值 return

- `return` 会终止函数执行并返回值
- 可同时返回多个值（以**元组**形式返回）

```python
def greet():
    return "Hello World", "你好"

# 接收方式1：一个变量接收元组
result = greet()          # ('Hello World', '你好')

# 接收方式2：解包
str1, str2 = greet()
```

### 4. 可变对象 vs 不可变对象传参

| 类型 | 包含 | 传参行为 |
|------|------|----------|
| 不可变 | `int` `str` `tuple` | 类似值传递，函数内修改不影响外部 |
| 可变   | `list` `dict`       | 类似引用传递，函数内修改影响外部 |

```python
def changeme(mylist):
    mylist.append([1, 2, 3, 4])   # 直接修改了原列表

mylist = [10, 20, 30]
changeme(mylist)
print(mylist)   # [10, 20, 30, [1, 2, 3, 4]]
```

### 5. 全局变量与 global

函数内若要修改全局变量，需用 `global` 声明：

```python
discount = 0.1

def dis_count():
    global discount
    discount = 0.5
    print("内部", discount)

dis_count()
print("外部", discount)   # 0.5，全局变量已被修改
```

### 6. Lambda 匿名函数

Lambda 是一种小型、匿名的内联函数，只能包含**一个表达式**，无需 `def` 定义。

语法格式：`lambda 参数列表: 表达式`

```python
# 无参数
f = lambda: "Hello World"
print(f())            # Hello World

# 单参数：加 10
add10 = lambda a: a + 10
print(add10(5))       # 15

# 多参数：两数相乘
mul = lambda a, b: a * b
print(mul(5, 6))      # 30
```

**结合内置高阶函数使用：**

| 函数 | 语法 | 作用 |
|------|------|------|
| `map()` | `map(func, iterable)` | 对每个元素应用函数，返回迭代器 |
| `filter()` | `filter(func, iterable)` | 保留函数返回 `True` 的元素 |
| `reduce()` | `reduce(func, iterable)` | 累积运算，最终合并为单值（需导入） |

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# map：每个元素平方
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
print(squared)        # [1, 4, 9, 16]

# filter：过滤偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)          # [2, 4, 6, 8]

# reduce：求乘积（需 from functools import reduce）
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)        # 120
```

### 7. 装饰器（Decorator）

装饰器是一种**在不修改原函数代码的前提下动态扩展函数功能**的高级特性。本质是一个函数：接收一个函数作为参数，返回增强版的新函数，通过 `@装饰器名` 语法糖应用到目标函数上。

**常见应用场景：** 日志记录、性能计时、权限控制、结果缓存

#### 基本结构

```python
def timer(func):              # 接收原函数
    def wrapper(*args, **kwargs):
        print("开始计时")
        result = func(*args, **kwargs)  # 执行原函数
        print("结束计时")
        return result
    return wrapper            # 返回包装后的新函数

def say_hello():
    print("Hello")

# @timer 等价于下面这行：
say_hello = timer(say_hello)
say_hello()
```

#### 语法糖 @

```python
@timer          # 等价于 say_hello = timer(say_hello)，在函数定义时立即替换
def say_hello():
    print("Hello")
```

#### 实战案例：计时装饰器

```python
import time, functools

def timer(func):
    @functools.wraps(func)    # 保留原函数名称和文档信息
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 [{func.__name__}] 耗时: {end - start:.4f} 秒")
        return result
    return wrapper

@timer
def get_data():
    time.sleep(2.9)
    return "爬到了 100 条数据"

print(get_data())  # 输出：函数 [get_data] 耗时: 2.9xxx 秒
```

#### 带参数的装饰器（三层嵌套）

当装饰器本身需要接收参数时，需要多套一层函数：

```python
def repeat(number):           # 最外层：接收装饰器参数
    def decorator(func):      # 中间层：接收原函数
        def wrapper(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(4)                    # 执行 4 次
def say_hello():
    print("Hello")

say_hello()   # 打印 4 次 Hello
```

> **执行顺序：** `@decorator` 作用于函数定义时，装饰器**立即执行一次**完成替换；之后每次调用函数名，实际执行的是 `wrapper`。

---

## 四、异常处理（py_try_cach.py）

### 1. try / except 基本结构

程序运行时可能产生异常，使用 `try/except` 可以捕获并处理错误，防止程序崩溃。

```python
try:
    num = int(input("请输入一个数字："))
    print(num)
except Exception:          # Exception 是所有非语法错误异常的父类
    print("输入错误！请输入一个正确的数字")
print("=========")         # 无论是否出现异常，都会执行
```

### 2. 捕获指定异常

捕获特定类型的异常，处理更精准：

```python
try:
    num = int(input("请输入一个数字："))
except ValueError:
    print("传入的值不对")   # 输入非数字时触发
```

### 3. 捕获多种异常（as e）

使用 `as e` 可以打印异常的具体描述信息：

```python
try:
    print(1 / 0)
    print("1" > 1)
except ValueError as e:
    print("传入的值不对", e)
except ZeroDivisionError as e:
    print("除数不能为 0", e)
except TypeError as e:
    print("类型错误", e)
```

### 4. else 与 finally

| 子句 | 触发时机 | 常用场景 |
|------|---------|----------|
| `else` | **没有异常**时执行 | 操作成功后的后续逻辑 |
| `finally` | **无论是否异常**都执行 | 资源释放、日志收尾 |

```python
try:
    num = int(input("请输入数字："))
except ValueError as e:
    print(e)
else:
    print(num, type(num))   # 输入正确时执行
finally:
    print("程序执行完毕")    # 始终执行，即使抛出异常
```

### 5. 常见内置异常类型

| 异常类型 | 触发场景 | 简单示例 |
|---------|---------|----------|
| `ValueError` | 类型转换失败 | `int("abc")` |
| `ZeroDivisionError` | 除数为 0 | `1 / 0` |
| `TypeError` | 类型不匹配的操作 | `"1" + 1` |
| `NameError` | 访问未定义的变量 | `print(未定义变量)` |
| `IndexError` | 列表索引越界 | `[1,2,3][99]` |
| `KeyError` | 字典键不存在 | `d["不存在的键"]` |
| `FileNotFoundError` | 文件不存在 | `open("不存在.txt")` |
| `AttributeError` | 调用对象不存在的属性/方法 | `None.upper()` |

### 6. 抛出异常 raise

`raise` 用于**主动抛出异常**，搭配 `Exception(描述信息)` 创建异常对象后抛出：

```python
# 创建异常对象并抛出
e = Exception("余额不足！")
raise e

# 也可以一步完成
raise Exception("余额不足！")
```

> `raise` 触发后，程序会立即中断当前函数，若未被 `try/except` 捕获则程序崩溃。

### 7. 综合实战：模拟银行取款

将 `global`、`raise`、`try/except` 结合在一个完整场景中练习：

```python
# 账户余额和状态（全局变量）
balance = 1000
is_frozen = False

def withdraw(amount):
    """
    取款函数
    - 账户冻结 → 抛出冻结异常
    - 余额不足 → 抛出余额不足异常
    - 正常      → 扣减余额并打印
    """
    global balance
    if is_frozen:
        raise Exception("账户已冻结")
    if balance < amount:
        raise Exception(f"余额不足！当前余额：{balance} 元")
    balance -= amount
    print("取款成功，当前余额：", balance)

# 第一次取款：余额充足，正常执行
withdraw(200)             # 当前余额：800

# 第二次取款：超出余额，触发异常
try:
    withdraw(1000)
except Exception as e:
    print(e)              # 余额不足！当前余额：800 元
```

**知识点对照：**

| 代码 | 用到的知识点 |
|------|--------------|
| `global balance` | 函数内修改全局变量 |
| `raise Exception(...)` | 主动抛出自定义异常 |
| `if is_frozen` / `if balance < amount` | 条件判断 + 业务逻辑校验 |
| `try / except Exception as e` | 捕获异常并打印错误信息 |
| `f"余额不足！当前余额：{balance} 元"` | f-string 格式化输出 |

### 8. 更多异常报错案例

**NameError — 访问未定义变量（来自 py_try_cach.py）**

```python
try:
    print(llll)           # llll 未定义，抛出 NameError
finally:
    print("ooooo")        # 即使抛出异常，finally 依然执行
```

**IndexError — 列表索引越界**

```python
try:
    lst = [1, 2, 3]
    print(lst[10])        # 下标 10 不存在
except IndexError as e:
    print("索引越界：", e)
# 输出：索引越界：list index out of range
```

**KeyError — 字典键不存在**

```python
try:
    d = {"name": "Alice"}
    print(d["age"])       # 键 'age' 不存在
except KeyError as e:
    print("键不存在：", e)
# 输出：键不存在：'age'
```

**FileNotFoundError — 文件不存在**

```python
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("文件找不到：", e)
# 输出：文件找不到：[Errno 2] No such file or directory: 'data.txt'
```

**TypeError — 类型操作错误**

```python
try:
    result = "100" + 100  # 字符串与数字不能直接相加
except TypeError as e:
    print("类型错误：", e)
# 输出：类型错误：can only concatenate str (not "int") to str
```

**AttributeError — 调用不存在的属性**

```python
try:
    n = None
    n.upper()             # None 没有 upper() 方法
except AttributeError as e:
    print("属性错误：", e)
# 输出：属性错误：'NoneType' object has no attribute 'upper'
```

**ZeroDivisionError — 除数为零**

```python
try:
    a, b = 10, 0
    print(a / b)
except ZeroDivisionError as e:
    print("除零错误：", e)
# 输出：除零错误：division by zero
```

**ValueError — 类型转换失败**

```python
try:
    num = int("hello")    # 无法将字符串 'hello' 转为整数
except ValueError as e:
    print("值错误：", e)
# 输出：值错误：invalid literal for int() with base 10: 'hello'
```

---

## 五、学习要点速记

| # | 要点 |
|---|------|
| 1 | Python 用**缩进**代替花括号，同一代码块缩进必须一致 |
| 2 | `input()` 返回字符串，需要数字时用 `int()` / `float()` 转换 |
| 3 | 比较运算符不能跨类型（数字 vs 字符串） |
| 4 | `and` / `or` / `not` 组合条件 |
| 5 | 三元表达式适合简单的二选一 |
| 6 | `elif` 从上往下匹配，命中即停止 |
| 7 | `for i in range(n)` 是最基础的定次循环 |
| 8 | `break` 终止循环，`continue` 跳过本次，`else` 在未被中断时执行 |
| 9 | 推导式（列表/字典/集合/元组）是 Python 简洁写法的核心 |
| 10 | 迭代器只能前进，用 `iter()` 创建，`next()` 访问 |
| 11 | 函数参数顺序：必需参数 → 默认参数 → `*args` → `**kwargs` |
| 12 | 可变对象传入函数会被"引用传递"，修改影响原变量 |
| 13 | 函数内修改全局变量需加 `global` 声明 |
| 14 | f-string 是 Python 3.6+ 推荐的字符串格式化方式 |
| 15 | lambda 适合一行内的简单函数，结合 `map` / `filter` / `reduce` 使用 |
| 16 | 装饰器用三层嵌套结构实现：最外层接函数、中间层是 wrapper、用 `return wrapper` 返回 |
| 17 | `@decorator` 是语法糖，等价于 `func = decorator(func)`，函数定义时立即替换 |
| 18 | `@functools.wraps(func)` 保留原函数名称和文档，装饰器中推荐加上 |
| 19 | 带参数的装饰器需三层嵌套：最外层接参数、中间层接函数、最内层是 wrapper |
| 20 | `try/except` 捕获异常防止程序崩溃，`as e` 可打印异常详情 |
| 21 | `else` 在无异常时执行，`finally` 无论是否异常都执行（常用于资源释放） |
| 22 | `raise Exception("描述")` 主动抛出异常，触发后立即中断当前函数 |
| 23 | 捕获异常尽量指定具体类型（如 `ValueError`），避免用 `Exception` 一刀切 |
| 24 | 常见异常：`ValueError` `ZeroDivisionError` `TypeError` `NameError` `IndexError` `KeyError` `FileNotFoundError` `AttributeError` |

---

## 运行方式

```bash
python py_if.py
python py_for.py
python py_def.py
python py_try_cach.py
```

> **提示**：各文件中大部分代码以注释形式保存，学习时取消注释逐段运行体验效果更佳。
