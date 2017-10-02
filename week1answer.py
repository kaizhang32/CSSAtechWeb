#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:48:17 2017

@author: jackylee
"""


class User:
    def __init__(self, username, password, info):
        self.username = username
        self.password = password
        self.info = info
        
    def show_info(self):
        userinfo = "用户名：%s\n" % self.username
        userinfo += "密码：%s\n" % self.password
        userinfo += "个人信息：%s" %self.info
        print(userinfo)
        
    def edit_info(self, info):
        self.info = info
        

class Activity:
    # member_num 这个参数可以设置默认
    def __init__(self, title, content, date, member_num=0):
        self.title = title
        self.content = content
        self.date = date
        self.member_num = str(member_num)
    
    def add_member(self):
        self.member_num = str(int(self.member_num)+1)
        '''
        也可以写成如下，方便理解：
        number = int(self.member_num) + 1
        self.member_num = str(number)
        '''
        
    def reduce_member(self):
        self.member_num = str(int(self.member_num)-1)
        '''
        也可以写成如下，方便理解：
        number = int(self.member_num) - 1
        self.member_num = str(number)
        '''

    def edit_content(self, content):
        self.content = content
        

def lst_function():
    lst = list()
    # for循环要会写
    for i in range(1, 6):
        lst.append(i)
    for i in range(6, 11):
        lst.append(i)
    lst.remove(4)
    print(lst)
    
    
def dict_function():
    dic = dict()
    dic['Li'] = 10411234
    # 学会使用dict.get()方法
    print(dic.get('Li'))
    
    # 如果不存在的话，这样做就不会报错
    print(dic.get('Lee', 0))
    
        