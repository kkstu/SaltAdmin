#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

settings = dict(
    template_path = 'view',
    static_path = 'static',
    static_url_prefix = '/static/',
    xsrf_cookies = False,
    cookie_secret = "db884468559f4c432bf1c1775f3dc9da",
    login_url = "/login",
    debug = True,
    autoreload = True
)

db = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'saltadmin2',
    'user': 'test',
    'pass': 'test',
    'charset': 'utf8'
}