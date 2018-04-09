# encoding: utf-8  
""" 
create by 'poet' on 2018/4/5 14:59 
"""
from flask import Flask, jsonify

from app import create_app

__author__ = 'poet'

app = create_app()

if __name__ == '__main__':  # 入口文件确保 if 里面的 文件 只在 入口文件中执行
    # if __name__  ....  的 具体作用
    # 生产环境 nginx+ uwsgi
    app.run(debug=app.config['DEBUG'])
