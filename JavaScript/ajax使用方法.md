## Ajax ( Asynchronous Javascript And XML )
- 定义：异步的JavaScript和XML，一种创建交互式网页应用的网页开发技术。一种用于创建快速动态网页的技术。
- 特点：
    - Ajax 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。
    - 通过在后台与服务器进行少量数据交换，Ajax 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。
    - 传统的网页（不使用 Ajax）如果需要更新内容，必须重载整个网页页面。
    - Ajax不是一种新的编程语言，而是一种用于创建更好更快以及交互性更强的Web应用程序的技术。

### Ajax应用
- 运用 XHTML+CSS 来表达资讯
- 运用 JavaScript 操作 DOM（Document Object Model）来执行动态效果
- 运用 XMLHttpRequest 或 新的Fetch API 与网页服务器进行异步资料交换
- 运用 XML和XSLT 操作资料

### Ajax工作原理

![avatar](../images/ajax工作原理.jpg)

Ajax是基于现有的Internet标准，并且联合使用

- XMLHttpRequest 对象 (异步的与服务器交换数据)
- JavaScript/DOM (信息显示/交互)
- CSS (给数据定义样式)
- XML (作为转换数据的格式)

### 创建 XMLHttpRequest 对象
XMLHttpRequest 是Ajax的基础。

- XMLHttpRequest对象
    + 所有现代浏览器均支持 XMLHttpRequest 对象（ IE5和IE6使用ActiveXObject ）
    + XMLHttpRequest 用于在后台与服务器交换数据
```js
// 创建 XMLHttpRequest 对象的语法：
variable = new XMLHttpRequest();

// 老版本IE5和IE6使用 ActiveX 对象：
variable = new ActiveXObject("Microsoft.XMLHTTP");

// 为了适应所有的现代浏览器，先检查浏览器是否支持XMLHttpRequest对象，
// 如果支持就创建XMLHttpRequest对象，如果不支持就创建ActiveXObject。
```

## 向服务器发送请求
- 如需将请求发送到服务器，我们使用XMLHttpRequest对象的open()和send()方法
```js
xmlhttp.open("GET","ajax_info.txt",true);
xmlhttp.send();

//方法、描述
open(method,url,async)      //规定请求的类型、URL以及是否异步处理请求。
//method: 请求的类型: GET 或 POST；
//url: 文件在服务器上的位置；
//async: true(异步) 或 false(同步)

send(string)        //将请求发送到服务器
//string: 仅用于POST请求
```

### GET 和 POST 的区别
- GET的优点: 与 POST 相比，GET更简单更快，在大部分情况下都能用。
- 但是在以下情况中，请使用 POST:
    + 无法使用缓存文件( 更新服务器上的文件或数据库 )
    + 向服务器发送大量数据( POST没有数据量的限制 )
    + 发送包含未知字符的用户输入时，POST 比 GET 更稳定可靠，更安全。

##### GET、POST请求
- 为避免 GET 请求可能得到缓存的结果，可以向 URL 添加一个唯一的ID
```js
xmlhttp.open("GET", "/try/ajax/demo_get.php?t="+Math.random(), true);
xmlhttp.send();

//用 GET 方法发送信息，可以在 URL 中添加信息
xmlhttp.open("GET", "/try/ajax/demo_get2.php?fname=Henry&lname=Ford", true);
xmlhttp.send();
```
- POST 请求
```js
xmlhttp.open("POST", "/try/ajax/demo_post.php", true);
xmlhttp.send();

//如果需要像HTML表单一样传输数据，需要使用setRequestHeader()来添加HTTP头，然后在send()方法中规定希望发送的数据
xmlhttp.open("POST", "/try/ajax/demo_post2.php", true);
xmlhttp.sendRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send("fname=Henry&lname=Ford");

//方法
xmlhttp.sendRequestHeader(header, value);       //向请求添加HTTP头
//header: 规定头的名称
//value: 规定头的值
```

###  URL-服务器上的文件
- url 参数是服务器上文件的地址，该文件可以使任意类型的文件。
- 比如 .txt、 .xml 或者服务器脚本文件: .asp、 .php( 在传回响应之前，能够在服务器上执行任务 )

### Async-True或False
- ajax指的是异步 JavaScript 和 XML 
- XMLHttpRequest对象用于ajax的话，open()方法的 async 参数必须设置为 true。
- 通过ajax, JavaScript无需等待服务器的响应，而是
    + 在等待服务器响应时执行其他脚本
    + 当响应就绪后对响应进行处理

##### Async=true
- 当 async=true 时，需要规定在响应处于 onreadystatechange 事件中的就绪状态时执行的函数：
```js
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.getElementById("myDiv"),innerHTML=xmlhttp.responseText;
    }
}
xmlhttp.open("GET", "/try/ajax/ajax_info.txt", true);
xmlhttp.send();
```

##### Async=false
- JavaScript会等到服务器响应就绪才继续执行，如果服务器繁忙或缓慢，应用程序会挂起或停止。当 async=false 时，不要编写 onreadystatechange 函数，把代码放到 send() 语句后即可。
```js
xmlhttp.open("GET", "/try/ajax/ajax_info.txt", false);
xmlhttp.send();
document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```

## 服务器响应
- 如果要获得来自服务器的响应，就要使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。
```js
responseText    //获得字符串形式的响应数据
responseXML     //获得XML形式的响应数据
```

### responseText属性
- 当来自服务器的响应不是 XML 时，使用 responseText 属性。
```js
document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```

### responseXML属性
- 当来自服务器的响应是 XML，且需要作为 XML 对象进行解析时，使用responseXML属性。
```js
xmlDoc=xmlhttp.responseXML;
txt="";
x=xmlDoc.getElementsByTagName("ARTIST");
for (i=0;i<x.length;i++)
{
    txt=txt + x[i].childNodes[0].nodeValue + "<br>";
}
document.getElementById("myDiv").innerHTML=txt;
```

## onreadystatechange事件
- 当请求被发送到服务器时，我们需要执行一些基于响应的任务。
- 每当readyState改变时，就会触发 onreadystatechange 事件。
- readyState属性存有 XMLHttpRequest 的状态信息。
- XMLHttpRequest对象的三个重要属性：
```js
onreadystatechange    //存储函数(或函数名)，每当readyState属性改变时，就会调用该函数
readyState    //存有 XMLHttpRequest 的状态，从 0 到 4 发生变化
//0: 请求未初始化
//1: 服务连接已建立
//2: 请求已接收
//3: 请求处理中
//4: 请求已完成，且响应已就绪
state    //200: "OK"    404: 未找到页面
```
- 当服务器响应，已做好被处理的准备时，执行onreadystatechange事件中的任务
- 当readyState等于 4 且状态为 200 时，表示响应已就绪
```js
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.getElementById("myDiv"),innerHTML=xmlhttp.responseText;
    }
}
```

### 使用回调函数
- 回调函数式一种以参数形式传递给另一个函数的函数
- 如果网站上有多个 ajax 任务，那么应该编写一个标准的函数用来创建 XMLHttpRequest 对象。并为每个 ajax 任务调用该函数，
```js
function myFunction()
{
    loadXMLDoc("/try/ajax/ajax_info.txt",function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
    });
}
```
