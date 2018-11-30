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

## PHP实例
- ajax用于创建动态性更强的应用程序
```js
//实例1: 将演示当用户在输入框中键入字符时，网页如何与 web 服务器进行通信。
function showHint(str)
{
    var xmlhttp;
    if (str.length == 0)
    {
        document.getElementById("txtHint").innerHTML="";
        return;
    }
    if (window.XMLHttpRequest)
    {   //主流浏览器执行代码
        xmlhttp = new XMLHttpRequest();
    }
    else
    {   //IE5、IE6浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", "/try/ajax/gethint.php?q="+str, true);
    xmlhttp.send();
}

```
```html
<h3>在输入框中尝试输入字母 a:</h3>
<form action="">
输入姓名: <input type="text" id="txt1" onkeyup="showHint(this.value)" />
</form>
<p>提示信息: <span id="txtHint"></span></p>
```
```js
源码解析:

- 当输入框为空( str.length == 0 )时, 函数清空 txtHint 占位符的内容,并退出函数。
- 如果不为空, showHint 函数执行以下任务:
    - 创建 XMLHttpRequest 对象
    - 当服务器响应就绪时执行函数
    - 把请求发送到服务器上的文件
```

##### 服务器页面-PHP
- 由上面的 JavaScript 调用的服务器页面是PHP文件，名为“gethint.php”
- "gethint.php"中的源代码会检查一个名字数组，然后向浏览器返回相应的名字:
```php
<?php
// Fill up array with names
$a[]="Anna";
$a[]="Brittany";
$a[]="Linda";
$a[]="Nina";
$a[]="Ophelia";
$a[]="Petunia";
$a[]="Amanda";

//get the q parameter from URL
$q=$_GET["q"];

//lookup all hints from array if length of q>0
if (strlen($q) > 0)
{
  $hint="";
  for($i=0; $i<count($a); $i++)
  {
    if (strtolower($q)==strtolower(substr($a[$i],0,strlen($q))))
    {
      if ($hint=="")
      {
        $hint=$a[$i];
      }
      else
      {
        $hint=$hint." , ".$a[$i];
      }
    }
  }
}

// Set output to "no suggestion" if no hint were found
// or to the correct values
if ($hint == "")
{
  $response="no suggestion";
}
else
{
  $response=$hint;
}

//output the response
echo $response;
?>
```

## DataBase实例
- ajax 可用来与数据库进行动态通信
```js
//实例2: 将演示网页如何通过ajax从数据库读取信息
function showCustomer(str)
{
  var xmlhttp;
  if (str=="")
  {
    document.getElementById("txtHint").innerHTML="";
    return;
  }
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET","/try/ajax/getcustomer.php?q="+str,true);
  xmlhttp.send();
}
```
```html
<form action="">
<select name="customers" onchange="showCustomer(this.value)" style="font-family: Verdana, Arial, Helvetica, sans-serif;">
<option value="APPLE">Apple Computer, Inc.</option>
<option value="BAIDU ">BAIDU, Inc</option>
<option value="Canon">Canon USA, Inc.</option>
<option value="Google">Google, Inc.</option>
<option value="Nokia">Nokia Corporation</option>
<option value="SONY">Sony Corporation of America</option>
</select>
</form>
<br>
<div id="txtHint">客户信息将显示在这...</div>
```
```js
源码解析:

- showCustomer() 函数执行以下任务:
    - 检查是否已选择某个客户
    - 创建 XMLHttpRequest 对象
    - 当服务器响应就绪时执行所创建的函数
    - 把请求发送到服务器上的文件
```

##### 服务器页面-PHP
- "getcustomer.php" 中的源代码负责对数据库进行查询，然后用 HTML 表格返回结果:
```php
<%
response.expires=-1
sql="SELECT * FROM CUSTOMERS WHERE CUSTOMERID="
sql=sql & "'" & request.querystring("q") & "'"

set conn=Server.CreateObject("ADODB.Connection")
conn.Provider="Microsoft.Jet.OLEDB.4.0"
conn.Open(Server.Mappath("/db/northwind.mdb"))
set rs=Server.CreateObject("ADODB.recordset")
rs.Open sql,conn

response.write("<table>")
do until rs.EOF
  for each x in rs.Fields
    response.write("<tr><td><b>" & x.name & "</b></td>")
    response.write("<td>" & x.value & "</td></tr>")
  next
  rs.MoveNext
loop
response.write("</table>")
%>
```

## XML实例
- ajax可以用来与XML文件进行交互式通信
```js
//实例3: 将演示网页如何使用ajax来读取来自XML文件的信息
function loadXMLDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    myFunction(this);
    }
  };
  xhttp.open("GET", "cd_catalog.xml", true);
  xhttp.send();
}
function myFunction(xml) {
  var i;
  var xmlDoc = xml.responseXML;
  var table="<tr><th>Artist</th><th>Title</th></tr>";
  var x = xmlDoc.getElementsByTagName("CD");
  for (i = 0; i <x.length; i++) {
    table += "<tr><td>" +
    x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue +
    "</td><td>" +
    x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue +
    "</td></tr>";
  }
  document.getElementById("demo").innerHTML = table;
}
```
```html
<h1>XMLHttpRequest 对象</h1>

<button type="button" onclick="loadXMLDoc()">获取我收藏的 CD</button>
<br><br>
<table id="demo"></table>
```
```
源码分析:

    - 当用户点击上面的"获取我收藏的 CD"这个按钮，就会执行 loadXMLDoc() 函数。
    - loadXMLDoc()函数创建XMLHttpRequest对象,添加当服务器响应就绪时执行的函数并将请求发送到服务器。
    - 当服务器响应就绪时会构建一个HTML表格，从XML文件中提取节点（元素），最后使用XML 数据填充 id="demo" 的表格元素。
```

##### 服务器页面-XML
- 上面这个例子中使用的服务器页面实际上是一个名为 "cd_catalog.xml" XML 文件。
```xml
<CATALOG>
<CD>
<TITLE>Empire Burlesque</TITLE>
<ARTIST>Bob Dylan</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Columbia</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1985</YEAR>
</CD>
<CD>
<TITLE>Hide your heart</TITLE>
<ARTIST>Bonnie Tyler</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>CBS Records</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1988</YEAR>
</CD>
</CATALOG>
```
