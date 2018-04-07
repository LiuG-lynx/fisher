# encoding: utf-8  
""" 
create by 'poet' on 2018/4/6 12:52 
"""
__author__ = 'poet'
# 将http请求封装

from urllib import request

# urllib 发送请求
# requests 发送请求 更推荐
import  requests
class HTTP:   # 封装成对象 易 拓展
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)  # r 对象里 包含信息太多,需要清洗
        # restful
        if r.status_code != 200:  #三元表达式 优化代码
            return r.json() if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

