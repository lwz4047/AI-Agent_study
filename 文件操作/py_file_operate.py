# 文本文件：指定utf-8编码，只读格式
# f = open("test.txt", "r", encoding="utf-8") # f为文件对象
# print(f.read())
#
# # 关闭文件
# f.close()

# with open("test.txt", "r", encoding="utf-8") as f:
#     # 读写操作
#     print(f.encoding)
# print(f.closed) # 检测文件的关闭状态

# 一行一行去读取
# with open("test.txt", "r", encoding="utf-8") as f:
#     content = f.read(1)
# print(content)
#
# with open("test.txt", "r", encoding="utf-8") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()
# print(f"第一行：{line1}", end="")
# print(f"第二行：{line2}",end="")
# print(f"第三行：{line3}")

# 读取所有行
# with open("test.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
# print(f"所有行：{lines}")
#
# for line in lines:
#     print(line,end="")


# # 只写模式（w）：文件不存在则创建，存在则覆盖原有内容
# with open("test2.txt", "w", encoding="utf-8") as f:
#     f.write("\n小米鹏程N90_MAX")

# 追加模式（a）；文件不存在则创建，存在则在末尾追加内容,不会覆盖旧内容
# with open("test3.txt","a",encoding="utf-8") as f: # 只能写，不能读
#     f.write("\n小米鹏程N90_MAX")


with open("test.txt","a+",encoding="utf-8") as f:
    f.write("\n小米汽车，SU7和YU7")
    print("当前指针的位置",f.tell())
    # 将指针移动到开头
    f.seek(0)
    print("读取内容",f.read())

# 文件指针：就像第一个标记，指示下次读写的起始位置
# 读模式（r，r+）指针在文件开头
# 写/追加模式（w,w+,a,a+）指针在文件末尾
