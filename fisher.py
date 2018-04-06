# encoding: utf-8  
""" 
create by 'poet' on 2018/4/5 14:59 
"""
__author__ = 'poet'

from flask import Flask
from helper import is_isbn_or_key

# from config import DEBUG
app = Flask(__name__)
app.config.from_object('config')  # 接受一个 模块的路径,由于 config文件 在fisher同级 ,所以直接引用


@app.route('/book/search/<q>/<page>')
def srearch(q, page):
    """
    q : 代表普通的关键字 orisbn
    page
    """
    # isbn13 13个0 到9 的数字组合
    #  isbn10 10个 0到 9 的数字组合 含有一些 '-'
    isbn_or_key = is_isbn_or_key(q)


if __name__ == '__main__':  # 入口文件确保 if 里面的 文件 只在 入口文件中执行
    # if __name__  ....  的 具体作用
    # 生产环境 nginx+ uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
