# -*- coding:utf-8 -*-
from mysql_demo import Mysql_demo
import random
class Book():
    #首页列表返回
    def first_book_list(self):
        datas = list()
        self.rand_num = [random.randint(830,100000) for _ in range(0,30)]
        a = Mysql_demo()
        for i in self.rand_num:
            self.sql = 'select title,author from book where _id={0};'.format(i)
            data = a.search(self.sql)
            datas.append(data[0][0]+'       '+data[0][1])
        datas = tuple(datas)
        return datas

if __name__ == '__main__':
    a = Book()
    a.first_book_list()