# class Person:
#     def __init__(self,name):
#         self.name = name # 实例属性
#
#     def greet(self): #实例方法：带有self参数，self代表调用该方法的对象本身
#         print(f"你好呀，我是{self.name}~")
#
# # 必须创建实例对象才能调用
# person = Person("张三")
# person.greet()

# 静态方法

# class GeometryTool:
#     # 几何工具类
#     @staticmethod   # 静态方法
#     def circle_area(redius):
#         """计算圆的面积：nr2"""
#         return 3.14 * redius ** 2
#
#
# # 直接通过类名调用静态方法，不用创建对象(推荐)
# print(GeometryTool.circle_area(5))

# 类方法
class Person:
    average_age = 75 # 平均年龄（类属性）

    @classmethod
    def get_average_age(cls): # 类方法：cls代表类本身(无需显示传参)
        """获取平均年龄"""
        return cls.average_age # 可维护性更强

    @classmethod
    def set_average_age(cls,age): # 类方法：cls代表类本身(无需显示传参)
        """设置平均年龄"""
        cls.average_age = age


# person = Person()
# # 通过对象调用方法
# person.set_average_age(99)
# print(person.get_average_age())
#
# person2 = Person()
# print(person2.get_average_age())

# 通过类名去调用
Person.set_average_age(100)
print(Person.get_average_age())


