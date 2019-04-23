# -*- coding:utf-8 -*-
import tkinter

def start():
    base = tkinter.Tk()
    base.geometry("800x500")
    base.geometry('+200+100')
    base.wm_title('网络图书管理系统')
    #提示按钮
    lable = tkinter.Label(base, text='请登录：         ', font=("微软雅黑", 18))
    lable.grid(row=1, column=1)
    #登录按钮
    Button_submit = tkinter.Button(base,text="登录",font=("隶书",18),bg='blue')
    Button_submit.grid(row=1, column=2)
    #占位
    zahnwei1 = tkinter.Label(base, text='         ', font=("微软雅黑", 18))
    zahnwei1.grid(row=1,column=3)
    #注册按钮
    Button_submit = tkinter.Button(base,text="注册",font=("隶书",18))
    Button_submit.grid(row=1, column=4)
    #分割线
    fengexian1 = tkinter.Label(base, text='——————————————————————————————————————————————————', font=("微软雅黑", 18))
    fengexian1.place(x=0,y=40,width=1000,height=10)
    #搜索框
    entry = tkinter.Entry(base, font=("隶书",22), width=20)
    entry.place(x=100,y=50,width=500,height=40)
    #搜索按钮
    Button_search = tkinter.Button(base,text="搜索",font=("隶书",18),bg='cyan')
    Button_search.place(x=620,y=50)
    base.mainloop()


if __name__ == '__main__':
    start()