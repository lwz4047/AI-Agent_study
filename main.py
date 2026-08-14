# =============================================
#   PythonStudy 项目主入口
#   整合基础篇各模块，统一从此处启动
# =============================================

import os
import sys

# 将基础篇路径加入模块搜索路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "基础篇"))
sys.path.append(os.path.join(BASE_DIR, "基础篇", "函数版学员信息管理"))


def show_menu():
    """显示主菜单"""
    print("=" * 40)
    print("      PythonStudy 基础篇学习项目")
    print("=" * 40)
    print("1. 运行学员信息管理系统")
    print("2. 查看项目结构")
    print("0. 退出")
    print("=" * 40)


def show_project_structure():
    """打印项目目录结构"""
    structure = """
PythonStudy/
├── main.py                          ← 项目主入口（当前文件）
└── 基础篇/
    ├── py_if.py                     ← 条件判断（if/elif/else/三元表达式）
    ├── py_for.py                    ← 循环语句（for/while/推导式/迭代器）
    ├── py_def.py                    ← 函数（参数/返回值/作用域）
    ├── py_try_cach.py               ← 异常处理（try/except/else/finally）
    └── 函数版学员信息管理/
        └── student_xinxi.py         ← 综合练习：学员信息管理系统
"""
    print(structure)


def run_student_system():
    """启动学员信息管理系统"""
    print("\n正在启动学员信息管理系统...\n")
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "student_xinxi",
            os.path.join(BASE_DIR, "基础篇", "函数版学员信息管理", "student_xinxi.py")
        )
        module = importlib.util.load_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"启动失败：{e}")


def main():
    """主函数：项目入口"""
    show_menu()
    while True:
        try:
            choice = input("\n请输入序号：").strip()
        except KeyboardInterrupt:
            print("\n已退出。")
            break

        if choice == "1":
            run_student_system()
        elif choice == "2":
            show_project_structure()
        elif choice == "0":
            print("再见！")
            break
        else:
            print("输入有误，请重新输入（0-2）")


if __name__ == "__main__":
    main()
