# 正则表达式
import re # 导入模块
# res = re.match(r"h\w+", "hello world")
# if res:
#     print(res.group())
# else:
#     print("匹配失败")

# res = re.match(".","哈\tiabc")
# print(res.group())

# res = re.match("[abc]","c") # 匹配abc中任意字符
# print(res.group())

# res = re.match("[0-9]","980") # 匹配人一个数字
# print(res.group())

# \d*匹配任意多个数字，包括零个数字 \d+匹配一个或多个数字(至少一个) \d?  最多匹配零个或一个数字
# \d{n}匹配n个数字字符   \d{n,m}匹配n到m个数字字符
# res = re.match(r"\d{1,5}","123456abc")
# print(res.group())

# def check_email(email):
#     """判断邮箱格式是否正确，正确返回 True，否则返回 False"""
#     pattern = r"^[a-zA-Z]\w{3,15}@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$"
#     # ^[a-zA-Z]         以字母开头
#     # \w{3,15}          后面跟 3~15 个字母/数字/下划线（用户名总长 4~16）
#     # @                 @ 分隔符
#     # [a-zA-Z0-9]+      域名主体（一段字母或数字）
#     # (\.[a-zA-Z0-9]+)+ 至少一个 .域名后缀，如 .com / .com.cn
#     # $                 结尾，保证完全匹配
#     result = re.match(pattern, email)
#     return result is not None
#
#
# # 测试用例
# email_list = [
#     "zhangsan@qq.com",        # 正确
#     "lisi_123@163.com",       # 正确
#     "wangwu@mail.163.com.cn", # 正确（多级域名）
#     "1zhangsan@qq.com",       # 错误：以数字开头
#     "zs@qq",                  # 错误：缺少域名后缀
#     "zs@@qq.com",             # 错误：两个 @
#     "zhangsan@qq.com.cn ",    # 错误：结尾有空格
# ]
#
# for email in email_list:
#     if check_email(email):
#         print(f"{email} -> 邮箱格式正确")
#     else:
#         print(f"{email} -> 邮箱格式错误")


# 核心函数search方法
# res = re.search("th","python is good")
# print(res.group())

# 核心函数findall方法
# res = re.findall(r"\w{3}","python is good")
# print(res)

# 核心函数sub
# res = re.sub("python","xiaomi","hello,python! I love python") # 没有指定替换次数，默认替换所有。
# print(res)


"""贪婪模式"""
# res = re.sub("python","xiaomi","hello,python! I love python",count=1)
# print(res)
#
# print(re.sub("a","*","123aaa456aaa789A",flags=re.I)) # 忽略大小写

# * [0,*]
# res = re.match(r"\d*","123456789asdf")
# print(res.group())

# + [1,*]
# res = re.match(r"\d+","123456789aaaaa")
# print(res.group())
# {n,m} [n,m]
# res = re.match(r"\d{1,5}","123456789asdf")
# print(res.group())


# ==================== 贪婪模式 vs 非贪婪模式 ====================
# 贪婪模式（默认）：尽可能多地匹配字符
# 非贪婪模式：在量词后加 ? ，尽可能少地匹配字符

# html = "<div>hello</div><div>world</div>"
#
# # ---------- 贪婪模式 ----------
# res_greedy = re.findall(r"<div>.+</div>", html)
# print("贪婪模式：", res_greedy)
# # 输出：['<div>hello</div><div>world</div>']
# # 解释：.+ 尽可能多地匹配，把整个字符串都吞进去了
#
# # ---------- 非贪婪模式 ----------
# res_lazy = re.findall(r"<div>.+?</div>", html)
# print("非贪婪模式：", res_lazy)
# # 输出：['<div>hello</div>', '<div>world</div>']
# # 解释：.+? 尽可能少地匹配，遇到第一个 </div> 就停
#
#
# # ==================== 各种量词的非贪婪写法 ====================
# text = "aaa"
#
# print("\n--- * 与 *? ---")
# print(re.findall(r"a*", text))    # 贪婪：['aaa', '']
# print(re.findall(r"a*?", text))   # 非贪婪：['', '', '', '']
#
# print("\n--- + 与 +? ---")
# print(re.findall(r"a+", text))    # 贪婪：['aaa']
# print(re.findall(r"a+?", text))   # 非贪婪：['a', 'a', 'a']
#
# print("\n--- {n,m} 与 {n,m}? ---")
# print(re.findall(r"a{1,3}", text))   # 贪婪：['aaa']
# print(re.findall(r"a{1,3}?", text))  # 非贪婪：['a', 'a', 'a']
#
# print("\n--- ? 与 ?? ---")
# print(re.findall(r"a?", text))    # 贪婪：['a', 'a', 'a', '']
# print(re.findall(r"a??", text))   # 非贪婪：['', '', '', '']
#
#
# # ==================== 实战示例：提取引号中的内容 ====================
# s = 'name="Tom" age="18" city="Beijing"'
#
# # 贪婪：匹配从第一个 " 到最后一个 "
# print("\n贪婪提取引号内容：")
# print(re.findall(r'"(.+)"', s))
# # ['Tom" age="18" city="Beijing']
#
# # 非贪婪：每对引号单独匹配
# print("非贪婪提取引号内容：")
# print(re.findall(r'"(.+?)"', s))
# # ['Tom', '18', 'Beijing']

# 闭包
def outer():
    msg = "hello"          # 外部函数的局部变量

    def inner():
        print(msg)         # 内部函数引用了外部变量

    return inner           # 返回内部函数

fn = outer()   # outer() 执行完毕，但 msg 变量并没有被销毁
fn()           # 输出：hello  ← 这就是闭包，inner 记住了 msg

