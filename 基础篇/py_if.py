# num = 34
# if num%2 == 0: # 34 % 2 == 0（true）==》执行缩进的代码
#     print("这个数为偶数")
#     print("哈哈哈")
# print("判断结束") #不管条件是否成立，都执行，和 if 同级的语句
#
# # 注意：满足条件要执行的代码，可以是一行，也可以是多行：多行代码要保证缩进量一致
# # 比较运算符： == != < > <= >=
# print(1 == 1)
# print(1 != 1)
# print(1 > 1)
# print(1 >= 1)
#
#
# print("a" == "a")
#注意：数字和字符串不能比较

#逻辑运算符：and or not
#and
#登陆验证
# username = input('Please input your username: ')
# password = input('Please input your password: ')
# if username == 'admin' and password == '123456':
#     print("密码正确")
# else:
#     print("密码错误")

# 判断创建水果
# fruit = input("输入水果名称")
# if fruit == "banana" or fruit == "apple" or fruit == "mango":
#     print(f"{fruit}是常见水果")

# not
# 判断用户输入数字是否为0
# num = int(input("请输入数字："))
# if not num == 0:
#     print(f"{num}数字不为0")


# if 10:
#     print("顶顶顶顶")

# 格式： 条件成立的结果 if条件 else 条件不成立的结果 三元表达式
# score = int(input("输入成绩："))
# print("及格") if score >= 60 else print("不及格")

#写一个判断成绩的代码
# score = int(input("输入成绩："))
# if score >= 60:
#     print("及格")
# elif score >= 80:
#     print("优秀")
# elif score >= 90:
#     print("优秀")
# else:
#     print("不及格")

# 会员购物优惠判断
# 判断是否为会员
# 是会员，输入金额，打9.5折
# 不是会员，更具金额判断
# is_member = input("是否为会员：")
# if is_member == "是":
#     money = float(input("请输入金额："))
#     print(f"会员打9.5折，应付金额：{money*0.95}")
# elif is_member == "否":
#     money = float(input("请输入金额："))
#     if money >= 100:
#         print(f"满100打8.5折，应付金额：{money*0.85}")
#     elif money >= 50:
#         print(
#             f"满50打8折，应付金额：{money*0.8}"
#         )
# else:
#     print("下次光临")



