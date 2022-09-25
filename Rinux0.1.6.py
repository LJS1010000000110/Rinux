import pickle, os, sys


print("欢迎使用Rinux0.1.6，如有命令不知请输入“help”命令，感谢您的支持")
books = []
with open("books.pickle", "rb") as f:
    books = pickle.load(f)
PC_name = None
with open("PCname.pickle", "rb") as a:
    PC_name = pickle.load(a)
UserName = []
with open("User.pickle", "rb") as y:
    UserName = pickle.load(y)
user = "user"
usern = None


while True:
    if user == "user":
        print("user@user-",PC_name,"~$")
        bash = input("    ")
    else:
        print("root@",usern,"-", PC_name, "~#")
        bash = input("    ")

    if bash == "sudo -i":
        a = input("请输入用户名:")
        for i in range(len(UserName)):
            if UserName[i] == a:
                print("验证成功。")
                acd = input("请输入用户密码：")
                if UserName[i + 1] == acd:
                    print("登陆成功。")
                    user = "root"
                    usern = a
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("欢迎使用Rinux0.1.6，如有命令不知请输入“help”命令，感谢您的支持")
                else:
                    print("验证失败。")
                    sys.exit()
                break
            elif i == len(UserName) - 1:
                print("验证失败。")
                break
    elif bash == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif bash == "all books":
        for i in range(len(books)):
            print(i + 1, books[i])
            if i == len(books) - 1:
                print("书的总数量：", len(books))
    elif bash == "replace book":
        if user == "root":
            for i in range(len(books)):
                print(i + 1, books[i])
            book_name3 = input("请输入要更换书籍的编号：")
            book_name2 = input("请输入此书更改后的书名：")
            try:
                book_name3 = int(book_name3)
                books[book_name3 - 1] = book_name2
                with open("books.pickle", "wb") as bu:
                    pickle.dump(books, bu)
                    print("书籍改变成功。")
                    for i in range(len(books)):
                        print(i + 1, books[i])
                        if i == len(books) - 1:
                            print("书的总数量：", len(books))
            except:
                print("请输入正确的书籍编号。")
        else:
                print("你的权限不够，请升级权限后再试。")
    elif bash == "add book":
        if user == "root":
            for i in range(len(books)):
                print(i + 1, books[i])
            book_name = input("请输入书名：")
            books.append(book_name)
            with open("books.pickle", "wb")as bu:
                pickle.dump(books, bu)
                print("书籍添加成功。")
                for i in range(len(books)):
                    print(i + 1, books[i])
                    if i == len(books) - 1:
                        print("书的总数量：", len(books))
        else:
                print("你的权限不够，请升级权限后再试。")
    elif bash == "add books":
        if user == "root":
            book_num = input("请问要添加多少本：")
            book_num = int(book_num)
            try:
                for i in range(book_num):
                    book_name = input("请输入书名：")
                    for i in range(len(books)):
                        if books[i] == book_name:
                            print("此书存在。")
                            break
                        elif i == len(books) - 1:
                            books.append(book_name)
                            with open("books.pickle", "wb") as mnu:
                                pickle.dump(books, mnu)
                            print("书籍添加成功。")
                            for i in range(len(books)):
                                print(i + 1, books[i])
                                if i == len(books) - 1:
                                    print("书的总数量：", len(books))
            except:
                print("你输入的不是数据类型。")
        else:
                print("你的权限不够，请升级权限后再试。")
    elif bash == "name PC":
        if user == "root":
            book_name = input("请输入要取的计算机名：")
            PC_name = book_name
            with open("PCname.pickle", "wb")as v:
                pickle.dump(PC_name, v)
                print("更改计算机名成功。")
        else:
                print("你的权限不够，请升级权限后再试。")
    elif bash == "delete book":
        if user == "root":
            for i in range(len(books)):
                print(i + 1, books[i])
            book_nameR = input("请输入要删除书籍的书名：")
            try:
                books.remove(book_nameR)
                with open("books.pickle", "wb")as bo:
                    pickle.dump(books, bo)
            except:
                print("此书籍可能不存在")
        else:
            print("你的权限不够，请升级权限后再试。")
    elif bash == "name user":
        usm = input("请输入用户名：")
        usp = input("请输入用户密码：")
        usern = usm
        UserName.append(usm)
        UserName.append(usp)
        with open("User.pickle", "wb")as vb:
            pickle.dump(UserName, vb)
    elif bash == "exit":
        sys.exit()
    elif bash == "help":
        print("sudo             转为root管理员权限")
        print("clear            清空终端")
        print("all              显示所有书籍")
        print("add              添加书籍(需要root管理员权限)")
        print("delete           删除书籍(需要root管理员权限)")
        print("help             查看所有命令")
        print("name             更改系统需要的各种名(需要root管理员权限)")
        print("exit             关闭Rinux")
    else:
        print("此命令可能不存在，也可能目前尚未支持，请谅解。")