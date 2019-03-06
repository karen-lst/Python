<<<<<<< HEAD
- 输出
=======
### 输出
>>>>>>> 9622d146cd1a5fc2989cfdf0a5e8b8ca051e0388
- print('')里面用逗号隔开，可以输出多个字符串，输出形式中，逗号变成空格
- 多行输出可以用`'''  '''`。

### 布尔类型
- 布尔值可以用 `and or not` 运算

### 空值
- 空值是一个特殊的值，用 `None` 表示，不能理解为 0 ，0 是有意义的，`None` 是一个特殊的空值

### 常量
- python中习惯上用全部大写的变量名表示常量

### 除法运算
- `/` 除法计算结果永远为浮点数，哪怕两个数能整除，结果仍为浮点数
- `//` 地板除，结果永远为整数，哪怕除不尽，结果也为整数
- `%` 取余，计算结果取余数

### 赋值
- python支持多种数据类型，在计算机内部，每一个数据都存储在一个内存地址中，变量就是指向这些地址，对变量赋值就是把变量指向对应数据的内存地址。

### 数值
- python的整数、浮点数没有大小限制，超过一定限制就表示为 `inf` 无限大。

### 列表
- `append()` 追加元素到列表的末尾
- `insert()` 把元素插到指定位置
- `pop()` 删除列表末尾的元素，或者 `pop(i)` 删除指定索引的位置


### 元组
- 当定义一个元组时，元组的元素就必须被确定下来，不可再更改
- 只有一个元素的元组必须在元素后面加一个逗号，消除歧义。因为 `(1)` 也可以表示为数学计算中的小括号运算

- 判断
```py
if x:
	pass
# 只要 X 是非零数值、非空字符串、非空列表，就判断为 True , 否则为 False
```

### 循环
- python中有两种循环，一种是 `for ... in `，依次把 list 或 tuple 中的每个元素迭代出来
	- python提供 `range()` 函数，可以生成一个整数序列，序列从0开始
- 一种是`while()`循环，只要条件满足就不断循环
- 在循环中，`break` 语句可以提前退出循环；`continue` 跳出当前循环
- 当程序陷入死循环时，可以按 `Ctrl+C` 退出程序

### 字典
- 字典具有极快的查找速度，不会随着字典大小的增加而变慢，使用键-值存储。key 值唯一，是不可变对象。
- 判断 `key` 是否存在：
	- 通过 `in ` 判断
	- 通过 `get()` 判断，如果不存在，返回 `None`
- 删除一个 `key`：
	- `pop(key)` :对应的 `value` 也会被删除
- 与列表相比字典的优缺点：
	- 查找和插入的速度极快、不会随着 key 值的增加而变慢
	- 需要占用大量的内存，内存浪费多
- 列表则相反：
	- 查找和插入的速度随着元素的增加而变慢
	- 占用内存小，浪费内存很少
- 字典可以用在需要告诉查找的很多地方，在python代码中，无处不在，正确使用字典非常重要。
- 通过 key 计算位置的算法叫 哈希算法 。要保证 key 值不能变，而python中 字符串、整数 是不可变的，所以可以作为 key。
```py
d.get(key)  如果 key 不存在，返回 None ，或者返回指定的一个 value
```


### 集合
- set 也是一组有 key 的集合，但是不存储 value，由于 key 不能重复，所以，在集合中，没有重复的元素。
- 重复元素在集合中被自动过滤
```py
add(key)  可以添加元素到set
remove(key)  可以删除元素

```

### 函数
```py
# 求绝对值的函数
abs()

# 返回最大值
max()

# 数据类型转换函数
int()、float()、str()、bool()

# 把一个整数转换成十六进制表示的字符串
hex()
```
- 当传入函数的参数数量、或参数类型不对时，会报出 `TypeError` 错误
- 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，然后由这个变量指向函数对象，相当于给这个函数起了一个“别名”
```py
a = abs
a(-1)
```
- 函数内部的语句在执行到 `return` 语句时，函数就执行完毕，并将结果返回了。
- 如果没有 `return` 语句，函数执行完毕也会返回结果，只是结果为 `None` 。
- 函数返回多个值时，实际上返回的是一个 `Tuple`。多个位置可以同时接收一个 `tuple`，按位置赋给对应的值。

##### 函数的参数
- 位置参数
<<<<<<< HEAD
- 默认参数：默认参数必须指向不变对象，如果改变了默认参数的内容，那么下一次调用时，就不再是函数定义时默认的内容了。
```py
def app_end(l=[]):
	l.append('END')
	return l

print(app_end())
>>>['END']
print(app_end())
>>>['END','END']

# 因为列表是可变的，列表对象的内容被改变了，而 l 又还是指向了同一个列表对象，所以默认参数的内容就变了。
# 可以将列表换成 None

def app_end(l=None):
	if l is None:
		l = []
	l.append('END')
	return l
```
- 可变参数：
	- 在参数前面加一个 `*` 号，表示传入的参数个数是可变的。
	- python允许在列表和元组前面加一个`*`号，把list、tuple的元素变成可变参数传进去
	- 允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple
```py
def calc(*number):
	sum = 0
	for i in number:
		sum += i ** 2
	return sum
```
- 关键字参数：
	- 关键字允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
	- 关键字参数可以扩展函数的功能
	- `**extra` 表示把 `extra` 这个 dict 的所有 key-value 用关键字参数传入到函数的 `**kw` 参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
```py
def person(name,age,**kw):
    print('name:',name,'age:','other:',kw)


person('asd',43)
person('asd',43,city='beijing')
person('asd',43,city='beijing',job='engineer')
>>>name: asd age: other: {}
>>>name: asd age: other: {'city': 'beijing'}
>>>name: asd age: other: {'city': 'beijing', 'job': 'engineer'}

# 也可以这样
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('jack',43,**extra)
```

##### 递归函数
- 如果一个函数在内部调用自身，这个函数就是递归函数
- 递归函数的优点是：定义简单、逻辑清晰。
- 理论上，所有递归函数都能写成循环的方式，但是循环的逻辑没有递归清晰
- 使用递归函数时，需要防止栈溢出，在计算机中，函数调用时通过栈（stack）实现的。每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小是有限制的，所以，递归调用的次数太多，会导致栈溢出。
	- 解决栈溢出的办法就是：通过 尾递归 优化。事实上，尾递归和循环的效果是一样的。所以，可以把循环看成是一种特殊的尾递归函数。
	- 尾递归是指，在函数返回的时候，调用自身本身，并且，return 语句不能包含表达式。这样，解释器就可以把尾递归做优化，使递归无论调用多少次，都只占用一个栈帧，就不会出现栈溢出的情况。
	- 大多数编程语言没有针对尾递归做优化，python解释器也没有，所以，即使把上面的函数改成尾递归方式，也会导致栈溢出。任何递归函数都存在栈溢出的问题。
```py
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
=======
- 默认参数

### python语言的高级特性
- python开发的准则：代码越少越好、越简单越好。1行代码能实现的功能，绝不写5行代码。代码越少，开发效率越高。

##### 切片
字符串、列表、元组，都可以使用切片操作，切片非常灵活，一行代码可以实现多行循环才能完成的操作。

##### 迭代
给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历，我们称为迭代。
    + python的for循环抽象程度要高于java的for循环，因为python的for循环不仅可以用在list、tuple上，还可以作用在其他可迭代对象上。
    + 任何可迭代对象，都可以作用于for循环（包括我们自定义的数据类型）。
    + 只要符合迭代条件，可以使用for循环。比如：dict、字符串。
        * 因为dict的存储不是按照list的方式顺序排列，dict是无序的，所以，迭代出来的结果顺序可能不一样。
        * 默认情况下，dict迭代的是key，如果要迭代value，如下。如果要同时迭代key、value，如下。
        * 字符串也是可迭代对象，因此也可以作用于for循环
```py
d = {'a':1,'b':3,'c':4}

# 默认情况
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 迭代key、value
for k,v in d.items():
    print(k,v)
```
    + 如何判断一个对象是否是可迭代对象：通过 `collections` 模块的 `Iterable` 类型判断。如下。
    + 可以用python内置的 `enumerate` 函数把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
```py
from collections import Iterable

print(isinstance('adafa',Iterable))
print(isinstance([1,2,5],Iterable))
print(isinstance((1,5,6),Iterable))
print(isinstance(15654,Iterable))

for i,value in enumerate(['A','B','C']):
    print(i,value)
```

##### 列表生成式
- 列表生成式，是python内置的非常简单却强大的，可以用来创建list的生成式。最外层用 `[ ]` ，后面可以加上if判断，还可以使用双层循环。
- for循环其实可以同时使用两个甚至多个变量，比如dict的items()，可以同时迭代key、value。列表生成式也可以使用两个变量来生成list。
```python
print([x**2 for x in range(10)])
print([x**2 for x in range(10) if x%2 ==0])
print([x+y for x in 'ABD' for y in 'dfg'])
>>>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>[0, 4, 16, 36, 64]
>>>['Ad', 'Af', 'Ag', 'Bd', 'Bf', 'Bg', 'Dd', 'Df', 'Dg']

d = {'a':'34','f':'45','g':'67'}
print([k + '=' + v for k, v in d.items()])
>>>['a=34', 'f=45', 'g=67']

s = ['ASD','DSF','F','IH']
print([x.lower() for x in s])
>>>['asd', 'dsf', 'f', 'ih']

L = ['hello','WORLD',4564,'PONY',None]
print([i.lower() for i in L if isinstance(i,str)])
>>>['hello', 'world', 'pony']
```

##### 生成器
- 列表的容量是有限的，创建一个包含100万个元素的列表，会占用很大的存储空间，如果仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
- 如果列表元素可以按照某种算法推算出来，那我们就能在循环的过程中不断推算出后面的元素，这样就不必创建完整的list，从而节省大量的空间。
- 在python中，这种一边循环一边计算的机制，称为生成器：`generator`
- 如何创建一个生成器：
    + 第一种方法：只要把列表生成式的`[ ]` 改成 `( )` 就创建了一个 `genertor` 。使用for循环来迭代 `genertor`，就能不断获取下一个值。不会出现调用 `next()` 到最后一个元素时跳出 `StopIteration` 错误。
```py
g = (x ** 2 for x in range(1,6))
for i in g:
    print(i,end=',')
>>>1,4,9,16,25,
```
    + 如果推算的算法比较复杂，用类似列表生成式for循环无法实现时，还可以用函数实现。
```py
def num(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n += 1

b = num(3)
print(next(b))
print(next(b))
print(next(b))
>>>>>>> 9622d146cd1a5fc2989cfdf0a5e8b8ca051e0388
```