import pickle, os


print("Rinux0.1")

with open("books.pickle", "rb") as f:
    books = pickle.load(f)
user = "user"



while True:
    if user == "user":
        bash = input("user@user-PC~$")
    else:
        bash = input("root@user-PC~#")

    if bash == "sudo -i":
        user = "root"
    elif bash == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif bash == "all books":
        print(books)
    elif bash == "add book":
        if user == "root":
            book_name = input("请输入书名：")
            books.append(book_name)
            with open("books.pickle", "wb")as bo:
                pickle.dump(books, bo)
                print("书籍添加成功。")
        else:
                print("你的权限不够，请升级权限后再试。")
    elif bash == "delete book":
        if user == "root":
            book_nameR = input("请输入要删除书籍的书名：")
            try:
                books.remove(book_nameR)
                with open("books.pickle", "wb")as bo:
                    pickle.dump(books, bo)
            except:
                print("此书籍可能不存在")
        else:
            print("你的权限不够，请升级权限后再试。")
    elif bash == "help":
        print("sudo             转为root管理员权限")
        print("clear            清空终端")
        print("all              显示所有书籍")
        print("add              添加书籍(需要root管理员权限)")
        print("delete           删除书籍")
        print("help             查看所有命令")
    else:
        print("此命令可能不存在，也可能目前尚未支持，请谅解。")
