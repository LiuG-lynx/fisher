# encoding: utf-8  
""" 
create by 'poet' on 2018/4/6 12:24 
"""
__author__ = 'poet'


# 将 判断 isbn 的 判断提取成一个函数
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    shor_word = word.replace('-', '')
    if '-' in word and len(shor_word) == 10 and shor_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
