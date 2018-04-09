# encoding: utf-8  
""" 
create by 'poet' on 2018/4/5 20:58 
"""
__author__ = 'poet'

# 建议 配置文件里面的参数都大写
DEBUG = True
# 不放到 git中
# 数据库 密码，账号， flask——app key  机密信息放在secure文件，
# 生产环境与 开发环境的区别，都写到 secure里面
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/fisher'