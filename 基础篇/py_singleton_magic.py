# class House:
#     def __new__(cls, *args, **kwargs):
#         # cls代表类本身，必须作为第一个参数
#         print("__new__:分配内存，造房子框架")
#         # 调用父类的__new__，真正分配内存并返回对象引用
#         obj = object.__new__(cls)
#         return obj # 必须返回对象引用，否则__init__不会执行
#
#     def __init__(self,address,area):
#         print("__init__:初始话对象，给对象属性赋值，专修房子")
#         self.address = address
#         self.area = area
#
# # 实例化对象
# my_house = House("北京中南海",120)

# class Singleton:
#     # 类属性：记录唯一对象，初始值设为None
#     _instance = None
#
#     # 重写__new__方法
#     def __new__(cls, *args, **kwargs):
#         # 如果类属性_instance为None，说明还没有创建过对象
#         if cls._instance is None:
#             # 调用父类的__new__方法，创建对象并返回对象引用
#             cls._instance = object.__new__(cls)
#             return cls._instance
#         return cls._instance
#
#     def __init__(self,name):
#         # 注意：每次实例化对象都会执行__init__方法，需免重复初始化
#         # hasattr() 判断对象是否具有该属性
#         if not hasattr(self,"name"): # 判断对象是否具有name属性
#             self.name = name
#
# obg = Singleton("张三")
# print(obg)
#
# obg1 = Singleton("六四")
# print(obg1)
# print(obg.name)
# print(obg1.name)
#
# print(id(obg) == id(obg1))

# 魔术方法&魔术属性
# class Student:
#     """学生类，存储学生姓名和年龄"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Student(name={self.name}, age={self.age})"
#     def __del__(self):
#         print(f"{self.name}对象被删除")
#
# s1 = Student("小明",15)
# # print(s1.__doc__)
# # print(s1.__class__)
# # print(s1.__module__)
# print(s1)
# # 注意：__del__ 方法不用手动调用，Python的垃圾回收机制会自动处理，手动调用可能会导致资源释放异常


class Student:
    def __call__(self, a, b):
        # 对象调用时执行的逻辑（参数、逻辑都可自定义）
        return f"{a}+{b}={a+b}"

s1 = Student()
s1(1,2)