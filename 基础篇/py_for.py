# 需求：输出5次你好
# for i in range(5):
#     print("你好")
# cout = 1
# while cout <= 5:
#     print("你好")
#     cout += 1
from xxsubtype import bench

#计算 1-5 的和

# i = 1
# temp = 0
# while i <= 5:
#     temp += i
#     i +=1
# print(temp)

# while循环嵌套

# 需求3排6列的坐位表
# row = 1
# while row <= 3:
#     colum = 1
#     while colum <= 6:
#         print(f"第{row}排 第{colum}列！！",end="\t")
#         colum += 1
#     print()
#     row += 1

# 凡是可以使用for循环遍历的对象都是了迭代对象

# a = "sbbhhhhhhsssd"
# for i in a:
#     print(i,end="\t")
# print()
#
#
# for i in range(1,10,2):# 遵循包前不包后的规则
#     print(i,end="\t")

# 需求：用for循环计算1-100的和
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# for循环嵌套
# for i in range(1,4):
#     for j in range(1,7):
#         print(f"第{i}排 第{j}列",end="\t")
#     print()

# break 和 continue只能在循环体中使用

# 吃五个苹果，吃第三个水果后就不吃了
# for i in range(1,6):
#     if i == 3:
#         print("吃饱了")
#         break
#     print(f"吃第{i}苹果")
# print()


# 循环与else使用
# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("密密麻麻的")# 没被break中断，else继续执行。

# 斐波那契数列

# a,b = 0,1
# while b<1000:
#     a,b = b,a+b
#     print(b)

# 列表推导式
"""
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值。
"""
#过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：

# names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# new_name = [name.upper() for name in names if len(name)>3]
# print(new_name)

#计算 30 以内可以被 3 整除的整数：

# num = [i for i in range(30) if i%3 ==0]
# print(num)

# 字典推导基本格式：
"""
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""

# 使用字符串及其长度创建字典：

# listdemo = ['Google','Runoob', 'Taobao']
# # 将列表中各字符串值为键，各字符串的长度为值，组成键值对
# newlist = {key:len(key) for key in listdemo}
# print(newlist)
#
# # 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
#
#
# num = {x : x**2 for x in {2,3,4}}
# print(num)

# 集合推导式基本格式：
"""
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
# 计算数字 1,2,3 的平方数：
# number = {x**2 for x in {1,2,3}}
# print(number)

# 判断不是 abc 的字母并输出：
# str = {x for x in "abcdsjuedhdii" if x not in 'abc'}
# print(str)


# 元组推导式基本格式：
"""
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""

#我们可以使用下面的代码生成一个包含数字 1~9 的元组：
# a = (x for x in range(1,11))
# print(a)
# print(tuple(a))
"""                                   Python3 迭代器与生成器                            """
#迭代器
# 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。

# 字符串，列表或元组对象都可用于创建迭代器：

# list = [1,2,3,4]
# it = iter(list) # 创建迭代器对象
# print(next(it)) # 输出迭代器的下一个元素
# print(next(it))

# 也可以用for 循环
# it = iter(list) # 船舰迭代器
# for i in it:
#     print(i,end=",")

# 也可以使用 next() 函数：
# import sys
#
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it),end=",")
#     except StopIteration:
#         sys.exit()

