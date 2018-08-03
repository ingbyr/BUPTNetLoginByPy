#!/usr/bin/env python
# encoding: utf-8

import argparse

import requests as requests
from lxml import etree

from app import version
from app.line_option import LineOption


class BUPTNetLogin:

    def __init__(self):
        self.ngw = "http://ngw.bupt.edu.cn"
        self.ngw_login = self.ngw + "/login"
        self.ngw_logout = self.ngw + "/logout"

    def login(self, username, password, line):
        params = {
            "user": username,
            "pass": password,
            "line": line
        }
        r = requests.post(self.ngw_login, params=params)
        self.parse_login_response(r)

    @staticmethod
    def parse_login_response(r):
        root = etree.HTML(r.text)

        errors = root.xpath("//div[contains(@class, 'error message')]")
        if len(errors):
            print("[错误]", end=" ")
            for error in errors:
                print(error.text.strip(), end="。")

        for notices in root.xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div[2]"):
            for notice in notices:
                print(notice.text.strip())

    def logout(self):
        r = requests.get(self.ngw_logout)

        if r.status_code == 200:
            print("成功注销北邮校园网网关")


def enter():
    parser = argparse.ArgumentParser(description="北邮校园网网关登陆工具")
    parser.add_argument("-l", "--login", dest="line", action="store",
                        choices={"xyw", "lt", "yd", "dx"},
                        help="登陆北邮校园网网关，LINE可用参数 xyw（校园网）、lt（联通）、yd（移动）、dx(电信)")
    parser.add_argument("-u", "--username", dest="username", action="store", help="校园网账户名称")
    parser.add_argument("-p", "--password", dest="password", action="store", help="校园网账户密码")
    parser.add_argument("-lo", "--logout", dest="logout", action="store_true", help="注销北邮校园网网关")
    parser.add_argument("-v", "--version", dest="version", action="store_true", help="版本信息")
    args = parser.parse_args()

    bnl = BUPTNetLogin()

    if args.line:
        line = LineOption[args.line.upper()].value
        if args.username and args.password:
            bnl.login(args.username, args.password, line)

    elif args.logout:
        bnl.logout()

    elif args.version:
        print(version)

    else:
        parser.print_help()


if __name__ == '__main__':
    enter()
