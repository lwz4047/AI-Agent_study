# Python 基础篇 — 学习笔记

## 一、条件判断（py_if.py）

### 1. if 基本语法

- 条件成立时，执行**缩进**的代码块（可以一行或多行，多行缩进量必须一致）
- 与 `if` 同级的语句，不管条件是否成立都会执行

```python
num = 34
if num % 2 == 0:
    print("这个数为偶数")   # 条件成立才执行
    print("哈哈哈")
print("判断结束")           # 同级代码，始终执行
```

### 2. 比较运算符

`==`、`!=`、`<`、`>`、`<=`、`>=`

> 注意：数字和字符串**不能**直接比较（如 `1 == "1"` 无意义）

### 3. 逻辑运算符

| 运算符 | 含义 | 示例场景 |
|--------|------|----------|
| `and` | 两边都成立才为 True | 登录验证：用户名和密码同时正确 |
| `or` | 一边成立即为 True | 判断水果：banana / apple / mango 任一匹配 |
| `not` | 取反 | 判断数字不为 0：`not num == 0` |

### 4. 隐式布尔值

- 非零数字（如 `10`）在条件中视为 `True`，可直接 `if 10:` 执行

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

会员购物优惠案例——外层判断是否会员，内层再根据金额分档打折：

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

```python
# 输出5次你好
for i in range(5):
    print("你好")
```

---

## 三、其他基础（main.py）

### 1. 函数定义

```python
def print_hi(name):
    print(f'Hi, {name}')
```

### 2. 程序入口

```python
if __name__ == '__main__':
    print_hi('PyCharm')
```

### 3. f-string 格式化字符串

- 用 `f"..."` 前缀，在 `{}` 中直接嵌入变量或表达式

---

## 四、学习要点速记

| # | 要点 |
|---|------|
| 1 | Python 用**缩进**代替花括号，同一代码块缩进必须一致 |
| 2 | `input()` 返回的是字符串，需要数字时用 `int()` / `float()` 转换 |
| 3 | 比较运算符不能跨类型（数字 vs 字符串） |
| 4 | `and` / `or` / `not` 组合条件 |
| 5 | 三元表达式适合简单的二选一赋值/输出 |
| 6 | `elif` 从上往下匹配，命中即停止 |
| 7 | `for i in range(n)` 是最基础的定次循环 |
| 8 | f-string 是 Python 3.6+ 推荐的字符串格式化方式 |

---

## 运行方式

```bash
python py_if.py
python py_for.py
```

> **提示**：`py_if.py` 中大部分代码以注释形式保存，学习时取消注释逐段运行体验。
