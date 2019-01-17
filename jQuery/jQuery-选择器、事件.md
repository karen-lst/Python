## jQuery教程
- jQuery 是一个 JavaScript 库，极大地简化了 JavaScript 编程。
- 目前jQuery兼容于所有主流浏览器, 包括Internet Explorer 6。
- jQuery库包含以下功能：
    + HTML 元素选取
    + HTML 元素操作
    + CSS 操作
    + HTML 事件函数
    + JavaScript 特效和动画
    + HTML DOM 遍历和修改
    + AJAX
    + Utilities

## jQuery 安装
- 可以通过多种方法在网页中添加 jQuery。 您可以使用以下方法：
    + 从 jquery.com 下载 jQuery 库
    + 从 CDN（内容分发网络） 中载入 jQuery
- 有两个版本的 jQuery 可供下载：
    + Production version - 用于实际的网站中，已被精简和压缩。
    + Development version - 用于测试和开发（未压缩，是可读的代码）
- jQuery 库是一个 JavaScript 文件，您可以使用 HTML 的script标签引用它：
```js
<head>
<script src="jquery-1.10.2.min.js"></script>
</head>
```
- 使用CDN的优势：
    - 许多用户在访问其他站点时，已经从百度、谷歌加载过 jQuery。所以当他们访问您的站点时，会从缓存中加载 jQuery，这样可以减少加载时间。同时，大多数 CDN 都可以确保当用户向其请求文件时，会从离用户最近的服务器上返回响应，这样也可以提高加载速度。

## jQuery语法
- jQuery 语法是通过选取 HTML 元素，并对选取的元素执行某些操作。
- 基础语法： `$(selector).action()`
    - 美元符号定义 jQuery
    - 选择符（selector）"查询"和"查找" HTML 元素
```js
$(this).hide() - 隐藏当前元素

$("p").hide() - 隐藏所有 <p> 元素

$("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素

$("#test").hide() - 隐藏所有 id="test" 的元素
```

## 文档就绪事件
- 所有 jQuery 函数位于一个 document ready 函数中：
```js
$(document).ready(function(){
   // 开始写 jQuery 代码...
});
这是为了防止文档在完全加载（就绪之前）
运行jQuery代码即在DOM加载完成后才可以对DOM进行操作。
如果在文档没有完全加载之前就运行函数，操作可能失败。

下面是两个具体的例子：
    试图隐藏一个不存在的元素
    获得未完全加载的图像的大小
```

## jQuery 选择器
- jQuery 选择器允许对 HTML 元素组或单个元素进行操作。
- jQuery 选择器基于元素的 id、类、类型、属性、属性值等"查找"（或选择）HTML 元素。
- 它基于已经存在的 CSS 选择器，除此之外，它还有一些自定义的选择器。
```js
//元素选择器、#id 选择器、.class 选择器
$(this)                     选取当前 HTML 元素
$("p.intro")                选取 class 为 intro 的 <p> 元素
$("p:first")                选取第一个 <p> 元素
$("ul li:first")            选取第一个 <ul> 元素的第一个 <li> 元素
$("ul li:first-child")      选取每个 <ul> 元素的第一个 <li> 元素
$("[href]")                 选取带有 href 属性的元素 在线实例
$("a[target='_blank']")     选取所有 target 属性值等于 "_blank" 的 <a> 元素
$("a[target!='_blank']")    选取所有 target 属性值不等于 "_blank" 的 <a> 元素
$(":button")                选取所有 type="button" 的 <input> 元素 和 <button> 元素
$("tr:even")                选取偶数位置的 <tr> 元素
$("tr:odd")                 选取奇数位置的 <tr> 元素
```

## jQuery事件
- jQuery 是为事件处理特别设计的
- 页面对不同访问者的响应叫做事件。
- 事件处理程序指的是当 HTML 中发生某些事件时所调用的方法。
- 实例：
    - 在元素上移动鼠标
    - 选取单选按钮
    - 点击元素
```js
常见 DOM 事件：

鼠标事件        键盘事件    表单事件    文档/窗口事件
click           keypress    submit      load
dblclick        keydown     change      resize
mouseenter      keyup       focus       scroll
mouseleave      hover       blur        unload
```
```js
常用的 jQuery 事件方法:
$(document).ready()    $(document).ready()方法允许我们在文档完全加载完后执行函数。
click()                click() 方法是当按钮点击事件被触发时会调用一个函数。
dblclick()             当双击元素时，会发生 dblclick 事件。
mouseenter()           当鼠标指针穿过元素时，会发生 mouseenter 事件。
mouseleave()           当鼠标指针离开元素时，会发生 mouseleave 事件。
mousedown()     当鼠标指针移动到元素上方，并按下鼠标按键时，会发生 mousedown 事件。
mouseup()       当在元素上松开鼠标按钮时，会发生 mouseup 事件。
hover()         hover()方法用于模拟光标悬停事件。
//当鼠标移动到元素上时，会触发指定的第一个函数(mouseenter);
//当鼠标移出这个元素时，会触发指定的第二个函数(mouseleave)。
focus()         当通过鼠标点击选中元素或通过 tab 键定位到元素时，该元素就会获得焦点
blur()          当元素失去焦点时，发生 blur 事件。
```
