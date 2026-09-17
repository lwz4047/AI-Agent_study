# 父类的父类：生物（所有生物的共性）
# class Living:
#     features = "有生命"  # 类属性
#
#     def breathe(self):
#         print("有呼吸")
#
# # 父类：动物类
# class Animal(Living):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self):
#         print(f"{self.name}在吃东西！")
#
#     def sleep(self):
#         print(f"{self.name},在睡觉")
#     def make_sound(self):
#         print("动物发出叫声！")
#
# # 子类：狗类继承动物类
# class Dog(Animal):
#     # 特有方法：小狗汪汪叫
#     def bark(self):
#         print("小狗汪汪叫")
#
# class Cat(Animal):
#     def make_sound(self): # 完全覆盖
#         # 重写父类方法，实现猫的特有叫声（我自己新增的逻辑）
#         super().make_sound() # 调用父类的make_sound方法
#         print("猫咪喵喵喵")
#
# # # 创建子类对象
# # dog = Dog("旺财",1)
# # # 继承父类的公开的方法
# # dog.eat()
# # dog.sleep()
# # # 调用自己的私有方法
# # dog.bark()
# #
# # # 访问间接继承父类的父类的属性与方法
# # dog.breathe()
#
# cat = Cat("丧彪",1)
# cat.make_sound()


# 父类1： 手表类
# class Watch:
#     def show_time(self):
#         print(f"当前时间：16:25")
#
# # 父类2： 健康设备类
# class HealthDevice:
#     def check_heart_rate(self):
#         print(f"当前心率：75次")
# # 子类： 智能手表类，继承手表类和健康设备类
# class SmartWatch(Watch,HealthDevice):
#     pass
#
# smartwatch = SmartWatch()
# smartwatch.show_time()
# smartwatch.check_heart_rate()

# class Phone:
#     def take_photo(self):
#         print("222222")
#
# class Camera:
#     def take_photo(self):
#         print("4444")
#
# class CameraPhone(Phone,Camera):
#     # 重写方法再调用
#     def take_photo(self):
#         print("222222")
#         print("4444")
#
#
# c1 = CameraPhone()
# c1.take_photo()
# # 类名.方法(子类对象)
# Camera.take_photo(c1)

# 父类1： 手表类
class Watch:
    def show_time(self):
        print(f"当前时间：16:25")

# 父类2： 健康设备类
class HealthDevice:
    def check_heart_rate(self):
        print(f"当前心率：75次")
# 子类： 智能手表类，继承手表类和健康设备类
class SmartWatch(Watch):
    def __init__(self):
        # 创建 HealthDevice 的实例
        # 去调用 HealthDevice 里的方法
        self.hd = HealthDevice()

smartwatch = SmartWatch()
smartwatch.show_time()
smartwatch.hd.check_heart_rate()