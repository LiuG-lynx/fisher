# encoding: utf-8  
""" 
create by 'poet' on 2018/4/5 14:59 
"""
__author__ = 'poet'

from flask import Flask, make_response
# from config import DEBUG
app = Flask(__name__)
app.config.from_object('config')  # 接受一个 模块的路径,由于 config文件 在fisher同级 ,所以直接引用

@app.route('/hello')    # 兼容 用户 在访问时兼容访问
def hello():    # mvc  里的 控制器  成为 视图函数
    # 基于类的视图 (即插视图)
    '''视图函数比较关注的 几点  respons 对象中
    status code  200,404,301
    content-type http headers   http请求中的 头文件
    content-type = text/html
    默认为 text/html形式, text/plain文本格式 , appcaltion/json是 返回 json格式的 方式
    '''
    headers = {
        'content-type' : 'text/plain',
        'location': 'http://www.baidu.com'
    }
    # response = make_response('<htmxl></html>',301)  # 创建 response对象
    # response.headers = headers
    # return response  # response 返回的 第一种方式
    return '<html></html', 301, headers  # response的  第二种方式  flask 用到最多, 实质是元组 flask最终转换为 第一种的 response的 对象

# app.add_url_rule('/hello', view_func=hello)  # 路由的 注册方式 二


# app.config  就是 字典的子类

if __name__ == '__main__':  # 入口文件确保 if 里面的 文件 只在 入口文件中执行
    # if __name__  ....  的 具体作用
    # 生产环境 nginx+ uwsgi
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])