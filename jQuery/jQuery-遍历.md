## jQuery - 遍历
#### jQuery 祖先
- jQuery方法，用于向上遍历DOM树：
	+ parent()
	+ parents()
	+ parentsUntil()
```js
//parent()方法返回被选元素的直接父元素，该方法只会向上一级对DOM树进行遍历
$(document).ready(function(){
	$("span").parent();
});

//parents()方法返回被选元素的所有祖先元素，直到文档的根元素(<html>)
$(document).ready(function(){
	$("span").parents();
});
//可以使用可选参数来过滤对祖先元素的搜索，返回所有<span>元素的所有祖先，并且是<ul>元素
$(document).ready(function(){
	$("span").parents("ul");
});

//parentsUntil()方法返回介于两个给定元素之间的所有祖先元素
//返回介于<span>与<div>元素之间的所有祖先元素
$(document).ready(function(){
	$("span").parentsUntil("div");
});
```

#### jQuery 后代
- 向下遍历DOM树，查找元素的后代
	+ children()
	+ find()
```js
//children()方法返回被选元素的所有直接子元素，只会向下一级对DOM树进行遍历
$(document).ready(function(){
	$("div").children();
});
//可以使用可选参数来过滤子元素的搜索
//返回类名为"1"的所有<p>元素，并且是<div>的直接子元素
$(document).ready(function(){
	$("div").children("p.1");
});

//find()返回被选元素的后代元素，直到最后一个后代
//返回属于<div>后代的所有<span>元素
$(document).ready(function(){
	$("div").find("span");
});
//返回<div>的所有后代
$(document).ready(function(){
	$("div").find("*");
});
```

#### jQuery 同胞
- 在DOM树中进行水平遍历，遍历元素的同胞元素
	- siblings()
	- next()
	- nextAll()
	- nextUntil()
	- prev()
	- prevAll()
	- prevUntil()
```js
//返回被选元素的所有同胞元素
$(document).ready(function(){
	$("h2").siblings();
});
//返回属于<h2>的同胞元素的所有<p>元素
$(document).ready(function(){
	$("h2").siblings("p");
});

//next()方法返回被选元素的下一个同胞元素，只返回一个元素
$(document).ready(function(){
	$("h2").next();
});

//nextAll()方法返回被选元素的所有跟随的同胞元素
$(document).ready(function(){
	$("h2").nextAll();
});

//nextUntil()方法返回介于两个给定参数之间的所有跟随的同胞元素
//返回介于<h2>与<h6>元素之间的所有同胞元素
$(document).ready(function(){
	$("h2").nextUntil("h6");
});

//prev() prevAll() prevUntil()方法与上述方法类似，只是方向相反。遍历同胞之前的元素。
```

#### jQuery 过滤
- 过滤的作用：缩小搜索元素的范围
- 三个最基本的过滤方法：`first()、last()、eq()`
	- 允许基于其在一组元素中的位置来选择一个特定的元素。
- 其他过滤方法，比如 `filter()、not()`
	- 允许选取匹配或不匹配某项指定标准的元素。
```js
//first() 方法返回被选元素的首个元素
//选取首个 <div> 元素内部的第一个 <p> 元素：
$(document).ready(function(){
  $("div p").first();
});

//last() 方法返回被选元素的最后一个元素。
//选择最后一个 <div> 元素中的最后一个 <p> 元素：
$(document).ready(function(){
  $("div p").last();
});

//eq() 方法返回被选元素中带有指定索引号的元素。
//索引号从 0 开始,选取第二个 <p> 元素（索引号 1）：
$(document).ready(function(){
  $("p").eq(1);
});

//filter()方法允许您规定一个标准。不匹配这个标准的元素会被从集合中删除，匹配的元素会被返回。
//返回带有类名 "url" 的所有 <p> 元素：
$(document).ready(function(){
  $("p").filter(".url");
});

//not() 方法返回不匹配标准的所有元素。与 filter() 相反。
//返回不带有类名 "url" 的所有 <p> 元素：
$(document).ready(function(){
  $("p").not(".url");
});
```
