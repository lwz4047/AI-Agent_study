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


