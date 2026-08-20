# 需求： 生成 1 到 3 之间的随机整数


# import random
# import requests
# # 调用random模块里的randint函数
# num = random.randint(1,100)
# print(num)
# print(type(num))


# 爬取百度内容
# response = requests.get('https://www.baidu.com')
# response.encoding = 'utf-8'
# print(response.text)

# 导入自定义模块名
# import my_module as mm # 使用别名
# # 使用功能：模块名，功能
# result = mm.add(2,4)
# print(result)

# 导入指定功能 from 模块名 import 功能名(*) * 代表导入所有功能
# from my_module import add , module_name,greet
# # 使用功能：功能
# result = add(1,2)
# print(result)
#
# print(module_name)
# greet("username")


# module_name = "py_module"
# import my_module
# # 使用本模块的功能
# print(module_name)
# # 使用工具模块的功能
# print(my_module.module_name)


import my_module     # 导入模块时，会执行所有代码

