## 110道python面试题

1.一行代码实现1--100之和

`print(sum(range(1,101)))`
可以用内置函数sum()实现，sum()里面的参数是可迭代对象，将可迭代对象的元素进行累加。可以是列表、元组、集合类型。
```py
sum([1,2,3])
sum((1,2,3))
sum({1,2,3})
```

2.如何在一个函数内部修改全局变量

在函数内部用global声明，修改全局变量。global语句被用来声明变量x是全局的
```py
x = 2

def func():
    global x
    x = 4

func()
print(x)
>>>4
```

3. 列出5个python标准库

- os:提供通用的、标准的操作系统交互功能（路径操作、进程管理、环境参数）
- sys:通常用于命令行参数
- math:数学运算
- re:正则匹配
- datetime:处理日期时间

4.字典如何删除键和合并两个字典
```py
dic = {'name':'karen','age':23}
aa = {'city':'beijing'}
del dic['name']
print(dic)
>>>{'age': 23}
dic.update(aa)
print(dic)
>>>{'age': 23, 'city': 'beijing'}

```