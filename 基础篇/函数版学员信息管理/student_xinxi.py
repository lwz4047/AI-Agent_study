# 数据要存储
# 学员信息用字典
# 多个学员信息用列表
info = []



# 1.功能界面，显示信息

def info_print():
    print("=" *30)
    print("      学院管理系统 V1.0")
    print("1. 添加学员")
    print("2. 删除学员")
    print("3. 修改学员")
    print("4. 查询学员")
    print("5. 显示所有学员")
    print("6. 退出系统")
    print("=" *30)


# 定义删除学员函数

def dele_info():
    #接受用户输入的删除姓名
    del_name = input("请输入要删除的学员的姓名：")
    #判断该学员是否存在
    for student in info:
        if del_name == student["name"]:
            #删除学员
            info.remove(student)
            print(f"删除成功！已删除【{del_name}】的下学员信息")
            print(f"当前剩余学员：{info}")
            return # 函数结束
    # 遍历完没找学员
    print(f"错误：未找到姓名为【{del_name}】的学生")

# 添加学员
def add_info():
    new_id = input("请输入学号：")
    new_name = input("请输入学员姓名：")
    new_tel = input("请输入手机号：")

    # 判断学员是否存在
    for student in info:
        if new_id == student['id']:
            print(f"该学员{new_name}已存在！无法重复添加")
            return

    student_dict = {
        "id":new_id,
        "name":new_name,
        "tel":new_tel
    }
    info.append(student_dict)
    print(f"添加成功！学员信息{student_dict}")

# 修改学员的函数
def modify_info():
    modify_name = input("输入修改的学员姓名：")
    # 判断该学员是否存在
    for student in info:
        if modify_name == student["name"]:
            student["id"] = input("请输入新的学号：")
            student["name"] = input("请输入新的姓名：")
            student["tel"] = input("请输入新的号码：")
            print(f"修改成功，{info}")
            return
    # 未找到该学员
    print(f"未找到该学员，{modify_name}")

# 查询学员
def search_info():
    # 接受用户输入的查询姓名
    search_name = input("请输入要查询的学员姓名：")

    # 判断学员是否存在
    for student in info:
        if search_name == student["name"]:
            # 找到该学员
            print("=" *20)
            print(f"学号：{student["id"]}")
            print(f"姓名：{student["name"]}")
            print(f"号码：{student["tel"]}")
            print("=" * 20)
            return
    # 没找到
    print(f"没找到该{search_name}学员！")


# 显示所有学员信息

def print_info():
    # 格式化表头
    print("=" * 34)
    print("学号\t\t姓名\t\t手机号")
    print("-" * 34)
    for student in info:
        print(f"{student['id']}\t\t{student['name']}\t\t{student['tel']:>10}")
    print("-" * 34)

# 显示功能界面
info_print()

# 不知道循环的次数，但是知道循环的结束条件 ==》 while True + break
while True:
    # 接受用户输入的功能序号
    user_num = int(input("请输入功能序号（1-6）："))

    # 根据序号执行对应功能
    if user_num == 1:
        print("选择了【添加学员】")
        add_info()
    elif user_num == 2:
        print("选择了【删除学员】")
        dele_info()
    elif user_num == 3:
        print("选择了【修改学员】")
        modify_info()
    elif user_num == 4:
        print("选择了【查询学员】")
        search_info()
    elif user_num == 5:
        print("选择了【显示所有学员】")
        print_info()
    elif user_num == 6:
        # 退出系统(二次确认)
        exit_config = input("确定要退出吗？y or n：")
        if exit_config == "y":
            print("退出成功")
            # 退出循环
            break

    else:
        print("输入有误，请重新输入")
