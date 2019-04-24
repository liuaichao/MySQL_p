# -*- coding:utf-8 -*-
import tkinter
import requests
from lxml import etree
import os
from PIL import Image, ImageTk
import time
class Book_det():
    def start(self,book_name):
        self.base = tkinter.Tk()
        self.base.geometry("600x400")
        self.base.geometry('+500+100')
        self.base.wm_title(book_name[0])
        #书名
        self.lable1 = tkinter.Label(self.base, text='书名: '+book_name[0], font=("微软雅黑", 15),anchor='w')
        self.lable1.place(x=270, y=40,width=300)
        #作者
        self.lable2 = tkinter.Label(self.base, text='作者: '+book_name[1], font=("微软雅黑", 15),anchor='w')
        self.lable2.place(x=270, y=80,width=300)
        #出版社
        self.lable3 = tkinter.Label(self.base, text='出版社: '+book_name[2], font=("微软雅黑", 15),anchor='w')
        self.lable3.place(x=270, y=120,width=300)
        #概述
        self.lable4 = tkinter.Label(self.base, text='概述: ' + book_name[3], font=("微软雅黑", 15),wraplength=300,justify='left')
        self.lable4.place(x=270, y=120, width=300)
        #图片
        self.headers = {
            'Referer': 'http://www.bookschina.com/',
            'Host': 'www.bookschina.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }
        req = requests.get(book_name[4],headers=self.headers)
        html = etree.HTML(req.text)
        self.photo_url = html.xpath('//a[@class="img"]/img/@src')[0]
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }

        with open('D:\\pythonproject\\MySQL_project\\book_photo\\'+book_name[0]+'.png','wb') as f:
            res = requests.get(self.photo_url,headers=self.headers)
            f.write(res.content)

        img = Image.open("D:\\pythonproject\\MySQL_project\\book_photo\\"+book_name[0]+'.png')  # 打开图片
        self.book_photo = ImageTk.PhotoImage(img)
        self.lable4 = tkinter.Label(self.base,image = self.book_photo)
        self.lable4.place(x=10, y=30, width=212,height=300)
        self.base.mainloop()

if __name__ == '__main__':
    a = Book_det()
    a.start(('鲁滨逊漂流记sadsfasf','刘爱超','清华大学出版社','撒的看法和卡拉地方埃里克森符合几号放假啊的爱上福建安徽课件撒低级埃里克声嘶力竭的女生空间的','http://www.bookschina.com/7424433.htm'))