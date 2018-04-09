# encoding: utf-8  
""" 
create by 'poet' on 2018/4/7 14:03 
"""
from app.libs.http_helper import HTTP
from flask import current_app

__author__ = 'poet'


class YuShuBook:
    # 模型层 MVC   M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # result json =>  python dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result
        # result text => str

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
