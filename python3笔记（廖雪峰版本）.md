### 输出
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
```

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
    + 定义genertor的另一种方法：如果一个函数包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个genertor。
    + genertor和函数的执行流程不一样，函数时顺序执行，遇到return语句后者最后一行函数语句就返回。而genertor在每次调用next()的时候执行，遇到yield语句返回，再次执行时，从上次返回的yield语句处继续执行。
    + 使用for循环调用genertor时，如果想要拿到return语句的返回值，就必须捕获StopIteration错误，返回值包含在StopIteration的value中：
```py
def num(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n += 1
    return 'done'
b = num(3)
print(next(b))
print(next(b))
print(next(b))
>>>1
>>>1
>>>2

b = num(4)
while True:
	try:
		x = next(b)
		print('b:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
```

##### 迭代器
- 可以直接作用于for循环的数据类型有：
	+ 集合数据类型：list、tuple、dict、set、str
	+ generator：生成器、带yield的函数
- 可直接作用于for循环的对象统称为：可迭代对象(Iterable)
- 可使用isinstance()判断一个对象是否是Iterable对象
- 可以被next()函数调用并不断返回下一个值得对象统称为迭代器：Iterator
- 生成器都是迭代器对象，list、dict、str虽然是可迭代对象，却不是迭代器。可以使用iter()函数，将可迭代对象变成迭代器。`isinstance(iter([]), Iterator)`
- python的迭代器对象表示的是一个数据流，我们不能提前知道序列的长度，只能不断通过next()函数计算出下一个数据，所以迭代器的计算是惰性的。只有在需要返回下一个数据时，它才会计算。
- python的for循环本质上就是通过不断调用next()函数实现的

### 函数式编程
- 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言
编写的函数没有变量，任意一个函数，只要输入是确定的，输出就是确定的。这种纯函数我们称之为没有副作用。
- 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
- 函数式编程的特点：允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
- Python 对函数式编程提供部分支持。由于 Python 允许使用变量，因此，Python 不是纯函数式编程语言。

##### 高阶函数
- 变量可以指向函数（函数本身也可以赋值给变量）
- 函数名也是变量，函数名就是指向函数的变量
- 一个函数可以接收另一个函数作为参数，这种函数就称为高阶函数，函数式编程就是指这种高度抽象的编程范式
```py
def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))
>>>11
```

##### map/reduce
- map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator 返回。
```py
def f(x):
    return x**2

g = map(f,[1,2,3,4,5,6,7,8,9])
print(list(g))
# g 是一个迭代器，是一个惰性序列，通过list()函数，把迭代器整个序列都计算出来，并返回一个list

g = map(str,[1,2,3,4,5,6,7,8,9])
print(list(g))
# 把list里面的所有数字转换成字符串
```
- reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce 把结果和序列的下一个元素再传入函数做累计计算。`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`
```py
from functools import reduce
def add(x,y):
    return x*10 +y

g = reduce(add,[1,2,3,4,5,6])
print(g)
# 累加

def normalize(name):
    return name.capitalize()

print(list(map(normalize,['adam', 'LISA', 'barT'])))
# 规范英文名
```

##### filter
- python 内建的filter()函数用于过滤序列。和map()类似，但和map()不同的是。
- filter()把传入的函数依次作用于每个元素，根据函数返回值是True还是False决定保留还是丢弃该元素。
- filter()这个高阶函数，关键在于正确实现一个“筛选”函数。返回的也是一个迭代器，需要有list()函数获得所有结果并返回list。
```py
def is_odd(s):
    return s%2==1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))
>>>[1, 3, 5, 7, 9]
# 在一个list中只保留奇数，删掉偶数

def is_pa(n):
    s = str(n)
    if s == s[::-1]:
        return True

print(list(filter(is_pa,range(1,1000))))
# 利用filter()过滤掉非回数
```

##### sorted
- python内置的sorted()函数可以对list进行排序。此外，sorted()函数还是一个高阶函数，可以接受key函数来实现自定义的排序。
- key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序。
- 如果要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
```py
sorted([36, 5, -12, 9, -21], key=abs)
>>>[5, 9, -12, -21, 36]

from operator import itemgetter
L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
```

##### 返回函数
- 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。当返回的函数被调用时，才真正计算函数结果。
- 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
- 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数。
- 返回闭包时牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量

##### 匿名函数
- 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
- 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
- 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
- Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。

##### 装饰器

##### 偏函数
- Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
- int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
```py
int('12345')
>>>12345
```
- 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
```py
int('12345', base=8)
>>>5349
int('12345', 16)
>>>74565
```
- functools.partial就是帮助我们创建一个偏函数的。
```py
import functools
int2 = functools.partial(int, base=2)
int2('1000000')
>>>64
```
- 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

### 模块
- Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。以内建的sys模块为例，编写一个hello的模块：
```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```
- 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
- 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
- 第6行使用__author__变量把作者写进去,以上就是Python模块的标准文件模板

##### 作用域
- 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
- 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
- Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
- private函数或变量不应该被别人引用，那它们有什么用呢？
	+ 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了
	+ 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
```py
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

### 面向对象编程
- 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
- 数据封装、继承和多态是面向对象的三大特点。
```py
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```

##### 类和实例
- 在Python中，定义类是通过class关键字
- class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
- 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
- 可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法
- `__init__方法`的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

###### 数据封装
- 我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
- 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
- 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
- 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。