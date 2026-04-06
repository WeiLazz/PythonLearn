import json
import sys
import os

DATA_FILE = "books.json"

def load_books():
    """从JSON文件加载图书数据"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            books = json.load(f)
        # 确保ID为整数（可能从文件读取时变为字符串）
        for book in books:
            book['bookID'] = int(book['bookID'])
        return books
    except (json.JSONDecodeError, KeyError, ValueError):
        print("数据文件损坏，将使用空数据。")
        return []

def save_books(books):
    """保存图书数据到JSON文件"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def display_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("1. 添加图书")
    print("2. 显示所有图书（可排序）")
    print("3. 搜索图书")
    print("4. 删除图书")
    print("5. 修改图书信息")
    print("6. 统计信息")
    print("7. 退出程序")
    print("=" * 40)

def add_books(books):
    """添加图书（书名不能重复）"""
    name = input("请输入图书名：").strip()
    if not name:
        print("书名不能为空！")
        return
    # 检查书名是否已存在（不区分大小写）
    for b in books:
        if b['bookName'].lower() == name.lower():
            print("已有该图书！")
            return
    writer = input("请输入作者姓名：").strip()
    if not writer:
        print("作者不能为空！")
        return
    year = input("请输入出版年份：").strip()
    if not year.isdigit() or len(year) != 4:
        print("年份格式错误，请输入4位数字！")
        return
    # 生成新ID：当前最大ID + 1
    if books:
        new_id = max(book['bookID'] for book in books) + 1
    else:
        new_id = 1
    books.append({
        'bookName': name,
        'bookWriter': writer,
        'bookYear': year,
        'bookID': new_id
    })
    save_books(books)
    print(f"图书“{name}”添加成功！图书ID为{new_id}")

def show_books(books):
    """显示所有图书，支持按年份排序"""
    if not books:
        print("暂无图书，请先添加！")
        return
    # 询问排序方式
    sort_choice = input("是否按年份排序？(y/n，默认n)：").strip().lower()
    if sort_choice == 'y':
        order = input("升序(a)还是降序(d)？(默认升序)：").strip().lower()
        reverse = (order == 'd')
        sorted_books = sorted(books, key=lambda b: int(b['bookYear']), reverse=reverse)
    else:
        sorted_books = books
    print("\n图书列表：")
    print(f"{'ID':<4} {'书名':<20} {'作者':<12} {'年份':<6}")
    print("-" * 50)
    for book in sorted_books:
        print(f"{book['bookID']:<4} {book['bookName']:<20} {book['bookWriter']:<12} {book['bookYear']:<6}")

def search_book(books):
    """按书名或作者模糊搜索"""
    key = input("请输入搜索关键字（支持书名/作者）：").strip()
    if not key:
        print("关键字不能为空！")
        return
    results = []
    for book in books:
        if (key.lower() in book['bookName'].lower() or
            key.lower() in book['bookWriter'].lower()):
            results.append(book)
    if results:
        print(f"\n找到 {len(results)} 本图书：")
        print(f"{'ID':<4} {'书名':<20} {'作者':<12} {'年份':<6}")
        print("-" * 50)
        for book in results:
            print(f"{book['bookID']:<4} {book['bookName']:<20} {book['bookWriter']:<12} {book['bookYear']:<6}")
    else:
        print("未找到匹配的图书")

def delete_book(books):
    """根据ID删除图书"""
    try:
        del_id = int(input("请输入要删除的图书ID：").strip())
    except ValueError:
        print("ID必须是数字！")
        return
    for i, book in enumerate(books):
        if book['bookID'] == del_id:
            del books[i]
            save_books(books)
            print(f"图书ID {del_id} 已删除。")
            return
    print(f"未找到ID为 {del_id} 的图书。")

def modify_book(books):
    """修改图书信息"""
    try:
        mod_id = int(input("请输入要修改的图书ID：").strip())
    except ValueError:
        print("ID必须是数字！")
        return
    # 查找图书
    target = None
    for book in books:
        if book['bookID'] == mod_id:
            target = book
            break
    if not target:
        print(f"未找到ID为 {mod_id} 的图书。")
        return
    print(f"当前信息：书名={target['bookName']}, 作者={target['bookWriter']}, 年份={target['bookYear']}")
    print("留空表示不修改该项。")
    new_name = input("请输入新书名：").strip()
    if new_name:
        # 检查新书名是否与其他书冲突（排除自身）
        for book in books:
            if book['bookID'] != mod_id and book['bookName'].lower() == new_name.lower():
                print("书名已存在，修改取消。")
                return
        target['bookName'] = new_name
    new_writer = input("请输入新作者：").strip()
    if new_writer:
        target['bookWriter'] = new_writer
    new_year = input("请输入新年份：").strip()
    if new_year:
        if not new_year.isdigit() or len(new_year) != 4:
            print("年份格式错误，修改取消。")
            return
        target['bookYear'] = new_year
    save_books(books)
    print("图书信息已更新。")

def statistics(books):
    """统计信息"""
    if not books:
        print("暂无图书，无法统计。")
        return
    total = len(books)
    print(f"\n📚 图书总数：{total} 本")
    # 统计作者作品数量
    author_count = {}
    for book in books:
        author = book['bookWriter']
        author_count[author] = author_count.get(author, 0) + 1
    print("\n📖 作者作品数量：")
    for author, count in author_count.items():
        print(f"  {author}: {count} 本")
    # 可选：显示最早/最晚出版的图书
    if books:
        min_year = min(books, key=lambda b: int(b['bookYear']))
        max_year = max(books, key=lambda b: int(b['bookYear']))
        print(f"\n⏱️ 最早出版：{min_year['bookName']} ({min_year['bookYear']})")
        print(f"⏱️ 最晚出版：{max_year['bookName']} ({max_year['bookYear']})")

def main():
    books = load_books()
    print("欢迎使用图书管理系统（增强版）！")
    while True:
        display_menu()
        choice = input("请输入序号（1-7）：").strip()
        if choice == '1':
            add_books(books)
        elif choice == '2':
            show_books(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            modify_book(books)
        elif choice == '6':
            statistics(books)
        elif choice == '7':
            print("数据已保存，感谢使用，再见！")
            sys.exit(0)
        else:
            print("无效输入，请重新选择！")

if __name__ == "__main__":
    main()