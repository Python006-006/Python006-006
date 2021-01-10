学习笔记
linux:
arch ：查看操作系统
安装mysql：
查看内核版本命令：
cat /proc/version
rpm -Uvh http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
rpm -Uvh http://dev.mysql.com/get/mysql57-community-release-el6-3.noarch.rpm
https://repo.mysql.com//mysql80-community-release-el6-3.noarch.rpm
rpm -Uvh https://dev.mysql.com/downloads/repo/yum/mysql80-community-release-el6-3.noarch.rpm

yum -y install mysql-community-server

wget dev.mysql.com/get/mysql80-community-release-el6-1.noarch.rpm

rpm -Uvh dev.mysql.com/get/mysql80-community-release-el6-1.noarch.rpm

systemctl start mysql.service
systemctl enable mysqld
systemctl status mysqld.service

查看字符集
show variables like '%character%';
show variables like 'collation_%';
注意：mysql 中的字符集是utf8 和utf-8 是不一样的
修改配置文件
vim /etc/mysql/my.cnf
在命令模式下输入
:set nu
或者
:set number
都可以为vi设置行号，如果要取消的话，则输入
:set nonu
行号的设置是vi的环境设置，不会影响文本的内容。

systemctl restart mysql


开启远程连接数据库服务：
1.首先编辑文件/etc/mysql/mysql.conf.d/mysqld.cnf：''or''my.cnf
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
进入编辑页面，此时输入/bind    当出现bind-address    = 127.0.0.1时，按一下回车,此时按下键盘上的‘i’,当右下角出现:”--INSERT--”此时在bind-address    = 127.0.0.1 最前面输入#
在my.cnf中加上skip-name-resolve
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mengdairA6' WITH GRANT OPTION;
service mysql restart
