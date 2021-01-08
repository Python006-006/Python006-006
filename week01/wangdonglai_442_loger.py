# --*-- encoding:utf-8 --*--
import logging
import os.path
import time
from pathlib import Path

project_path = 'python-' 

current_time=time.strftime('%Y%m%d%H%M',
                           time.localtime(time.time()))  # 返回当前时间
print(current_time)
current_path=os.path.dirname(os.path.abspath(project_path))  # 返回当前目录

print(current_path)

path1=current_path.split(project_path)  #指定分隔符对字符串进行切片
print(path1)
path2=[path1[0], project_path]
print(path2)
path3=''
new_name=path3.join(path2) + '/var/log/' #在该路径下新建下级目录

dir_time = time.strftime('%Y%m%d', time.localtime(time.time()))  #返回当前时间的年月日作为目录名称
log_filename = new_name + dir_time + '/' + 'test.log'
print(log_filename) 
isExists=os.path.exists(new_name + dir_time)   #判断该目录是否存在
if not isExists:
    os.makedirs(new_name + dir_time)
    print(new_name + dir_time + "目录创建成功")

else:
            # 如果目录存在则不创建，并提示目录已存在
    print(new_name + "目录 %s 已存在" % dir_time)

#配置log config
logging.basicConfig(filename = log_filename,
                    level= logging.DEBUG ,
                    datefmt= '%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name) -8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                    )

#编辑函数
def removeDuplicates01(nums):
    if len(nums) == 0:
        print(nums)
        return 0
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    print(nums)
    return j + 1
#运行函数并输出日志
try:
    removeDuplicates01(2)
except TypeError:
    logging.debug("There is a error in this file",exc_info=1)
    logging.info("There is a error in this file",exc_info=1)
    logging.warning("There is a error in this file",exc_info=1)
    logging.error("There is a error in this file",exc_info=1)
    logging.critical("There is a error in this file",exc_info=1)