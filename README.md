# BUPTLogin
![](https://img.shields.io/badge/version-0.1.0-green.svg)
![](https://img.shields.io/github/stars/ingbyr/BUPTNetLogin.svg)
![](https://img.shields.io/github/forks/ingbyr/BUPTNetLogin.svg)
![](https://img.shields.io/github/issues/ingbyr/BUPTNetLogin.svg)

北邮校园网网关登陆工具，适配新网关 ngw.bupt.edu.cn


## 安装
- 使用pip安装   `pip3 install BUPTNetLogin`

- 使用便携版 [下载页面](https://github.com/ingbyr/BUPTNetLogin/releases)

## 使用方法
使用命令 `bnl`

```shell
user@server ~> bnl
usage: bnl [-h] [-l {dx,xyw,lt,yd}] [-u USERNAME] [-p PASSWORD] [-lo] [-v]

北邮校园网网关登陆工具

optional arguments:
  -h, --help            show this help message and exit
  -l {dx,xyw,lt,yd}, --login {dx,xyw,lt,yd}
                        登陆北邮校园网网关，LINE可用参数 xyw（校园网）、lt（联通）、yd（移动）、dx(电信)
  -u USERNAME, --username USERNAME
                        校园网账户名称
  -p PASSWORD, --password PASSWORD
                        校园网账户密码
  -lo, --logout         注销北邮校园网网关
  -v, --version         版本信息
```

登陆联通网络举例：
```shell
user@server ~> bnl -l lt -u 用户名 -p 密码
```

注销网络举例
```shell
user@server ~> bnl -lo
```


## 更新
```html
pip3 install BUPTNetLogin --upgrade
```


## 依赖库
使用pip将自动安装以下库：
- requests
- lxml


## 自行编译便携版
- win: `.\venv\Scripts\pyinstaller -n bnl --noupx -c -F .\app\bupt_net_login.py`
- linux: `./venv/bin/pyinstaller -n bnl --noupx -c -F ./app/bupt_net_login.py`


> 更多请前往 [个人博客](https://www.ingbyr.com)