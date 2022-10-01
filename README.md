# Rinux0.1.6(Build 100106）
一个命令类似于Linux的图书管理系统
目前正处于build版本，建议换为Rinux0.1.3（稳定），此版本预计将于2022.10.2（10.2进行最终测试，将于11：00正式发布）正式发布。
## 已添加的新功能：
### （1）添加账号后输入`sudo -i`时需要输入用户名、密码才可登录
#### 添加账户命令（无root即可创建）：`name user`
### （2）更改了查看所有书时打印的样式。
#### 原样式：列表
#### ["小红帽", "格林童话", "骆驼祥子"]
### 现样式：遍历+书的总数量
#### 1 小红帽
#### 2 格林童话
#### 3 骆驼祥子
#### 书的总数量:3
### （3）一次性添加多个书籍
#### 可以通过`add books`命令一次性添加多个书籍。
### （4）更改书籍名称、更换书籍。
#### 输入`replace book`这个命令，然后填写要更换的书的编号和更换后的书名即可。
### （5）将添加书籍（包括添加多本书籍）、更改书籍名称、都添加了打印所有书籍让您更加便利。
### （6）在您添加、改变书名时（仅添加多本、添加和改变书名，后续会持续完善）会检测此书是否存在。
### （7）出现了命令我文件，只需点击无需自己使用命令运行
