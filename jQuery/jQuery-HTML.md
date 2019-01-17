## jQuery - 捕获
- jQuery 拥有可操作 HTML 元素和属性的强大方法。

#### DOM 操作
- jQuery 提供一系列与 DOM 相关的方法，这使访问和操作元素和属性变得很容易。
- 获得内容：text()、html() 以及 val()
    + text() - 设置或返回所选元素的文本内容
    + html() - 设置或返回所选元素的内容（包括 HTML 标记）
    + val() - 设置或返回表单字段的值
```js
$("#bt1").click(function(){
    alert("text: " + $("p").text());
});
$("#bt2").click(function(){
    alert("html: " + $("p").html());
});
$("#bt3").click(function(){
    alert("value: " + $("p").val());
});
```
- 获取属性：attr()
    + jQuery attr() 方法用于获取属性值。
```js
//实例1：演示如何获得链接中 href 属性的值
$("button").click(function(){
    alert("属性值为： " + $("#runoob").attr("href"));
});

<p><a href="http://www.runoob.com" id="runoob">菜鸟教程</a></p>
<button>显示href的值</button>
```

## jQuery - 设置
- text()、html()、val()三个方法，同样拥有回调函数。
- 回调函数有两个参数：被选元素列表中当前元素的下标，以及原始（旧的）值。然后以函数新值返回您希望使用的字符串。
```js
$(document).ready(function(){
  $("#btn1").click(function(){
    $("#test1").text(function(i,origText){
      return "旧文本: " + origText + " 新文本: Hello world! (index: " + i + ")";
    });
  });

  $("#btn2").click(function(){
    $("#test2").html(function(i,origText){
      return "旧 html: " + origText + " 新 html: Hello <b>world!</b> (index: " + i + ")";
    });
  });
});

<p id="test1">这是一个有 <b>粗体</b> 字的段落。</p>
<p id="test2">这是另外一个有 <b>粗体</b> 字的段落。</p>
<button id="btn1">显示 新/旧 文本</button>
<button id="btn2">显示 新/旧 HTML</button>
```
- attr() 方法也用于设置/改变属性值。
```js
//实例：演示如何改变（设置）链接中 href 属性的值：
$(document).ready(function(){
  $("button").click(function(){
    $("#runoob").attr("href","http://www.runoob.com/jquery");
  });
});

<p><a href="http://www.runoob.com" id="runoob">菜鸟教程</a></p>
<button>修改 href 值</button>
<p>点击按钮修改后，可以点击链接查看链接地址是否变化。</p>
```

## jQuery - 添加元素
- 添加新内容的四个 jQuery 方法：
    - append() - 在被选元素的结尾插入内容
    - prepend() - 在被选元素的开头插入内容
    - after() - 在被选元素之后插入内容
    - before() - 在被选元素之前插入内容
```js
//jQuery append() 方法在被选元素的结尾插入内容（仍然该元素的内部）
$(document).ready(function(){
  $("#btn1").click(function(){
    $("p").append(" <b>追加文本</b>。");
  });

  $("#btn2").click(function(){
    $("ol").append("<li>追加列表项</li>");
  });
});
//jQuery prepend() 方法在被选元素的开头插入内容。
$("p").prepend("在开头追加文本");

//jQuery after() 方法在被选元素之后插入内容。
$("img").after("在后面添加文本");

//jQuery before() 方法在被选元素之前插入内容。
$("img").before("在前面添加文本");
```

## jQuery - 删除元素
- 如需删除元素和内容，一般可使用以下两个 jQuery 方法：
    - remove() - 删除被选元素（及其子元素）
    - empty() - 从被选元素中删除子元素
```js
$(document).ready(function(){
  $("button").click(function(){
    $("#div1").remove();
  });
});

$(document).ready(function(){
  $("button").click(function(){
    $("#div1").empty();
  });
});

//jQuery remove() 方法也可接受一个参数，允许您对被删元素进行过滤。
//该参数可以是任何 jQuery 选择器的语法。
//下面的例子删除 class="italic" 的所有 <p> 元素：
$(document).ready(function(){
  $("button").click(function(){
    $("p").remove(".italic");
  });
});

<p>这是一个段落。</p>
<p class="italic"><i>这是另外一个段落。</i></p>
<p class="italic"><i>这是另外一个段落。</i></p>
<button>移除所有  class="italic" 的 p 元素。</button>
```

## jQuery - 获取并设置 CSS 类
- jQuery 拥有若干进行 CSS 操作的方法。我们将学习下面这些：
    - addClass(): 向被选元素添加一个或多个类
    - removeClass(): 从被选元素删除一个或多个类
    - toggleClass(): 对被选元素进行添加/删除类的切换操作
    - css(): 设置或返回样式属性
```js
//如何向不同的元素添加 class 属性
$(document).ready(function(){
  $("button").click(function(){
    $("h1,h2,p").addClass("blue");
    $("div").addClass("important");
  });
});

//如何在不同的元素中删除指定的 class 属性：
$("button").click(function(){
  $("h1,h2,p").removeClass("blue");
});

//如何使用 jQuery toggleClass() 方法。该方法对被选元素进行添加/删除类的切换操作：
$("button").click(function(){
  $("h1,h2,p").toggleClass("blue");
});
```

## jQuery - css() 方法
- css() 方法设置或返回被选元素的一个或多个样式属性。
```js
//返回 CSS 属性
//語法：css("propertyname");
$(document).ready(function(){
  $("button").click(function(){
    alert("背景颜色 = " + $("p").css("background-color"));
  });
});

//设置 CSS 属性
//語法：css("propertyname","value");
//下面的例子将为所有匹配元素设置 background-color 值
$(document).ready(function(){
  $("button").click(function(){
    $("p").css("background-color","yellow");
  });
});

//设置多个 CSS 属性
//語法：css({"propertyname":"value","propertyname":"value",...});
//下面的例子将为所有匹配元素设置 background-color 和 font-size：
$(document).ready(function(){
  $("button").click(function(){
    $("p").css({"background-color":"yellow","font-size":"200%"});
  });
});
```

## jQuery - 尺寸
- 通过 jQuery，很容易处理元素和浏览器窗口的尺寸。
- jQuery 提供多个处理尺寸的重要方法：
    - width()
    - height()
    - innerWidth()
    - innerHeight()
    - outerWidth()
    - outerHeight()
```js
//width()、height()设置或返回元素的宽度、高度(不包括内边距、边框、外边距)
$(document).ready(function(){
      $("button").click(function(){
        var txt = "";
        txt += "DIV的宽度: " + $("#d1").width() + "<br>";
        txt += "DIV的高度: " + $("#d1").height() + "<br>";
        txt += "DIV的宽度(包含内边距): " + $("#d1").innerWidth() + "<br>";
        txt += "DIV的高度(包含内边距): " + $("#d1").innerHeight() + "<br>";
        txt += "DIV的宽度(包含内边距、边框): " + $("#d1").outerWidth() + "<br>";
        txt += "DIV的高度(包含内边距、边框): " + $("#d1").outerHeight() + "<br>";
        $("#d1").html(txt);
      });
    });
//innerWidth()、innerHeight()返回元素的宽度、高度(包括内边距)
//outerWidth()、outerHeight()返回元素的宽度、高度(包括内边距、边框)
```
