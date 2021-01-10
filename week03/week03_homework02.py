# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3
 
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';

Base = declarative_base()

# class Book_table(Base): 
#     __tablename__ = 'bookorm' 
#     book_id = Column(Integer(), primary_key=True) 
#     book_name = Column(String(50), index=True) 


# book_table=Table('book',metadata,
#     Column('id',Integer,primary_key=True),
#     Column('name',String(20)),
#     )

# 定义一个更多的列属性的类
# 规范写法要记得写在最上面


class Cust_table(Base): 
    __tablename__ = 'customer' 
    cust_id = Column(Integer(), primary_key=True) 
    cust_name = Column(String(15), nullable=False, unique=False)
    age = Column(Integer(),nullable=False, unique=False)
    sex = Column(String(15), nullable=False, unique=False)
    education = Column(String(15), nullable=False, unique=False)
    created_on = Column(DateTime(), default=datetime.now) 
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "Cust_table(cust_id='{self.cust_id}', " \
            "cust_name={self.cust_name}, " \
            "age={self.age}, " \
            "sex={self.sex}, " \
            "education={self.education})".format(self=self)

# 实例一个引擎
dburl="mysql+pymysql://root:mengdairA6@114.116.250.6:3306/testdb?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)


# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()



# 增加数据
cust_demo0 = Cust_table(cust_id = 1 , cust_name = '张三', age = 8, sex = '男', education = '本科')
cust_demo2 = Cust_table(cust_id = 2 , cust_name = '李四', age = 9, sex = '女', education = '研究生')
cust_demo3 = Cust_table(cust_id = 5 , cust_name = '王五', age = 10, sex = '人妖', education = '博士')
cust_demo4 = Cust_table(cust_id = 6 , cust_name = '王五', age = 10, sex = '人妖', education = '博士')

# 增加多条数据
session.add(cust_demo0)
session.add(cust_demo2)
session.add(cust_demo3)
session.add(cust_demo4)
session.commit()
# session.flush()

# 使用迭代代替all()
result = session.query(Cust_table).all()
print(result)

# for result in session.query(Cust_table):
#     print(result)

# result_first = session.query(Cust_table).first()
# print(result_first)
# one() 
# scalar()

# 指定列数
result_name = session.query(Cust_table.cust_name).first()
print(result_name)

session.commit()