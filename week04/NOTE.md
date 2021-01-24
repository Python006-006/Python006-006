学习笔记
1. Django 安装
Pip isntall  （or） --Upgrade Django== 2.2.13(注意：‘==’前后不能有空格)
Upgrade Django == 
(w)Python –m  venv  venv_01
(w)激活： activate.bat
(w)激活： deactivate.bat

2. 解决VSCODE ”无法加载文件Activate.ps1，因为在此系统上禁止运行脚本报错“的问题
https://www.ttkf.cn/439.html
win + x 以管理员身份运行PowerShell
输入set-executionpolicy remotesigned，设置成Y即可
分析原因：
     Windows PowerShell默认是Restricted（防止运行没有数字签名的脚     本），要设置成remotesigned模式
解决方法：
以管理员身份运行 PowerShell，并输入 set-executionpolicy remotesigned ,再输入“y”如图：
再次返回到VsCode中就可以使用虚拟环境库
Vc_code:格式代码
vs code格式化代码的快捷键如下：（来源于这里）
Windows    Shift + Alt + F
Mac            Shift + Option + F
Ubuntu       Ctrl + Shift + I
Alt  + 上下键 ：上下换行
Ctrl + / ： 注释
3. 创建Django项目:
创建django项目：Django-admin  startproject   XXX(自定义项目名称，如：MyDjango)
Cd XXX 
Python mange.py help 
创建app：Python  manage.py  startapp   XXX(自定义)
运行django ：python   manage.py  runserver  XXXXX:xx(自定义地址和端口)
推出 django 服务：Ctrl + c
