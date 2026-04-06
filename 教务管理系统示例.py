# 教务管理系统 - 学员成绩管理

def display_menu():
    """显示主菜单"""
    print("\n" + "="*40)
    print("        教务管理系统")
    print("="*40)
    print("1. 添加学生信息")
    print("2. 修改学生信息")
    print("3. 删除学生信息")
    print("4. 查询学生信息")
    print("5. 列出所有学生")
    print("6. 统计班级成绩")
    print("7. 退出系统")
    print("="*40)

def add_student(students):
    """添加学生信息"""
    name = input("请输入学生姓名：").strip()
    # 检查姓名是否已存在
    for stu in students:
        if stu['name'] == name:
            print("错误：该学生已存在！")
            return
    try:
        chinese = float(input("请输入语文成绩："))
        math = float(input("请输入数学成绩："))
        english = float(input("请输入英语成绩："))
    except ValueError:
        print("错误：成绩必须是数字！")
        return
    # 添加学生记录
    students.append({
        'name': name,
        'chinese': chinese,
        'math': math,
        'english': english
    })
    print(f"学生 {name} 添加成功！")

def modify_student(students):
    """修改学生信息"""
    name = input("请输入要修改的学生姓名：").strip()
    for stu in students:
        if stu['name'] == name:
            try:
                chinese = float(input("请输入新的语文成绩："))
                math = float(input("请输入新的数学成绩："))
                english = float(input("请输入新的英语成绩："))
            except ValueError:
                print("错误：成绩必须是数字！")
                return
            stu['chinese'] = chinese
            stu['math'] = math
            stu['english'] = english
            print(f"学生 {name} 信息修改成功！")
            return
    print("错误：未找到该学生！")

def delete_student(students):
    """删除学生信息"""
    name = input("请输入要删除的学生姓名：").strip()
    for i, stu in enumerate(students):
        if stu['name'] == name:
            del students[i]
            print(f"学生 {name} 已删除！")
            return
    print("错误：未找到该学生！")

def query_student(students):
    """查询单个学生信息"""
    name = input("请输入要查询的学生姓名：").strip()
    for stu in students:
        if stu['name'] == name:
            print("\n学生信息：")
            print(f"姓名：{stu['name']}")
            print(f"语文：{stu['chinese']}")
            print(f"数学：{stu['math']}")
            print(f"英语：{stu['english']}")
            return
    print("错误：未找到该学生！")

def list_all_students(students):
    """列出所有学生"""
    if not students:
        print("当前没有任何学生记录。")
        return
    print("\n所有学生信息：")
    print("姓名\t语文\t数学\t英语")
    print("-"*30)
    for stu in students:
        print(f"{stu['name']}\t{stu['chinese']}\t{stu['math']}\t{stu['english']}")

def calculate_statistics(students):
    """统计班级成绩"""
    if not students:
        print("当前没有任何学生，无法统计。")
        return

    # 初始化统计变量
    chinese_scores = [stu['chinese'] for stu in students]
    math_scores = [stu['math'] for stu in students]
    english_scores = [stu['english'] for stu in students]

    # 计算最高分、最低分、平均分
    chinese_max = max(chinese_scores)
    chinese_min = min(chinese_scores)
    chinese_avg = sum(chinese_scores) / len(chinese_scores)

    math_max = max(math_scores)
    math_min = min(math_scores)
    math_avg = sum(math_scores) / len(math_scores)

    english_max = max(english_scores)
    english_min = min(english_scores)
    english_avg = sum(english_scores) / len(english_scores)

    # 找出最高分和最低分对应的学生姓名
    chinese_max_students = [stu['name'] for stu in students if stu['chinese'] == chinese_max]
    chinese_min_students = [stu['name'] for stu in students if stu['chinese'] == chinese_min]
    math_max_students = [stu['name'] for stu in students if stu['math'] == math_max]
    math_min_students = [stu['name'] for stu in students if stu['math'] == math_min]
    english_max_students = [stu['name'] for stu in students if stu['english'] == english_max]
    english_min_students = [stu['name'] for stu in students if stu['english'] == english_min]

    # 输出统计结果
    print("\n班级成绩统计：")
    print(f"语文最高分：{chinese_max} 分，学生：{', '.join(chinese_max_students)}")
    print(f"语文最低分：{chinese_min} 分，学生：{', '.join(chinese_min_students)}")
    print(f"语文平均分：{chinese_avg:.2f} 分")
    print()
    print(f"数学最高分：{math_max} 分，学生：{', '.join(math_max_students)}")
    print(f"数学最低分：{math_min} 分，学生：{', '.join(math_min_students)}")
    print(f"数学平均分：{math_avg:.2f} 分")
    print()
    print(f"英语最高分：{english_max} 分，学生：{', '.join(english_max_students)}")
    print(f"英语最低分：{english_min} 分，学生：{', '.join(english_min_students)}")
    print(f"英语平均分：{english_avg:.2f} 分")

def main():
    """主程序"""
    students = []  # 存储所有学生信息的列表，每个元素为字典
    while True:
        display_menu()
        choice = input("请输入操作编号：").strip()
        if choice == '1':
            add_student(students)
        elif choice == '2':
            modify_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            query_student(students)
        elif choice == '5':
            list_all_students(students)
        elif choice == '6':
            calculate_statistics(students)
        elif choice == '7':
            print("感谢使用教务管理系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")

if __name__ == "__main__":
    main()