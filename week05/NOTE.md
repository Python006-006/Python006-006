学习笔记
rabbitmq
yum install rabbitmq-server
sudo apt-get  install  rabbitmq-server
rabbitmq-plugins enable rabbitmq_management (安装插件)
 systemctl start rabbitmq-server（启动rabbitmq服务）
ps -ef |grep java
ss -ntpl |grep 5672
rabbitmqctl change_password guest mengdairA6 (修改rabbitmq密码)
rabbit 操作
停止：service rabbitmq-server stop

启动：service rabbitmq-server start

重启：service rabbitmq-server restart

查看状态：service rabbitmq-server status
