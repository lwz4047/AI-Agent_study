# Python 基础篇 — 学习笔记

## 目录

- [一、条件判断（py_if.py）](#一条件判断py_ifpy)
- [二、循环语句（py_for.py）](#二循环语句py_forpy)
- [三、函数（py_def.py）](#三函数py_defpy)
- [四、学习要点速记](#四学习要点速记)

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

---

## 四、学习要点速记

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

---

## 运行方式

```bash
python py_if.py
python py_for.py
python py_def.py
```

> **提示**：各文件中大部分代码以注释形式保存，学习时取消注释逐段运行体验效果更佳。
