# encoding: utf-8  
""" 
create by 'poet' on 2018/4/5 14:59 
"""
import json

from yushu_book import YuShuBook
from flask import Flask, jsonify
from helper import is_isbn_or_key
__author__ = 'poet'


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
    # pycharm类中  导入的快捷Enter
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
        # dict 序列化
    return jsonify(result)  # flask 的处理方式
    # python 的 json
    # return json.dumps(result) , 200, {'content-type':'application/json'}



if __name__ == '__main__':  # 入口文件确保 if 里面的 文件 只在 入口文件中执行
    # if __name__  ....  的 具体作用
    # 生产环境 nginx+ uwsgi
    app.run(debug=app.config['DEBUG'])
