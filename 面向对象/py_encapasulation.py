# 需求：定义银行账户类，把“账户名”“余额”这些属性和“查询余额”方法打包在类里
class BankAccount:
    def __init__(self,name,balance):
        self.name = name            # 账户名（公开属性，可以在外部访问）
        self.__balance = balance    # 余额（私有属性，禁止外部直接访问）

    # 接口1：查询余额
    def check_balance(self):
        print(f"{self.name}的账户余额为{self.__balance}元。")

    # 接口2：存款（修改余额，加验证）
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        # 余额 = 余额 + 存款金额
            print("存款成功！！",f"存款金额为{self.__balance}元")
        else:
            print("存款失败")

    # 接口3：取款
    def withdraw(self,amount):
        if amount < 0:
            print("取款失败")
        elif amount > self.__balance:
            print("取款失败")
        else:
            self.__balance -= amount
            print("取款成功!!",f"取款金额为{self.__balance}元")



account = BankAccount("小米",1000)
# 强行访问私有属性（不推荐）
print(account._BankAccount__balance)
account.check_balance()
# account.deposit(500)
# account.withdraw(1000)
# 尝试去直接访问私有属性，会报错
# print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
