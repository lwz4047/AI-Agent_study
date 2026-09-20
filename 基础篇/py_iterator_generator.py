# 第一步：导入判断工具（从collections.abc）模块中导入Iterable
from collections.abc import Iterable

# 第二步：判断对象是否可迭代
# print(isinstance("abc", Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance({"name":"张三"}, Iterable))
# print(isinstance(range(5), Iterable))
# print(isinstance(123, Iterable))

# li = [1,2,3,4,5]
# 
# # 通过iter（可迭代对象）获取对应的迭代器
# li_iter = iter(li)
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# # print(next(li_iter)) # StopIteration停止迭代
# 
# 
# # ==================== 自定义迭代器 ====================
# # 一个类要成为迭代器，必须实现两个魔术方法：
# #   __iter__：返回迭代器本身（一般直接 return self）
# #   __next__：返回下一个值，取完时抛出 StopIteration
# 
# # 需求：做一个从 1 数到 n 的简单迭代器
# class MyIterator:
#     def __init__(self, end):
#         self.current = 1   # 当前值，从 1 开始
#         self.end = end     # 结束值
# 
#     def __iter__(self):
#         # 返回迭代器自身，这样才能用 for 循环
#         return self
# 
#     def __next__(self):
#         # 超过结束值，抛出 StopIteration 表示迭代结束
#         if self.current > self.end:
#             raise StopIteration
#         value = self.current   # 先保存当前值
#         self.current += 1      # 再往后走一步
#         return value
# 
# 
# # 方式一：手动用 next() 一个一个取
# my_iter = MyIterator(3)
# print(next(my_iter))  # 1
# print(next(my_iter))  # 2
# print(next(my_iter))  # 3
# # print(next(my_iter))  # 再取会抛 StopIteration
# 
# # 方式二：用 for 循环（Python 自动处理 StopIteration）
# for num in MyIterator(5):
#     print(num)  # 依次输出 1 2 3 4 5


# ==================== 生成器 ====================
# 生成器是一种特殊的迭代器，用函数 + yield 就能实现，
# 不用像上面那样手写 __iter__ 和 __next__，代码更简洁。
# yield 的特点：遇到 yield 会“暂停”并返回一个值，
#           下次取值时从暂停的地方继续往下执行。

# 方式一：含 yield 的函数（生成器函数）
def my_generator(end):
    current = 1
    while current <= end:
        yield current   # 返回当前值，并暂停在这里
        current += 1    # 下次取值时，从这里继续


# 手动 next() 取值
gen = my_generator(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # 再取会抛 StopIteration

# 用 for 循环取值
for num in my_generator(5):
    print(num)  # 依次输出 1 2 3 4 5


# 方式二：生成器推导式（把列表推导式的 [] 换成 ()）
# 列表推导式：一次性生成所有数据，占内存
# 生成器推导式：用多少算多少，省内存
squares_gen = (x * x for x in range(1, 6))
print(next(squares_gen))     # 1
print(list(squares_gen))     # [4, 9, 16, 25]（剩下的值）
