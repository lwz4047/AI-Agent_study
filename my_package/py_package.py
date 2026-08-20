# 导入包名.模块名 --精准导入指定模块
# import my_package.calc
#
# # 使用功能：包名.模块名.功能
# print(my_package.calc.add(8,2))

# 简化导入包名
# 需求： 导入 my_package 包下的greet 模块，调用里面的 say_helle 函数
# from my_package import greet
#
# # 使用功能： 模块名.功能
# greet.say_hi("小王")

# 批量导入
# from my_package import * # 指定了模块cale,greet
# print(calc.add(1,2))
# greet.say_hi("name")

# 导入包中模块的指定的功能
# from my_package.calc import add
# print(add(1, 2))
