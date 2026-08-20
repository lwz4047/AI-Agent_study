# 变量
module_name = "工具模块"

# 函数
def add(a,b):
    return a+b

def greet(name):
    print(f"你好呀！{name}!")


# 只想在本模块实行
print("my_module模块中的内置全局变量__name__:",__name__)
if __name__ == "__main__":
# 测试代码：测试功能是否正常，可以使用
    print(add(1, 2))