# -*- coding:utf-8 -*-
import tkinter
import t_user
from t_register import T_register
from mysql_demo import Mysql_demo
from book_list import Book
from book_det import Book_det
class MN():
    def __init__(self):
        self.book = Book()
        pass
    def start(self):
        self.base = tkinter.Tk()
        self.base.geometry("800x500")
        self.base.geometry('+200+100')
        self.base.wm_title('网络图书管理系统')
        # 提示按钮
        self.lable = tkinter.Label(self.base, text='   请登录：         ', font=("微软雅黑", 18))
        self.lable.place(x=0, y=0, width=150, height=50)
        # 登录按钮
        self.Button_submit = tkinter.Button(self.base, text="登录", font=("隶书", 18), bg='blue', command=self.t_submit)
        self.Button_submit.place(x=200, y=10, width=50, height=30)
        # 注册按钮
        self.Button_register = tkinter.Button(self.base, text="注册", font=("隶书", 18), command=self.register)
        self.Button_register.place(x=300, y=10, width=50, height=30)
        # 分割线
        self.fengexian1 = tkinter.Label(self.base, text='——————————————————————————————————————————————————', font=("微软雅黑", 18))
        self.fengexian1.place(x=0, y=40, width=1000, height=10)
        # 搜索框
        self.entry = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry.place(x=100, y=50, width=500, height=40)
        # 搜索按钮
        self.Button_search = tkinter.Button(self.base, text="搜索", font=("隶书", 18), bg='cyan')
        self.Button_search.place(x=620, y=50)
        # 列表
        self.var = tkinter.StringVar()
        global lb
        self.lb = tkinter.Listbox(self.base, listvariable=self.var,font=("隶书", 12))
        self.list_item = [i for i in range(1,31)]
        for item in self.list_item:
            self.lb.insert(tkinter.END, item)

        #设置list的值
        self.var.set((self.book.first_book_list()))
        self.lb.bind('<ButtonRelease-1>', self.print_item)
        self.scrl = tkinter.Scrollbar(self.base)
        self.scrl.place(x=600, y=100, height=340)
        self.lb.configure(yscrollcommand=self.scrl.set)
        self.lb.place(x=20, y=100, width=580, height=340)
        self.scrl['command'] = self.lb.yview
        self.base.mainloop()


    # 事件绑定
    def print_item(self,event):
        self.book_name = (self.lb.get(self.lb.curselection())).split('       ')[0]
        #根据book_name查找
        self.my_s = Mysql_demo()
        self.sql_s = 'select title,author,publisher,recolagu,href,drop_type from book where title="{0}";'.format(self.book_name)
        self.book_data = self.my_s.search(self.sql_s)
        self.bde = Book_det()
        self.bde.start(self.book_data)
    def m(self):
        self.lable.destroy()

    # 登录
    def submit(self):
        s = t_user.T_submit()
        s.t_submit()



    # 注册
    def register(self):
        r = T_register()
        r.register()




    def t_submit(self):
        self.bases = tkinter.Tk()
        self.bases.geometry("300x400")
        self.bases.geometry('+500+100')
        self.bases.wm_title('登录')
        # 提示
        self.lable1 = tkinter.Label(self.bases, text='电 话', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 手机号输入框
        self.entry1 = tkinter.Entry(self.bases, font=("隶书", 22), width=20)
        self.entry1.place(x=70, y=15, width=220, height=40)
        # 提示
        self.lable2 = tkinter.Label(self.bases, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        # 密码输入框
        self.entry2 = tkinter.Entry(self.bases, font=("隶书", 22), width=20, show="*")
        self.entry2.place(x=70, y=65, width=220, height=40)
        # 登录按钮
        self.Button1 = tkinter.Button(self.bases, text="登录", font=("隶书", 18), bg='cyan', command=self.t_is_submit)
        self.Button1.place(x=50, y=140, width=200)
        # 用户登录按钮
        self.Button2 = tkinter.Button(self.bases, text="用户登录", font=("隶书", 10), state=tkinter.DISABLED)
        self.Button2.place(x=30, y=350, width=55)
        # 学生登录按钮
        self.Button3 = tkinter.Button(self.bases, text="学生登录", font=("隶书", 10), command=self.t_std_submit)
        self.Button3.place(x=200, y=350, width=55)
        self.bases.mainloop()

    # 学生登陆
    def t_std_submit(self):
        self.lable1.destroy()
        self.lable2.destroy()
        # 提示
        self.lable1 = tkinter.Label(self.bases, text='学 号', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 提示
        self.lable2 = tkinter.Label(self.bases, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        self.Button2['state'] = tkinter.NORMAL
        self.Button3['state'] = tkinter.DISABLED
        self.Button2['command'] = self.t_submit

    # 登录按钮函数
    def t_is_submit(self):

        self.id = self.entry1.get()
        self.pwd = self.entry2.get()
        self.to_mysql()

    # 数据库查询
    def to_mysql(self):
        if self.id == '' or self.pwd == '':
            self.hnt = tkinter.messagebox.showerror('错误', '请输入账号密码')
        else:
            self.my = Mysql_demo()
            self.sql = 'select name from user where id="{0}" and pwd="{1}";'.format(self.id, self.pwd)
            self.name = self.my.search(self.sql)
            if self.name != False:
                self.hnt = tkinter.messagebox.showinfo('提示', '登录成功,欢迎,{0}'.format(self.name[0][0]))
                self.bases.destroy()
                #登录后变化
                self.lable.destroy()
                self.Button_submit.destroy()
                self.Button_register.destroy()
                self.lable = tkinter.Label(self.base, text='欢迎，{0}'.format(self.name[0][0]), font=("微软雅黑", 18))
                self.lable_title = tkinter.Label(self.base,text='Welcome Book World',font=("微软雅黑", 18),fg='orange')
                self.lable_title.place(x=0,y=0)
                self.lable.place(x=300, y=0, width=200, height=40)


            else:
                self.hnt = tkinter.messagebox.showerror('错误', '账号或密码出错了')
        # 登陆后变化

    # def after_submit(self):
    #
    #     self.lable.destroy()
    #     self.Button_submit.destroy()
    #     self.Button_register.destroy()
    #     self.lable = tkinter.Label(self.base, text='欢迎，{0}'.format(self.name[0][0]), font=("微软雅黑", 18))
    #     self.lable.place(x=200, y=0, width=200, height=50)

if __name__ == '__main__':

    lb = ''
    a = MN()
    a.start()


