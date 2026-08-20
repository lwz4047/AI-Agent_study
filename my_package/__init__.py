# 通过 __all__ 声明，当外部执行 from my_package import * 时，
# 只对外暴露 my_package 这一个名称


"""

__all__ 是一个列表，专门控制from ... import * 的导入范围，
避免导入不必要的内容：
.作用在包的 __init__.py 里：指定from 包名 import * 时要导入的模块
.作用在模块：指定from 模块名 import * 时要导入的类/函数/变量。


在这个文件不要写复杂的代码。
"""
__all__ = ["calc","greet"]

