"""常用类型 ： 鸭子类型"""
# # 微信支付类
# class WeChatPay:
#     def pay(self,money):
#         print(f"微信支付：扣除微信余额{money}元")
#
# # 支付宝支付类
# class Alipay:
#     def pay(self,money):
#          print(f"支付宝支付：扣除支付宝余额{money}元")
#
# # 银行卡支付类
# class Bank:
#     def pay(self,money):
#         print(f"银行卡支付：扣除银行卡余额{money}元")
#
# # 统一的支付接口：不管是什么支付对象，都调用pay方法
# def pay_order(pay_obj,money):
#     pay_obj.pay(money)
#
# # 测试不同支付方式
# pay_order(WeChatPay(),100) # pay_obj = WeChatPay() money = 100  pay_obj.pay(money) = WeChatPay().pay(100)
# pay_order(Alipay(),500) # pay_obj = Alipay() money = 500  pay_obj.pay(money) = Alipay().pay(100)
# pay_order(Bank(),500) # pay_obj = Bank() money = 500  pay_obj.pay(money) = Bank().pay(100)


# 父类：动物类，定义统一接口
# class Animal:
#     def make_sound(self):
#         print("动物发出声音~")

# 子类：狗类，重写叫声方法
# class Dog(Animal):
#     def make_sound(self):
#         print("小狗汪汪叫！！！")
#
# # 子类：猫类，重写叫声方法
# class Cat(Animal):
#     def make_sound(self):
#         print("丧彪喵喵叫！！")
#
# # 子类：鸡类，重写叫声方法
# class Chicken(Animal):
#     def make_sound(self):
#         print("小鸡怎么叫！！")
#
# # 统一的接口，调用不同动物的叫声
# def animal_speak(animal):
#     animal.make_sound() # 同一方法名，不同对象有不同的反应
#
# animal_speak(Dog()) #  animal = Dog()   animal.make_sound() = Dog().make_sound()

class Pet:
    def eat(self):
        print("宠物吃东西~")

class Dog(Pet):
    def eat(self):
        print("狗吃骨头~")

class Cat(Pet):
    def eat(self):
        print("猫吃鱼~")

class Pig(Pet):
    def eat(self):
        print("猪吃饲料~")

class Rabbit(Pet):
    def eat(self):
        print("兔子吃草~")

# 主人类
class Master:
    # 定义统一的接口
    def feed(self,pet):
        print("给宠物喂食~")
        pet.eat()

# 主人去喂养不同的宠物
master = Master()
master.feed(Pig())
master.feed(Dog())
master.feed(Cat())
master.feed(Rabbit())
