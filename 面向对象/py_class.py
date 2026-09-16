# 需求：定义一个汽车类
# class Car:
#     """汽车类"""
#     pass    # pass表示占位，表示孔磊，后续会加属性和方法
#

# 创建对象（实例化对象）： 对象名 = 类名()
# car1 = Car()
# print(car1) #<__main__.Car object at 0x000001EC3312D6A0>对像的内存地址
#
# # 第二次
# car2 = Car()
# print(car2) #<__main__.Car object at 0x000001C6937B7D90>对像的内存地址
# 两个内存地址不同

# 需求：给汽车类添加两个方法 start 和 run
# class Car:
#    """汽车类"""
#    def start(self): # 表示实例方法：带有self参数，self表示调用该方法的对象
#        print("汽车启动！！")
#        print("self",self)
#
#    def run(self):
#        print("汽车怎在行驶")
#
# # 创建对象
# car = Car()
# car.start()
# print("car",car) # self = car
# car.run()
#
# car1 = Car()
# car1.start()
# print("car1",car1) # self = car1
# car1.run()

# class Car:
#     # 类属性： 所有汽车共享，轮子数量为4
#     wheel_count = 4
#     def start(self):
#         print("我可以启动了！！")
#
# # 类和对象都可以访问类的属性
# # 创建对象
# car = Car()
# print(car.wheel_count)
#
# car1 = Car()
# print(car1.wheel_count)
#
# print(Car.wheel_count)

# class Car:
#     """汽车类"""
#     wheel_count = 4
#     # 构造函数
#     def __init__(self,color,brand):
#         self.color = color
#         self.brand = brand
#
#     def start(self):
#         print(f"{self.color}的{self.brand}启动了")
# # 给实例对象属性赋值
# # 创建对象，直接调用__init__构造函数，直接初始化(color,brand)
# car = Car("红色","小米SU7")
# car.start()
#
# car1 = Car("蓝色","小米鹏程N90")
# car1.start()



class Car:
    def __init__(self,brand):
        self.brand = brand
    def __del__(self): # 虚构函数 程序结束时，对象自动触发，触发__del__方法
        print(f"{self.brand}被销毁了")


# 创建对象
car = Car("丰田")
