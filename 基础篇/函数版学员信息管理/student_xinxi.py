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

    elif user_num == 3:
        print("选择了【修改学员】")

    elif user_num == 4:
        print("选择了【查询学员】")

    elif user_num == 5:
        print("选择了【显示所有学员】")

    elif user_num == 6:
        # 退出系统(二次确认)
        exit_config = input("确定要退出吗？yes or no")
        if exit_config == "yes":
            print("退出成功")
            # 退出循环
            break

    else:
        print("输入有误，请重新输入")
