学习笔记

l = [3, 2, 3, 7, 8, 1]
l.count(3) 
2
l.index(7)
3
l.reverse()
l
[1, 8, 7, 3, 2, 3]
l.sort()
l
[1, 2, 3, 3, 7, 8]
tup = (3, 2, 3, 7, 8, 1)
tup.count(3)
2
tup.index(7)
3
list(reversed(tup))
[1, 8, 7, 3, 2, 3]
sorted(tup)
[1, 2, 3, 3, 7, 8]

这里我简单解释一下这几个函数的含义。
count(item) 表示统计列表 / 元组中 item 出现的次数。
index(item) 表示返回列表 / 元组中 item 第一次出现的索引。
list.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。
reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序，reversed() 返回一个倒转后的迭代器（上文例子使用 list() 函数再将其转换为列表）；
sorted() 返回排好序的新列表。