学习笔记
class Human(object):
    #静态字段
    live = True
    
    def __init__(self, name ,age):

        #普通字段

        self.name = name
        self.age = age


man = Human('Adam', 8)
woman = Human('Eve', 9)

#有静态字段live属性
print(Human.__dict__)
#有普通字段，name属性
print(man.__dict__)

#实例可以使用静态字段，也可以使用普通字段
print(man.name)
print(man.live)

woman.live = False

print(woman.live)

#类可以使用静态字段
print(Human.live)
print(woman.__dict__)
print(man.__dict__)

Human.sname= 'tainjia'



class Human(object):
    #静态字段
    live = True
    
    def __init__(self, name ,age):

        #普通字段

        self.name = name
        self.age = age


man = Human('Adam', 8)
woman = Human('Eve', 9)

#有静态字段live属性
print(Human.__dict__)
#有普通字段，name属性
print(man.__dict__)

#实例可以使用静态字段，也可以使用普通字段
print(man.name)
print(man.live)

woman.live = False

print(woman.live)

#类可以使用静态字段
print(Human.live)
print(woman.__dict__)
print(man.__dict__)

#可以为类添加静态属性
Human.sname= 'tainjia'

print(Human.__dict__)

TEST_name = Human('李四', 19)
TEST_name.sname = '22'
print(TEST_name.__dict__)

print(dir(TEST_name))
print('*'*20)
print(dir(man))
print(man.__dict__)

#内置类型不能添加属性和方法
setattr(list,  'newattr', 'value')  #相当于：list.newattr = value



