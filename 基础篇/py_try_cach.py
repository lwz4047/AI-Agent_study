# 异常处理
# try:
#     num = int(input("请输入一个数字："))
#     print(num)
# except Exception: # Exception 是所有非语法错误异常的父类
#     print("输入错误！请输入一个正确的数字")
# print("=========")
from tokenize import blank_re

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

# try:
#     print(llll)
# finally: # 不管是否报错，程序都要执行
#     print("ooooo")

# === 抛出自定以异常 ===
# 创建异常对象：异常类型（异常具体描述信息）
# e = Exception("余额不足！")
# # 抛出异常
# raise e


# 需求模拟银行取款需求
# 账户余额和状态
balance = 1000
is_frozen = False

def withdraw(amount):
    """
    作用：取款（金额超出余额抛出余额不足的异常，账户弹出冻结异常
    参数：取款的金额设置为参数
    返回值：无
    :return:
    """
    global balance
    # 先判断账户是否冻结

    if is_frozen:
        # 账户冻结 == > 抛出异常
        raise Exception("账户已冻结")
    if balance < amount :
       raise Exception(f"余额不足！ 当前余额：{balance}元")
    # 取款的金额
    balance -= amount
    print("当前余额：",balance)

withdraw(200)

try :
    withdraw(1000)
except Exception as e:
    print(e)
