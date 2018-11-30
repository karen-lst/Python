### 多线程、泛型

```c#
//Program.cs  line-32
private Object thisLock = new Object();
```

- 涉及到的知识点
    + 泛型（Generic）
    + lock()用法
    + 多线程

- Object就是泛型，什么数据类型都可以装，是所有类的基类，在面向对象编程中俗称装箱、拆箱。

- lock( ){ },把 { } 中的代码段锁定，防止多个线程同时运行该代码段。如果有线程在操作 { } 中的代码，那么thislock就会被占用，如果这时候有其他线程想访问，则排队等待，等前一个访问使用完成再访问。
    + lock主要用于处理并发问题，锁定独占对象。

### 实例化、类

```c#
//Program.cs  line-41
Program program = new Program();
```

- 涉及到的知识点
    + 实例化
    + 类

- 实例化Program类，为program对象。   对象具有类的属性，可以调用类的方法。
- 一般当建立了一个类，其实只是建立了一个模型，就比如是你只是做了一个蛋糕的模子，还不是真正的蛋糕。而Program program = new Program()其实就是用Program这个蛋糕模子来做一个蛋糕 P，P就是一个完成好的蛋糕了。

### 命令行

```c#
//Program.cs  line-43
string[] parameters = System.Environment.GetCommandLineArgs();
```

- 涉及到的知识点
    + 命令行
    + 参数

- 获取命令行参数

```c#
//举个简单例子，比如说你在系统的命令提示符（也就是CMD下）输入这样的东西运行（假定你的程序叫myapp.exe）
myapp.exe   a1 b2 c3
//那么Environment.GetCommandLineArgs长度则为4
[0]为myapp.exe，[1]为a1，[2]为b2
//如果直接输入myapp.exe或者是双击运行这myapp，则 GetCommandLineArgs长度为1
[0]即为myapp.exe
```

### 反射

```c#
//Program.cs  line-53
string project = parameters.GetValue(1).ToString();
```
- 反射技术的简单操作（读取和设置类的属性）



### 类型转换

```c#
//Program.cs  line-54
program.ftp_StartNum = Convert.ToInt32(parameters.GetValue(2));
```
- 将字符串转换成数字
```c#
//方法
Convert.ToInt32（string value,int fromBase）
//fromBase为进制（2，8，10，16）
//如：将2进制（string）转换成10进制（int）
string strBase2="0101";
int intBase10=Convert.ToInt32(strBase2,2);
-->5
```
