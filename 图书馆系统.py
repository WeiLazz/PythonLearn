def display_menu():
    """菜单"""
    print("\n" + "="*40)
    print("1.添加图书")
    print("2.显示所有图书")
    print("3.搜索图书")
    print("4.删除图书")
    print("5.退出程序")
    print("="*40)

def add_books(books):
    """添加图书"""
    name = input("请输入图书名：").strip()
    for b in books:
        if b['bookName'] == name:
            print("已有该图书！")
            return
    writer = input("请输入作者姓名：").strip()
    year = input("请输入出版年份：").strip()
    bookID = len(books) + 1
    books.append({
        'bookName':name,
        'bookWriter':writer,
        'bookYear':year,
        'bookID':bookID
    })
    print(f"图书{name}添加成功！图书ID为{bookID}")

def show_books(books):
    """显示所有图书"""
    if not books:
        print("暂无图书，请先添加！")
        return
    print("图书列表：")
    print("-" * 50)
    for book in books:
        print(f"图书ID：{book['bookID']}，书名：{book['bookName']}，作者：{book['bookWriter']}，出版年份：{book['bookYear']}")
    print("-" * 50)

def search_book(books):
    """模糊搜索图书（按书名）"""
    key = input("请输入查询的书名关键字：").strip()
    if not key:
        print("关键字不能为空")
        return
    results = []
    for book in books:
        # 模糊匹配：关键字是否出现在书名中（不区分大小写）
        if key.lower() in book['bookName'].lower():
            results.append(book)
    if results:
        print(f"\n找到 {len(results)} 本图书：")
        # 格式化输出，可根据需要调整列宽
        print(f"{'ID':<4} {'书名':<20} {'作者':<12} {'年份':<6}")
        print("-" * 50)
        for book in results:
            print(f"{book['bookID']:<4} {book['bookName']:<20} {book['bookWriter']:<12} {book['bookYear']:<6}")
    else:
        print("未找到匹配的图书")

def main():
    """主程序"""
    books = []
    while True:
        display_menu()
        choice = input("请输入序号：").strip()
        if choice == '1':
            add_books(books)
        elif choice == '2':
            show_books(books)
        elif choice == '3':
            search_book(books)
        else:
            print("无效输入，请重新输入！")

if __name__ == "__main__":
    main()