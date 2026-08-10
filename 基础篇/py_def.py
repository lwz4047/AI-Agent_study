"""
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
    return x
"""
# def hello():
#     print("Hello World")
# hello()

# 更复杂的应用，函数中带参数：
# 比较两个数，并返回较大的次数：

# def max(a,b):
#     if a>b:
#         return b
#     else:
#         return b
# a = 4
# b = 5
# print(max(a, b))

# 计算面积函数：

# def area(width,height):
#     return width*height
# def print_welcome(name):
#     print("Welcome",name)
#
# print_welcome("Runoob")
# w = 4
# h =5
# print("width=",w,"height=",h,"area=",area(w,h))

"""
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。
如下实例调用了 printme() 函数：
"""
# 定义函数
# def printme(str):
#     # 打印任何传入的字符串
#     print(str)
#     return
#
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")

# 在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：
# a = [1,2,3] # a 是变量，但[1,2,3]是list对象，a 它仅仅是一个对象的引用（一个指针）
# a = "Sering" # 同理

"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""

# 通过 id() 函数来查看内存地址变化：
# def change(a):
#     print(id(a))  # 指向的是同一个对象
#     a = 10
#     print(id(a))  # 一个新对象
#
# a = 1
# print(id(a))
# change(a)

# 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist) # 传入函数的和在末尾添加新内容的对象用的是同一个引用。

"""
以下是调用函数时可使用的正式参数类型：
必需参数
关键字参数
默认参数
不定长参数
"""
# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：

# 可写函数说明
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
# # 调用 printme 函数，不加参数会报错
# printme("suc")

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：

# 可写函数说明
# def printinfo(name, age=35): # 未知参数放前面，默认参数放后面
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")

# 可变参数：接受任意数量的位置参数，自动打包成元组。
# 使用场景：函数需要确定不确定个数的参数
"""
不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
"""
"""
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
"""
# *var_args_tuple
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)

"""
还有一种就是参数带两个星号 **基本语法如下：

def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
"""
# 加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict,type(vardict))
#     for i in vardict.items():
#         print(i)
#     print('--------')
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)

# 声明函数时，参数中星号 * 可以单独出现，例如:

# def f(a,b,*,c):
#     return a+b+c
#
# print(f(1, 2, c=3))# c必须以关键字形式传参

# 函数返回值：return
# 也会终端函数的执行

# def add(a,b):
#
#     return a+b # 返回a+b的值，add(1,2)=3
#
# result = add(1,2) # result = add(1,2) = 1+2=3
# print(result,type(result))

# def greet():
#     print("你好吖：")
#     return "Hello World","尼玛"
# # 接受方式1：用一个变量接受（得到元组）
# result = greet()
# print(result,id(result))
#
# # 接受方式2：解包，用多个变量接受
# str1,str2 = greet()
# print(str1, str2)

# 全局变量在函数内部修改

# discount = 0.1
# def dis_count():
#     global discount # 声明为全局变量
#     discount = 0.5 # 局部变量：函数调用完就失败了
#     print("内部",discount)
#
# dis_count()
# print("外部",discount)

# 利用lambda 来创建匿名函数
"""
ambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，
但只能有一个表达式。
匿名函数不需要使用 def 关键字定义完整函数。
lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，
例如在 map()、filter()、reduce() 等函数中。
lambda 函数特点：
    lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
    lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。
"""
# lambda 语法格式：
  # lambda arguments: expression
"""
lambda是 Python 的关键字，用于定义 lambda 函数。
arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
expression 是一个表达式，用于计算并返回函数的结果。
  """

# 实列
# f = lambda :"Hello World"
# print(f())

# 以下实例使用 lambda 创建匿名函数，设置一个函数参数 a，函数计算参数 a 加 10，并返回结果：
# sex = lambda a : a+10 # a,为参数列表。
# print(sex(10))

# lambda 函数也可以设置多个参数，参数使用逗号 , 隔开：
# 以下实例使用 lambda 创建匿名函数，函数参数 a 与 b 相乘，并返回结果：
# x = lambda a, b : a * b
# print(x(5, 6))

# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。
# map() map(函数, 可迭代对象)：
# numbers = [1,2,3,4]
# squared = list(map(lambda x:x**2,numbers))
# map(函数, 可迭代对象)：遍历列表中每个元素，依次传入 lambda 函数做计算，返回 map 迭代器
# 迭代器（iterator）：一个能逐个取出容器里数据、自带 "下一个" 指针的对象，
# 只在需要时生成数据，不一次性把所有数据存进内存。
# list(...)用来存迭代器里的元素，为列表形式存储
# print(squared)

# filter(判断函数, 可迭代对象)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# 遍历列表，只保留函数返回 True的元素，返回 filter 迭代器。

# print(even_numbers)

# from functools import reduce
# numbers = [1,2,3,4,5]
# # 使用 reduce() 和 lambda 函数计算乘积
# product = reduce(lambda x,y:x*y,numbers)
# # reduce 作用：
# # 依次从序列中取出两个元素传入 lambda 函数，把运算结果作为下一轮的第一个参数，持续迭代，最终合并成单个值。
# print(product)

"""
python 装饰器，装饰器（decorator）是 Python 中的一种高级功能，
用于在不修改原函数代码的前提下，动态扩展函数或类的功能。
本质上，装饰器是一个函数：它接收一个函数作为参数，
并返回一个新的函数（通常是对原函数的增强版本）。

装饰器通过 @decorator_name 语法应用在函数或方法定义之前。
Python 还提供了一些内置装饰器，例如 @staticmethod 和 @classmethod。
常见应用场景：
日志记录：记录函数调用信息、参数和返回值
性能统计：统计函数执行时间
权限控制：限制函数访问权限
缓存：缓存函数结果，提高性能
"""
# def timer(func):
#     def wrapper(*args,**kwargs):
#         print("开始计时")
#         result = func(*args,**kwargs)
#         print("结束计时")
#         return result
#     return wrapper
#
# def say_hello():
#     print("Hello")
#
# # 这就是 @timer 背后真正执行的那行代码
# say_hello = timer(say_hello)
# say_hello()


# def timer(func):
#     print(">>> 机器内部：我正在接收原函数，并制造包装盒")
#     def wrapper():
#         print(">>> 包装盒：前置功能开始")
#         func()
#         print(">>> 包装盒：后置功能结束")
#     print(">>> 机器内部：包装盒制造完毕，返回给外部")
#     return wrapper
#
# def say_hello():
#     print("!!! 我是原函数的核心内容 !!!")
#
# print("=== 第 1 阶段：程序加载，执行替换 ===")
# say_hello = timer(say_hello)  # 这里会打印上面机器内部的报幕，但绝对不会打印 "!!!"
# print("=== 替换结束 ===")
#
# print("")
# print("=== 第 2 阶段：真正调用 ===")
# say_hello()  # 这里才开始打印 "!!!"


# 语法糖 @ 装饰器函数名
"""
你写了一个爬虫函数 get_data()，感觉它跑得很慢。
你想知道它具体耗时多少秒，但又不想在函数里到处塞 time.time()。
"""

# import time
# import functools
#
# # 这是装饰器的固定模板
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # --- 前置动作：计时开始 ---
#         start = time.time()
#         # 执行原函数
#         result = func(*args, **kwargs)
#
#         # --- 后置动作：计时结束并打印 ---
#         end = time.time()
#         print(f"⏱️ 函数 [{func.__name__}] 耗时: {end - start:.4f} 秒")
#         return result
#     return wrapper


# @timer
# def get_data():
#     print("正在爬虫---")
#     time.sleep(2.9)
#     return "爬到了 100 条数据"

# def get_data():
#     print("正在爬虫---")
#     time.sleep(2.9)
#     return "爬到了 100 条数据"
#
# get_data = timer(get_data)
# result = get_data()
# print(result) # 两种方法，普通的与语法糖


# 带参数的装饰器，
# 如果原函数有参数，需要在 wrapper 中使用 *args, **kwargs：
# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("执行前：")
#         func(*args,**kwargs)# 使用 *args, **kwargs 可以兼容任意参数函数
#         print("执行后：")
#     return wrapper
#
# @my_decorator
# def greet(name):
#     print(f"Hello {name}")
#
# greet("USA")


# 实例2
def repeat(number):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(number):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(4)
def sey_hello():
    print("Helle")

sey_hello()





