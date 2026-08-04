# 异常处理
# try:
#     num = int(input("请输入一个数字："))
#     print(num)
# except Exception: # Exception 是所有非语法错误异常的父类
#     print("输入错误！请输入一个正确的数字")
# print("=========")

# 捕获指定异常
# try:
#     num = int(input("请输入一个数字："))
# except ValueError:
#     print("传入的值不对")

# 捕获多种错误
# try:
#     # num = int(input("请输入一个数字："))
#     print(1/0)
#     print("1">1)
# except ValueError as e: # except 异常类型 as e 捕获并打印异常信息
#     print("传入的值不对",e)
# except ZeroDivisionError as e:
#     print("除数不能为0",e)
# except TypeError as e:
#     print("指针错误",e)

# else yu finally
# try:
#     num = int(input("sssss:"))
# except ValueError as e:
#     print(e)
# else:
#     # 没报错继续执行
#     print(num,type(num))

try:
    print(llll)
finally: # 不管是否报错，程序都要执行
    print("ooooo")
