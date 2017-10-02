class User:
    def __init__(self, username, password, info, author):
        self.username = username
        self.password = password
        self.info = info
        author="%s,%s,%s"%("lizhi","caoyudong","zhangzhihang")
        self.author = author
        
    def show_info(self):
        userinfo = "用户名：%s\n" % self.username
        userinfo = "密码：%s\n" % self.password
        userinfo = "个人信息：%s" %self.info
        print(userinfo)
        
    def edit_info(self, info):
        self.info = info
        
    def change_pwd(self,password):
        self.password = "123456"
        pwd = input("please enter current password:")
        if pwd == self.password:
            print("sucessful,please enter new pasword:")
            self.password=password
        
    def add_author(self,add_str):
        add_str="%s"%(",fangyue")
        self.author += add_str[0:8]

    def reduce_author(self):
        part1_author=self.author[0:17]
        part2_author=self.author[30:]
        self.author = part1_author + part2_author

    def retuen_username(self,username):
        self.username = username
        return
        
class Activity:
    def __init__(self, title, content, date, member_num=0):
        self.title = title
        self.content = content
        self.date = date
        self.member_num = str(member_num)
    
    def add_member(self):
        self.member_num = str(int(self.member_num)+1)

    def reduce_member(self):
        self.member_num = str(int(self.member_num)-1)

    def edit_content(self, content):
        self.content = content
        

def lst_function():
    lst = list()
    for i in range(1, 6):
        lst.append(i)
    for i in range(6, 11):
        lst.append(i)
    lst.remove(4)
    print(lst)
    
    
def dict_function():
    dic = dict()
    dic['Li'] = 10411234
    print(dic.get('Li'))
    print(dic.get('Lee', 0))
    
def onetoten_function():
    onetoten = list()
    for i in range(1,10):
        onetoten.append(i)
    print(onetoten)
        
def reduce1to10_function():
    from .onetoten import reduce1to10
    i=len(reduce1to10)
        if i>0:
            reduce1to10.pop(i)
            i-=1
        else:
            print("list is empty")
        
