## add.py
```py
input()  # 返回的数据类型都是 String ,如果读入的数据需要进行数值运算，需要转换为 float(a) 类型，不然使用 + 符号进行的是字符串的连接。

format()  # 使用 format() 进行字符串的格式化时用 . 连接需要格式化的字符串。

x,y = y,x # 不使用临时变量，来交换变量。python的特点，可以同时赋值给多个变量。一条语句就可以完成三条语句的作用，优雅、简短。

max()   # 取一个序列中的最大值，可以是元组、列表、一串数字、一串字符
```

## 涉及到的模块
```py
# 数学复杂计算
import cmath

# 随机数
import random

# 编码字符
import unicodedata
unicodedata.numeric()   # 判断一个字符是否是数字

# 判断闰年
import calendar
print(calendar.isleap(2000))
print(calendar.isleap(2011))

# 阶乘
import math
math.factorial(4)
```

```py
# PIL 图像处理模块
from PIL import Image, ImageFilter, ImageDraw, ImageFont

# 创建图像对象
Image.new(mode,size,color)
>>>image = Image.new("RGB",(width,height),(255,255,255))

# 创建 Font 对象
# 加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。
ImageFont.truetype(file,size)
>>>font = ImageFont.truetype('Arial.ttf',36)

# 创建 Draw 对象
# 创建一个可用来对image进行操作的对象，指定操作的对象
>>>draw = ImageDraw.Draw(image)
```

## 需要注意的例子
- 带符号的温度转换：
    - 涉及到多个知识点，请熟练掌握每个知识点
- 判断数字是正数、负数、还是0：
    - 涉及到 捕获异常、跳出循环、一直执行的死循环等知识点