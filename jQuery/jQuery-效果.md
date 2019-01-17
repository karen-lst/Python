## jQuery 效果
- 隐藏、显示、切换，滑动，淡入淡出，以及动画等等

#### jQuery - 隐藏和显示
- `hide() 和 show()`
    - 可以使用 `hide() 和 show()` 方法来隐藏和显示 HTML 元素
```js
//语法：
$(selector).hide(speed,callback);
$(selector).show(speed,callback);
// speed 参数规定隐藏/显示的速度，可以取以下值："slow"、"fast" 或毫秒。
// callback 参数是隐藏或显示完成后所执行的函数名称。

//实例：
//hide() 和 show() 方法
$("#hide").click(function(){
  $("p").hide();
});
$("#show").click(function(){
  $("p").show();
});
//设置隐藏的速度
$("button").click(function(){
  $("p").hide(1000);
});
//设置隐藏的速度，并使用回调函数。"linear"是一个字符串，表示过渡使用哪种缓动函数。
//jQuery自身提供"linear" 和 "swing"，其他可以使用相关的插件）。
$(document).ready(function(){
  $(".hidebtn").click(function(){
    $("div").hide(1000,"linear",function(){
      alert("Hide() 方法已完成!");
    });
  });
});
```
- `jQuery toggle()`
    - 可以使用 toggle() 方法来切换 hide() 和 show() 方法。
```js
//语法：
$(selector).toggle(speed,callback);

//实例：
$("button").click(function(){
  $("p").toggle();
});
```

#### jQuery - 淡入淡出
- 通过 jQuery 下面四种 fade 方法可以实现元素的淡入淡出效果：
    - fadeIn()
    - fadeOut()
    - fadeToggle()
    - fadeTo()
```js
//jQuery fadeIn() 用于淡入已隐藏的元素。
//语法：
$(selector).fadeIn(speed,callback);
//实例：
$("button").click(function(){
  $("#div1").fadeIn();
  $("#div2").fadeIn("slow");
  $("#div3").fadeIn(3000);
});

//jQuery fadeOut() 方法用于淡出可见元素。
$("button").click(function(){
  $("#div1").fadeOut();
  $("#div2").fadeOut("slow");
  $("#div3").fadeOut(3000);
});

//jQuery fadeToggle() 方法可以在 fadeIn() 与 fadeOut() 方法之间进行切换。
$("button").click(function(){
  $("#div1").fadeToggle();
  $("#div2").fadeToggle("slow");
  $("#div3").fadeToggle(3000);
});

//jQuery fadeTo() 方法允许渐变为给定的不透明度（值介于 0 与 1 之间）
//語法：
$(selector).fadeTo(speed,opacity,callback);
//必需的 opacity 参数将淡入淡出效果设置为给定的不透明度（值介于 0 与 1 之间）。

//实例：
$("button").click(function(){
  $("#div1").fadeTo("slow",0.15);
  $("#div2").fadeTo("slow",0.4);
  $("#div3").fadeTo("slow",0.7);
});
```

#### jQuery - 滑动
- 通过 jQuery 以下滑动方法可以在元素上创建滑动效果：
    + slideDown()
    + slideUp()
    + slideToggle()
```js
//jQuery slideDown() 方法用于向下滑动元素
//语法:
$(selector).slideDown(speed,callback);
//实例：
$("#flip").click(function(){
  $("#panel").slideDown();
});

//jQuery slideUp() 方法用于向上滑动元素。
//slideToggle() 方法可以在 slideDown() 与 slideUp() 方法之间进行切换。
```

#### jQuery - 动画
- 可以用 animate() 方法来操作几乎所有的 CSS 属性，但是需要记住：
    - 使用 animate() 时，必须使用 Camel 标记法书写所有的属性名，
    - 比如，必须使用 paddingLeft 而不是 padding-left，使用 marginRight 而不是 margin-right。
    - 同时，色彩动画并不包含在核心 jQuery 库中。如果需要生成颜色动画，需要从 jquery.com 下载 颜色动画 插件。
```js
//jQuery animate() 方法用于创建自定义动画。
//语法：
$(selector).animate({params},speed,callback);
//必要的 params 参数定义形成动画的 CSS 属性。
//实例：
$("button").click(function(){
  $("div").animate({left:'250px'});
});

<div style="background:#98bf21;height:100px;width:100px;position:absolute;">
</div>
//默认情况下，所有 HTML 元素都有一个静态位置，且无法移动。
//如需对位置进行操作，要记得首先把元素的 CSS position 属性设置为 relative、fixed 或 absolute！

//生成动画的过程中同时使用多个属性：
$("button").click(function(){
  $("div").animate({
    left:'250px',
    opacity:'0.5',
    height:'150px',
    width:'150px'
  });
});
```

- 可以定义相对值。在值的前面加上 += 或 -=：
```js
$("button").click(function(){
  $("div").animate({
    left:'250px',
    height:'+=150px',
    width:'+=150px'
  });
});
```
- 可以使用预定义的值,把属性的动画值设置为 "show"、"hide" 或 "toggle"：
```js
$("button").click(function(){
  $("div").animate({
    height:'toggle'
  });
});
```
- 可以使用队列功能
    - jQuery 提供针对动画的队列功能。
    - 在彼此之后编写多个 animate() 调用
    - jQuery会创建包含这些方法调用的"内部"队列。然后逐一运行这些 animate 调用。
```js
$("button").click(function(){
  var div=$("div");
  div.animate({height:'300px',opacity:'0.4'},"slow");
  div.animate({width:'300px',opacity:'0.8'},"slow");
  div.animate({height:'100px',opacity:'0.4'},"slow");
  div.animate({width:'100px',opacity:'0.8'},"slow");
});

//把 <div> 元素往右边移动了 100 像素，然后增加文本的字号：
$("button").click(function(){
  var div=$("div");
  div.animate({left:'100px'},"slow");
  div.animate({fontSize:'3em'},"slow");
});
```

#### jQuery - 停止动画
- jQuery stop() 方法用于停止动画或效果，在它们完成之前。
- stop() 方法适用于所有 jQuery 效果函数，包括滑动、淡入淡出和自定义动画。
```js
//语法：
$(selector).stop(stopAll,goToEnd);
//可选的 stopAll 参数规定是否应该清除动画队列。默认是 false，即仅停止活动的动画，允许任何排入队列的动画向后执行。
//可选的 goToEnd 参数规定是否立即完成当前动画。默认是 false。
//默认地，stop() 会清除在被选元素上指定的当前动画。

//实例：
$("#stop").click(function(){
  $("#panel").stop();
});
```

#### jQuery - Callback 方法
- Callback 函数在当前动画 100% 完成之后执行。
```js
//实例1：在隐藏效果完全实现后回调函数
$("button").click(function(){
  $("p").hide("slow",function(){
    alert("段落现在被隐藏了");
  });
});

//实例2：没有回调函数，警告框会在隐藏效果完成前弹出
$("button").click(function(){
  $("p").hide(1000);
  alert("段落现在被隐藏了");
});
```

#### jQuery - 链(Chaining)
- 通过 jQuery，可以把动作/方法链接在一起。Chaining 允许我们在一条语句中运行多个 jQuery 方法（在相同的元素上）。
- 浏览器就不必多次查找相同的元素。如需链接一个动作，您只需简单地把该动作追加到之前的动作上。
```js
//实例1：把 css()、slideUp() 和 slideDown() 链接在一起。
//"p1" 元素首先会变为红色，然后向上滑动，再然后向下滑动：
$(document).ready(function()
  {
  $("button").click(function(){
    $("#p1").css("color","red").slideUp(2000).slideDown(2000);
  });
});
//当进行链接时，代码行会变得很长.可以按照希望的格式来写，包含换行和缩进
//jQuery 会抛掉多余的空格，并当成一行长代码来执行上面的代码行。
$(document).ready(function()
  {
  $("button").click(function(){
    $("#p1").css("color","red")
      .slideUp(2000)
      .slideDown(2000);
  });
});
```
