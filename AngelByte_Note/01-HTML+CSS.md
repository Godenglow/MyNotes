<font style="background-color:rgb(217,245,214);">大家学习中如果碰到任何的困难(BUG、学习规划、学习资料等)，都可以加入</font>[**<font style="background-color:rgb(217,245,214);">黑马智学伴侣(有问题点我)</font>**](https://heuqqdmbyk.feishu.cn/wiki/OFI5wHhUpiCGTkk2L86cXY2hngF)<font style="background-color:rgb(217,245,214);">寻求帮助，有学习交流群，老师、同学在线答疑。还有独享的企业级项目，避免与人撞车。</font>

Hello，各位同学，接下来呢，我们就正式的进入到Web前端开发知识的学习，那么在学习Web前端的开发内容之前，先来认识一下Web前端。

## 初识Web前端
### 介绍
我们介绍Web网站工作流程的时候提到，前端开发，主要的职责就是将数据以好看的样式呈现出来。说白了，就是开发网页程序，如下图所示：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891454270-031754ab-2b39-41bb-8b9c-8e96f50ccf3e.png)

**主要明确以下三个问题：**

1). 网页由哪些部分组成 ?

- 文字、图片、音频、视频、超链接、表格等等。

2). 我们看到的网页，背后的本质是什么 ?

- 前端程序员写的前端代码 (备注：在前后端分离的开发模式中)

3). 前端的代码是如何转换成用户眼中的网页的 ?

- 通过浏览器转化（解析和渲染）成用户看到的网页
- 浏览器中对代码进行解析和渲染的部分，称为 **浏览器内核**

而市面上的浏览器非常多，比如：IE、火狐Firefox、苹果safari、欧朋、谷歌Chrome、QQ浏览器、360浏览器等等。 而且我们电脑上安装的浏览器可能都不止一个，有很多。 

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891454208-52c132fa-c04d-4e57-9f2b-92a6bdee0338.png)

但是呢，需要大家注意的是，不同的浏览器，内核不同，对于相同的前端代码解析的效果也会存在差异。 那这就会造成一个问题，同一段前端程序，不同浏览器展示出来的效果是不一样的，这个用户体验就很差了。而我们想达到的效果则是，即使用户使用的是不同的浏览器，解析同一段前端代码，最终展示出来的效果都是相同的。

要想达成这样一个目标，我们就需要定义一个统一的标准，然后让各大浏览器厂商都参照这个标准来实现即可。 而这套标准呢，其实早都已经定义好了，那就是我们接下来，要介绍的**<font style="color:rgb(216,57,49);">web标准</font>**。

### Web标准
**Web标准**也称为**网页标准**，由一系列的标准组成，大部分由W3C（ World Wide Web Consortium，万维网联盟）负责制定。由三个组成部分：

- HTML：负责网页的<font style="color:rgb(216,57,49);">结构</font>（页面元素和内容）。
- CSS：负责网页的<font style="color:rgb(216,57,49);">表现</font>（页面元素的外观、位置等页面样式，如：颜色、大小等）。
- JavaScript：负责网页的<font style="color:rgb(216,57,49);">行为</font>（交互效果）。

那在我们的前端课程中，除了会讲解HTML、CSS、JS这些技术以外，还会讲解现在前端开发中的高级技术Vue、ElementPlus、Axios。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891454714-dbe2afc1-b73c-444f-abb9-52a01a48d259.png)

 而Web前端开发的内容呢，我们在设计的时候，也进行了分层的设计，分为了两个部分：

- Web前端基础：HTML、CSS、JS、Vue3、Ajax、Axios，前端基础部分为两天时间。
- Web前端进阶：Vue工程化、ElementPlus、Tlias智能学习辅助系统案例，前端进阶部分为三天时间。

那今天我们就先来讲解Web前端基础的第一部分： HTML & CSS。

<font style="background-color:rgb(255,245,235);">什么是HTML？</font>

**<font style="background-color:rgb(255,245,235);">HTML</font>**<font style="background-color:rgb(255,245,235);">: </font>**<font style="background-color:rgb(255,245,235);">H</font>**<font style="background-color:rgb(255,245,235);">yper</font>**<font style="background-color:rgb(255,245,235);">T</font>**<font style="background-color:rgb(255,245,235);">ext </font>**<font style="background-color:rgb(255,245,235);">M</font>**<font style="background-color:rgb(255,245,235);">arkup </font>**<font style="background-color:rgb(255,245,235);">L</font>**<font style="background-color:rgb(255,245,235);">anguage，超文本标记语言。</font>

- <font style="background-color:rgb(255,245,235);">超文本：超越了文本的限制，比普通文本更强大。除了文字信息，还可以定义图片、音频、视频等内容。</font>
- <font style="background-color:rgb(255,245,235);">标记语言：由标签 "<标签名>" 构成的语言</font>
    - <font style="background-color:rgb(255,245,235);">HTML标签都是预定义好的 。例如：使用 <h1> 标签展示标题，使用<a>展示超链接，使用<img>展示图片，<video>展示视频。</font>
    - <font style="background-color:rgb(255,245,235);">HTML代码直接在浏览器中运行，HTML标签由浏览器解析 。</font>
- 下面展示的是一段html代码经过浏览器解析，呈现的效果如右图所示： 

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891454637-830576f4-1cf0-4fcd-b1b8-2abd6cc05968.png)

<font style="background-color:rgb(255,245,235);">什么是CSS？</font>

- **<font style="background-color:rgb(255,245,235);">CSS:</font>**<font style="background-color:rgb(255,245,235);"> Cascading Style Sheet，层叠样式表，用于控制页面的样式（表现）。</font>

下面展示的是一段 html代码 及 CSS样式 经过浏览器解析，呈现的效果如右图所示：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891454288-aab8a685-5774-4f04-a58b-775c5b4dfc73.png)

## HTML快速入门
### 操作步骤
1. **新建文本文件，后缀名改为 .html，命名为：01. html快速入门.html**

创建一个名为HTML的文件夹，然后找到课程资料中的 1.png 文件放到该目录下的img目录中。此时HTML文件夹中内容如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891454966-fc9f877d-b4e7-458e-8310-505716c218f0.png)

1. **写HTML的基本骨架，定义标题**

选中文件，鼠标右击，选择使用记事本打开文件，并且编写网页的标题。

首先html有固定的基本结构

```plain
<html>
     <head>
          <title>HTML 快速入门</title>
     </head>
     <body>
                
     </body>
</html>
```

其中`<html>`是根标签，`<head>`和`<body>`是子标签。

- `<head>` : 定义网页的头部，用来存放给浏览器看的信息，如：CSS样式、网页的标题。 
- `<body>` : 定义网页的主体部分，存放给用户看的信息，也是网页的主体内容，如：文字、图片、视频、音频、表格等。
1. **在<body>中编写HTML的核心内容**

```plain
<html>
     <head>
        <title>HTML 快速入门</title>
     </head>
     <body>
        <h1>Hello HTML</h1>
        <img src="img/1.png">
     </body>
</html>
```

其中 `<h1>` 标签是一个一级标题的标签。 `<img>` 标签是一个图片标签，用来展示图片，而其中的 src 属性是用来指定要展示的图片。

1. **然后选中文件，鼠标右击，选择使用浏览器打开文件**

浏览器呈现效果如下:

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891455207-ec5ef42c-b153-427f-b331-28bd1eb4e7a5.png)

### 2.2 总结
**1). HTML页面的基础结构标签**

```plain
<html>
    <head>
        <title> </title>
    </head>
    <body>
       
    </body>
</html>
```

`<title>`中定义标题显示在浏览器的标题位置，`<body>`中定义的内容会呈现在浏览器的内容区域

**2). HTML中的标签特点**

- HTML标签不区分大小写，建议小写
- HTML标签的属性值，采用单引号、双引号都可以，一般写双引号
- HTML语法相对比较松散 (建议大家编写HTML标签的时候尽量严谨一些)

## 前端开发工具
我们通过快速入门案例，发现由记事本文件开发html是非常不方便的，所以接下来我们需要学习一款前端专业的开发工具VS Code。

Visual Studio Code（简称 VS Code ）是 Microsoft 于2015年4月发布的一款代码编辑器。VS Code 对前端代码有非常强大的支持，同时也其他编程语言（例如：C++、Java、Python、PHP、Go等）。VS Code 提供了非常强大的插件库，大大提高了开发效率。

- **官网：**[<font style="color:rgb(46,161,33);">https://code.visualstudio.com</font>](https://code.visualstudio.com/)
- **安装：**[**VsCode安装文档**](https://heuqqdmbyk.feishu.cn/wiki/P8Cbw64UAi3h92kqnUpcfF4cnNg)
- **注意：**
    - <font style="color:rgb(216,57,49);">需要注意的是，我们作为一名开发者，不应该将软件</font><font style="color:rgb(216,57,49);">软装</font><font style="color:rgb(216,57,49);">在包含中文名的路径中 。</font>
    - <font style="color:rgb(216,57,49);">由于安装了IDEA快捷键的插件，VSCode快键键与IDEA是一致的。</font>

## 常见标签&样式
那我们在讲解HTML的常见基础标签 及 CSS的基本样式时，我们就以 新浪新闻页面 为例，来进行讲解，这样大家不仅能够知道 常见标签及样式的作用，还能够知道具体的应用场景。

央视新闻的具体页面效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457027-ffa0abab-047c-4250-8ebc-3222b30cb060.png)

原始页面网址：https://news.cctv.com/2024/05/15/ARTIflTnFvNMx9nUVc4PA7T2240515.shtml

而大家可以看到，上述新闻网页，其实分为两个部分，一个是新闻的标题部分，另一个是新闻的正文部分。那接下来，我们就先来完成央视新闻标题部分的制作。

### 央视新闻-标题
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457068-d1973e91-44db-4607-9754-2972dcede9bb.png)

前面我们提到，我们在浏览器中看到的网页程序呈现出来的效果，实际上是浏览器解析并渲染了前端代码而呈现出来的。 而我们所编写的HTML页面，在浏览器中渲染的时候，是从上往下逐行解析展示的。 所以，我们在编写html页面的时候，要根据页面的布局，从上往下编写。

#### 标题排版
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457061-d7d74a8f-2a07-4da4-96a5-9454c1cacc39.png)

在制作网页的时候，我们可以充分的利用AI辅助工具**通义灵码**，来帮我们实现对应的功能，我们只需要在编辑器中给定对应的注释（提示词），通义灵码就可以帮我们实现对应的功能效果，然后我们再基于生成的代码进行调试即可。

接下来，我们就可以通过VsCode打开HTML文件夹，然后在其中创建一个html页面，命名为：`02. 央视新闻-标题排版.html`。

然后在这个文件中来制作新浪新闻网页，标题部分的排版内容为：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title>
</head>
<body>

  <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 -->
  <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1>
  
  <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 -->
  <a href="https://news.cctv.com/" target="_blank">央视网</a>
  2024年05月15日 20:07
  
</body>
</html>
```

那在上述我们用到的两个标签，一个是标题标签 `<h1></h1>`，另一个是超链接标题 `<a></a>`。这两个标签的具体用法如下：

<font style="background-color:rgb(255,245,235);">标题标签 h 系列：</font>

<font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><h1></font><font style="background-color:rgb(255,245,235);"> 11111111111111 </font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></h1></font>

<font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><h2></font><font style="background-color:rgb(255,245,235);"> 11111111111111 </font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></h2></font>

<font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><h3></font><font style="background-color:rgb(255,245,235);"> 11111111111111 </font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></h3></font>

<font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><h4></font><font style="background-color:rgb(255,245,235);"> 11111111111111 </font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></h4></font>

<font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><h5></font><font style="background-color:rgb(255,245,235);"> 11111111111111 </font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></h5></font>

<font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><h6></font><font style="background-color:rgb(255,245,235);"> 11111111111111 </font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></h6></font>

**<font style="background-color:rgb(255,245,235);">效果：</font>**<font style="background-color:rgb(255,245,235);">h1为一级标题，字体也是最大的 ； h6为六级标题，字体是最小的。</font>

**<font style="color:rgb(216,57,49);background-color:rgb(255,245,235);">注意：</font>**<font style="color:rgb(216,57,49);background-color:rgb(255,245,235);">HTML标签是预定义好的，不能随意定义，也就以为着，标题标签就只有这六个，没有 <h7></font>

<font style="background-color:rgb(255,245,235);">超链接 a 标签：</font>

<font style="background-color:rgb(255,245,235);">标签：</font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"><a href="....." target="....."></font><font style="background-color:rgb(255,245,235);">央视网</font><font style="color:rgb(46,161,33);background-color:rgb(255,245,235);"></a></font>

<font style="background-color:rgb(255,245,235);">属性：</font>

- <font style="background-color:rgb(255,245,235);">href: 指定资源访问的url</font>
- <font style="background-color:rgb(255,245,235);">target: 指定在何处打开资源链接</font>
    - <font style="background-color:rgb(255,245,235);">_self: 默认值，在当前页面打开</font>
    - <font style="background-color:rgb(255,245,235);">_blank: 在空白页面打开</font>

#### 标题样式
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457048-33292a8f-d872-4f75-ae10-0fb308445136.png)

我们可以看到，目前我们制作的新闻标题部分，新闻发布时间 `2024年05月15日 20:07` 的字体颜色是**黑色**，而在原始的央视新闻页面中，字体的颜色呈现**<font style="color:rgb(143,149,158);">灰色</font>**<font style="color:rgb(143,149,158);">，具体的呈现效果如下：</font>

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457027-edcde086-69de-40b0-997e-08ab0314f396.png)

那接下来，我们要来控制字体的颜色，而这部分其实是属于网页的样式，所以这里呢，就要**通过CSS样式控制**。

这些基础的功能我们就可以直接通过AI工具帮我们实现，参考如下**<font style="color:rgb(100,37,208);">提示词(prompt)：</font>**

<font style="background-color:rgb(255,245,235);">你是一名前端开发工程师，请通过css为网页中的新闻发布时间设置字体颜色为灰色。 网页内容如下：</font>

<font style="background-color:rgb(255,245,235);"><!DOCTYPE html></font>

<font style="background-color:rgb(255,245,235);"><html lang="en"></font>

<font style="background-color:rgb(255,245,235);"><head></font>

<font style="background-color:rgb(255,245,235);"> <meta charset="UTF-8"></font>

<font style="background-color:rgb(255,245,235);"> <meta name="viewport" content="width=device-width, initial-scale=1.0"></font>

<font style="background-color:rgb(255,245,235);"> <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title></font>

<font style="background-color:rgb(255,245,235);"></head></font>

<font style="background-color:rgb(255,245,235);"><body></font>

<font style="background-color:rgb(255,245,235);">   <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 --></font>

<font style="background-color:rgb(255,245,235);">   <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1></font>

<font style="background-color:rgb(255,245,235);">   <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 --></font>

<font style="background-color:rgb(255,245,235);">   <a href="https://news.cctv.com/" target="_blank">央视网</a></font>

<font style="background-color:rgb(255,245,235);">   2024年05月15日 20:07</font>

<font style="background-color:rgb(255,245,235);"></body></font>

<font style="background-color:rgb(255,245,235);"></html></font>

AI给出的最终代码实现如下：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title>
  <style>
    .publish-date {
      color: gray;
    }
  </style>
</head>
<body>

  <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 -->
  <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1>
  
  <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 -->
  <a href="https://news.cctv.com/" target="_blank">央视网</a>
  <span class="publish-date">2024年05月15日 20:07</span>

</body>
</html>
```

我们可以看到，通过上面这样一段代码，就可以控制字体的颜色，而其实上面这一段代码就是AI生成的CSS样式。最终效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457696-6f7ccb01-f1c6-4637-9a8d-1d215b47fe5e.png)

##### CSS引入方式
那在HTML的文件中，我们如何来编写CSS样式呢，此时就涉及到CSS的三种引入方式。

具体有3种引入方式，语法如下表格所示：

| <font style="color:rgb(0, 0, 0);">名称</font> | <font style="color:rgb(0, 0, 0);">语法描述</font> | <font style="color:rgb(0, 0, 0);">示例</font> |
| :---: | --- | :--- |
| <font style="color:rgb(0, 0, 0);">行内样式</font> | <font style="color:rgb(0, 0, 0);">在标签内使用style属性，属性值是css属性键值对。</font> | <font style="color:rgb(0, 0, 0);"><h1 style="xxx:xxx;">中国新闻网</h1></font> |
| <font style="color:rgb(0, 0, 0);">内部样式</font> | <font style="color:rgb(0, 0, 0);">定义<style>标签，在标签内部定义css样式。</font> | <font style="color:rgb(0, 0, 0);"><style> h1 {...} </style></font> |
| <font style="color:rgb(0, 0, 0);">外部样式</font> | <font style="color:rgb(0, 0, 0);">定义<link>标签，通过href属性引入外部css文件</font> | <font style="color:rgb(0, 0, 0);"><link rel="stylesheet" href="css/news.css"></font> |

对于上述3种引入方式，企业开发的使用情况如下：

- **行内样式：**会出现大量的代码冗余，不方便后期的维护，所以不常用（常配合JS使用）。
- **内部样式****：**通过定义css选择器，让样式作用于当前页面的指定的标签上。（可以写在页面任何位置，但通常约定写在head标签中）
- **外部样式：**html和css实现了完全的分离，企业开发常用方式。

##### 颜色表示方式
在前端程序开发中，颜色的表示方式常见的有如下三种：

| <font style="color:rgb(0, 0, 0);">表示方式</font> | <font style="color:rgb(0, 0, 0);">属性值</font> | <font style="color:rgb(0, 0, 0);">说明</font> | <font style="color:rgb(0, 0, 0);">取值</font> |
| :---: | :---: | --- | --- |
| <font style="color:rgb(0, 0, 0);">关键字</font> | <font style="color:rgb(0, 0, 0);">颜色英文单词</font> | <font style="color:rgb(0, 0, 0);">red、green、blue</font> | <font style="color:rgb(0, 0, 0);">red、green、blue...</font> |
| <font style="color:rgb(0, 0, 0);">rgb表示法</font> | <font style="color:rgb(0, 0, 0);">rgb(r, g, b)</font> | <font style="color:rgb(0, 0, 0);">红绿蓝三原色，每项取值范围：0-255</font> | <font style="color:rgb(0, 0, 0);">rgb(0,0,0)、rgb(255,255,255)、rgb(255,0,0)</font> |
| <font style="color:rgb(0, 0, 0);">rgba表示法</font> | <font style="color:rgb(0, 0, 0);">rgba(r, g, b, a)</font> | <font style="color:rgb(0, 0, 0);">红绿蓝三原色，a表示透明度，取值：0-1</font> | <font style="color:rgb(0, 0, 0);">rgb(0,0,0,0.3)、rgb(255,255,255,0.5)</font> |
| <font style="color:rgb(0, 0, 0);">十六进制表示法</font> | <font style="color:rgb(0, 0, 0);">#rrggbb</font> | <font style="color:rgb(0, 0, 0);">#开头，将数字转换成十六进制表示</font> | <font style="color:rgb(0, 0, 0);">#000000、#ff0000、#cccccc，简写：#000、#ccc</font> |

##### 设置字体颜色

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title>
  <!-- 2. 内部样式 -->
  <style>
    .publish-date {
      color: #b2b2b2;
    }
  </style>
  <!-- 3. 外部样式 -->
  <!-- <link rel="stylesheet" href="css/news.css"> -->
</head>
<body>

  <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 -->
  <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1>
  
  <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 -->
  <a href="https://news.cctv.com/" target="_blank">央视网</a>

  <!-- 1. 行内样式 -->
  <!-- <span style="color: #b2b2b2;">2024年05月15日 20:07</span> -->

  <span class="publish-date">2024年05月15日 20:07</span>

</body>
</html>
```

<font style="color:rgb(216,57,49);">备注: 要想拾取某一个网页中的颜色，</font><font style="color:rgb(216,57,49);">我们可以借助于截图软件的拾色器插件来完成</font><font style="color:rgb(216,57,49);">。【截图软件在资料中已经提供】</font>

##### CSS选择器
顾名思义：选择器是选取需设置样式的元素（标签），但是我们根据业务场景不同，选择的标签的需求也是多种多样的，所以选择器有很多种。

**选择器通用语法如下**：

```plain
选择器名   {
    css样式名：css样式值;
    css样式名：css样式值;
}
```

而我们是做[[02-Java Web|后台开发]]的，所以对于css选择器，我们只学习常见的这几种：

| <font style="color:#1f2329;">选择器</font> | <font style="color:#1f2329;">写法</font> | <font style="color:#1f2329;">示例</font> | <font style="color:#1f2329;">示例说明</font> |
| :---: | :---: | --- | --- |
| <font style="color:rgb(27, 30, 29);">元素选择器</font> | <font style="color:rgb(0, 0, 0);">元素名称 {...}</font> | <font style="color:rgb(0, 0, 0);">h1 {...}</font> | <font style="color:rgb(27, 30, 29);">选择页面上所有的<h1>标签</font> |
| <font style="color:rgb(27, 30, 29);">类选择器</font> | <font style="color:rgb(0, 0, 0);">.class属性值 {...}</font> | <font style="color:rgb(0, 0, 0);">.cls {...}</font> | <font style="color:rgb(27, 30, 29);">选择页面上所有class属性为cls的标签</font> |
| <font style="color:rgb(27, 30, 29);">id选择器</font> | <font style="color:rgb(0, 0, 0);">#id属性值 {...}</font> | <font style="color:rgb(0, 0, 0);">#hid {...}</font> | <font style="color:rgb(27, 30, 29);">选择页面上id属性为hid的标签</font> |
| <font style="color:rgb(27, 30, 29);">分组选择器</font> | <font style="color:rgb(0, 0, 0);">选择器1,选择器2{...}</font> | <font style="color:rgb(0, 0, 0);">h1,h2 {...}</font> | <font style="color:rgb(27, 30, 29);">选择页面上所有的<h1>和<h2>标签</font> |
| <font style="color:rgb(27, 30, 29);">属性选择器</font> | <font style="color:rgb(0, 0, 0);">元素名称[属性] {...}</font> | <font style="color:rgb(0, 0, 0);">input[type] {...}</font> | <font style="color:rgb(27, 30, 29);">选择页面上有type属性的<input>标签</font> |
| | <font style="color:rgb(0, 0, 0);">元素名称[属性名="值"] {...}</font> | <font style="color:rgb(0, 0, 0);">input[type="text"] {...}</font> | <font style="color:rgb(27, 30, 29);">选择页面上type属性为text的<input>标签</font> |
| <font style="color:rgb(27, 30, 29);">后代选择器</font> | <font style="color:rgb(0, 0, 0);">元素1元素2{...}</font> | <font style="color:rgb(0, 0, 0);">form input {...}</font> | <font style="color:rgb(27, 30, 29);">选择<form>标签内的所有<input>标签</font> |

那接下来，我们需要将页面上所有的超链接中，默认的下划线效果去除掉。具体的代码实现如下：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title>
  <!-- 2. 内部样式 -->
  <style>
    .publish-date {
      color: #b2b2b2;
    }
    
    /* 设置超链接取消下划线效果 */
    a {
      text-decoration: none;
    }
  </style>
  <!-- 3. 外部样式 -->
  <!-- <link rel="stylesheet" href="css/news.css"> -->
</head>
<body>

  <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 -->
  <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1>
  
  <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 -->
  <a href="https://news.cctv.com/" target="_blank">央视网</a>

  <!-- 1. 行内样式 -->
  <!-- <span style="color: #b2b2b2;">2024年05月15日 20:07</span> -->

  <span class="publish-date">2024年05月15日 20:07</span>

</body>
</html>
```

那到目前为止，标题部分的基本排版和样式，我们就已经制作完成了，具体页面效果：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457761-06dd6cd3-4a24-4807-9fe2-9ca0f3e71a50.png)

### 央视新闻-正文
在原始的央视新闻页面中，我们可以看到有视频，有文字，有图片，内容还是非常丰富的。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457805-d8489f57-f4d4-49c1-89b3-ca60b37f9306.png)

#### 正文排版
##### 基本实现
浏览器在解析渲染页面的时候，是从上往下解析渲染的，那接下来，我们就可以从上往下来布局这个页面，那这个过程中，我们就可以直接基于AI来辅助我们实现。

正文排版之后，页面的代码如下：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title>
  <!-- 2. 内部样式 -->
  <style>
    .publish-date {
      color: #b2b2b2;
    }
    
    /* 设置超链接取消下划线效果 */
    a {
      text-decoration: none;
    }
  </style>
</head>
<body>
      
    <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 -->
    <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1>
    
    <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 -->
    <a href="https://news.cctv.com/" target="_blank">央视网</a>

    <span class="publish-date">2024年05月15日 20:07</span>
    <br>
    <br>

    <!-- 定义一个视频, video/news.mp4 -->
    <video src="video/news.mp4" controls  width="80%"></video>
    <p>
      央视网消息（新闻联播）：作为共抓长江大保护的标志性工程，长江十年禁渔今年进入第四年。总书记指出，长江禁渔是为全局计、为子孙谋的重要决策。牢记总书记嘱托，沿江省市持续推进长江水生生物多样性恢复，努力保障退捕渔民就业生活。这段时间，记者深入长江两岸，记录下禁渔工作取得的重要阶段性成效和广大干部群众坚定不移推进长江十年禁渔的扎实行动。
    </p>
    <p>
      行走在长江沿线，科研人员发现很多可喜现象。
    </p>
    <!-- 定义一张图片, img/1.gif -->
    <img src="img/1.gif" alt=""  width="100%">
    <p>
      在长江南源，一处小头裸裂尻鱼新的栖息地被发现，鱼的数量大约超3万尾，为水生态保护提供了珍贵数据。
    </p>
    <p>
      在长江中游，追踪显示，人工增殖放流的中华鲟成功入海率已经从45%左右提升至60%以上；鄱阳湖鱼类小型化、低龄化趋势得到遏制，栖息地生存环境得以改善。
    </p>
    <p>
      在长江下游，今年3月起，南京秦淮河入江口首次出现野生中华绒螯蟹大规模洄游现象，种群数量明显增加。
    </p>
    <img src="img/2.jpg" width="100%">
    <p>
      水生生物资源恢复向好，见证了长江十年禁渔三年多来的阶段性成果。
    </p>
    <p>
      实施长江十年禁渔，是以同志为核心的党中央从中华民族长远利益出发作出的重要决策。党的十八大以来，总书记多次深入长江沿线考察调研，详细了解长江十年禁渔的实施情况，他指出，要坚定推进长江十年禁渔，巩固好已经取得的成果。
    </p>
    <img src="img/3.jpg" width="100%">
    <p>
      按照部署，自2021年1月1日起，在长江干流、大型通江湖泊、重要支流和长江口部分海域实行为期十年的禁渔，常年禁止天然渔业资源的生产性捕捞。禁渔三年多来，相关评估显示，长江干流和鄱阳湖、洞庭湖水生生物完整性指数由禁渔前最差的“无鱼”提升了两个等级。2022年，长江江豚数量达到1249头，实现历史性止跌回升。长江干流水质连续4年全线保持Ⅱ类。
    </p>
    <p>
      实施长江十年禁渔，解决好渔民上岸后的生产生活问题，禁渔才有稳定扎实的社会基础。
    </p>
    <img src="img/4.jpg" width="100%">
    <p>
      安徽退捕转产的3万多名渔民，在政府的引导下接受就业培训。在当涂县，免费学习养殖技术，养殖生态螃蟹成了退捕渔民的新选择。
    </p>
    <p>
      在拥有洞庭湖超六成水域的湖南岳阳，政府帮扶上岸渔民建起养殖场，发展风干鱼产业，还带领他们学习直播带货，拓宽销路。
    </p>
    <p>
      在渔民退捕上岸的鄱阳湖棠荫岛，当地在继续保护好生态的前提下，正探索规划利用独特的自然资源发展旅游产业。禁渔三年多来，有关部门对23.1万退捕渔民逐一建档立卡，多渠道提升就业、社保水平。
    </p>
    <img src="img/5.jpg" width="100%">
    <p>
      长江十年禁渔实施以来，沿江省市合力攻坚、久久为功，长江大保护不断向纵深推进，持续巩固禁渔成果。下一步，沿江省市还将加强水生生物重要栖息地修复，建立退捕渔民动态精准帮扶服务，完善跨区域、跨部门执法合作机制，确保一江清水绵延后世、惠泽人民。
    </p>
    <img src="img/6.jpg">
  
</body>
</html>
```

**<font style="color:rgb(216,57,49);">注意：在使用类似于通义零码这类的AI辅助工具时，如果存在一些敏感数据，比如：政治、宗教、信仰等。</font>**

##### 常见标签
那在上述的正文排版中，用到了如下标签，接下来详解介绍一下：

| **<font style="color:#1f2329;">标签</font>** | **<font style="color:#1f2329;">作用</font>** | **<font style="color:#1f2329;">属性/说明</font>** |
| :---: | :---: | --- |
| <font style="color:#1f2329;"><video></font> | <font style="color:#1f2329;">视频标签</font> | <font style="color:#1f2329;">src：指定视频的url（绝对路径/相对路径）</font> |
| | | <font style="color:#1f2329;">controls：是否显示播放控件</font> |
| | | <font style="color:#1f2329;">width：宽度（像素/相对于父元素百分比）；备注: 一般width 和 height 我们只会指定一个，另外一个会自动的等比例缩放。</font> |
| | | <font style="color:#1f2329;">height：高度（像素/相对于父元素百分比）；备注: 一般width 和 height 我们只会指定一个，另外一个会自动的等比例缩放。</font> |
| <font style="color:#1f2329;"><img></font> | <font style="color:#1f2329;">图片标签</font> | <font style="color:#1f2329;">src, width，height</font> |
| <font style="color:#1f2329;"><p></font> | <font style="color:#1f2329;">段落标签</font> | |
| <font style="color:rgb(0, 0, 0);"><br></font> | <font style="color:#1f2329;">换行标签</font> | |
| <font style="color:rgb(0, 0, 0);"><b> / <strong></font> | **<font style="color:#1f2329;">加粗</font>** | <font style="color:#1f2329;"><strong> 具有强调语义</font> |
| <font style="color:rgb(0, 0, 0);"><u> / <ins></font> | <u><font style="color:#1f2329;">下划线</font></u> | <font style="color:#1f2329;"><ins> 具有强调语义</font> |
| <font style="color:rgb(0, 0, 0);"><i> / <em></font> | _<font style="color:#1f2329;">倾斜</font>_ | <font style="color:#1f2329;"><em> 具有强调语义</font> |
| <font style="color:rgb(0, 0, 0);"><s> / <del></font> | ~~<font style="color:#1f2329;">删除线</font>~~ | <font style="color:#1f2329;"><del> 具有强调语义</font> |

在HTML页面中，我们在代码中录入空格、<、> 这些符号的时候，是没有对应的效果的，因为浏览器并不能准确的识别，此时，我们就需要通过字符实体来表示空格，<, > 。常见符号的字符实体如下：

| <font style="color:#1f2329;">字符实体</font> | <font style="color:#1f2329;">属性/说明</font> |
| :---: | :---: |
| <font style="color:rgb(101, 112, 110);">&nbsp;</font> | <font style="color:rgb(101, 112, 110);">空格</font> |
| <font style="color:rgb(101, 112, 110);">&lt;</font> | <font style="color:rgb(101, 112, 110);"><</font> |
| <font style="color:rgb(101, 112, 110);">&gt;</font> | <font style="color:rgb(101, 112, 110);">></font> |

##### 路径表示
在引入图片、视频、音频、css等内容时，我们需要指定文件的路径，而在前端开发中，路径的书写形式分为两类：

- 绝对路径:
    - 绝对磁盘路径: `<img src="C:\Users\Administrator\Desktop\HTML\img\logo.png">`
    - 绝对网络路径: `<img src="``https://i2.sinaimg.cn/dy/deco/2012/0613/yocc20120613img01/news_logo.png``">`
- 相对路径:

 ./ : 当前目录 , ./ 可以省略的

 ../: 上一级目录

#### 正文样式
正文的基本排版有了之后，接下来，我们要处理的是正文部分的样式。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891457935-491082f2-641e-4595-a0b9-52a5ef4e405b.png)

具体的css样式如下:

```plain
/* 设置段落首行缩进 */
    p {
      text-indent: 2em; /* 首行缩进2em */
      line-height: 2; /* 行高2倍 */
    }
```

### 央视新闻-布局
#### 功能实现
完成了标签及正文部分的排版制作，以及样式处理之后，那最后一步，我们就要来完成页面整体布局的设置了。 从原始的央视新闻页面中，我们可以看到，新闻页面是出于整个版面的正中心的，那这种呢，在布局中也称为 **版心居中**。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891458024-e3c56f85-5b68-404c-86f5-c1b0ca197487.png)

这个功能，我们依然可以通过AI，轻而易举的实现。具体的提示词如下：

<font style="background-color:rgb(255,245,235);">通过css使如下新闻网页的整体内容，占用整个页面宽度的70%，并且横向居中展示。具体的网页内容如下：.....</font>

最终网页代码如下所示：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</title>
  <style>
    .publish-date {
      color: #b2b2b2;
    }
    
    /* 设置超链接取消下划线效果 */
    a {
      text-decoration: none;
    }

    /* 设置段落首行缩进 */
    p {
      text-indent: 2em; /* 首行缩进2em */
      line-height: 2; /* 行高2倍 */
    }

    /* 新增样式 */
    .news-content {
      width: 70%; /* 宽度占70% */
      margin: 0 auto; /* 横向居中 */
    }
  </style>
</head>
<body>
    <!-- 包裹新闻内容的容器 -->
    <div class="news-content">
      <!-- 定义网页标题, 标题内容： 【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章 -->
      <h1 id="title">【新思想引领新征程】推进长江十年禁渔 谱写长江大保护新篇章</h1>
      
      <!-- 定义一个超链接, 链接地址：https://news.cctv.com/, 链接内容：央视网 -->
      <a href="https://news.cctv.com/" target="_blank" >央视网</a>

      <span class="publish-date">2024年05月15日 20:07</span>
      <br>
      <br>

      <!-- 定义一个视频, video/news.mp4 -->
      <video src="video/news.mp4" controls width="100%"></video>
      <p>
        <strong>央视网消息</strong>（新闻联播）：作为共抓长江大保护的标志性工程，长江十年禁渔今年进入第四年。总书记指出，长江禁渔是为全局计、为子孙谋的重要决策。牢记总书记嘱托，沿江省市持续推进长江水生生物多样性恢复，努力保障退捕渔民就业生活。这段时间，记者深入长江两岸，记录下禁渔工作取得的重要阶段性成效和广大干部群众坚定不移推进长江十年禁渔的扎实行动。
      </p>
      <p>
        行走在长江沿线，科研人员发现很多可喜现象。
      </p>
      <!-- 定义一张图片, img/1.gif -->
      <img src="img/1.gif" alt=""  width="100%">
      <p>
        在长江南源，一处小头裸裂尻鱼新的栖息地被发现，鱼的数量大约超3万尾，为水生态保护提供了珍贵数据。
      </p>
      <p>
        在长江中游，追踪显示，人工增殖放流的中华鲟成功入海率已经从45%左右提升至60%以上；鄱阳湖鱼类小型化、低龄化趋势得到遏制，栖息地生存环境得以改善。
      </p>
      <p>
        在长江下游，今年3月起，南京秦淮河入江口首次出现野生中华绒螯蟹大规模洄游现象，种群数量明显增加。
      </p>
      <img src="img/2.jpg"  width="100%">
      <p>
        水生生物资源恢复向好，见证了长江十年禁渔三年多来的阶段性成果。
      </p>
      <p>
        实施长江十年禁渔，是以同志为核心的党中央从中华民族长远利益出发作出的重要决策。党的十八大以来，总书记多次深入长江沿线考察调研，详细了解长江十年禁渔的实施情况，他指出，要坚定推进长江十年禁渔，巩固好已经取得的成果。
      </p>
      <img src="img/3.jpg"  width="100%">
      <p>
        按照部署，自2021年1月1日起，在长江干流、大型通江湖泊、重要支流和长江口部分海域实行为期十年的禁渔，常年禁止天然渔业资源的生产性捕捞。禁渔三年多来，相关评估显示，长江干流和鄱阳湖、洞庭湖水生生物完整性指数由禁渔前最差的“无鱼”提升了两个等级。2022年，长江江豚数量达到1249头，实现历史性止跌回升。长江干流水质连续4年全线保持Ⅱ类。
      </p>
      <p>
        实施长江十年禁渔，解决好渔民上岸后的生产生活问题，禁渔才有稳定扎实的社会基础。
      </p>
      <img src="img/4.jpg"  width="100%">
      <p>
        安徽退捕转产的3万多名渔民，在政府的引导下接受就业培训。在当涂县，免费学习养殖技术，养殖生态螃蟹成了退捕渔民的新选择。
      </p>
      <p>
        在拥有洞庭湖超六成水域的湖南岳阳，政府帮扶上岸渔民建起养殖场，发展风干鱼产业，还带领他们学习直播带货，拓宽销路。
      </p>
      <p>
        在渔民退捕上岸的鄱阳湖棠荫岛，当地在继续保护好生态的前提下，正探索规划利用独特的自然资源发展旅游产业。禁渔三年多来，有关部门对23.1万退捕渔民逐一建档立卡，多渠道提升就业、社保水平。
      </p>
      <img src="img/5.jpg"  width="100%">
      <p>
        长江十年禁渔实施以来，沿江省市合力攻坚、久久为功，长江大保护不断向纵深推进，持续巩固禁渔成果。下一步，沿江省市还将加强水生生物重要栖息地修复，建立退捕渔民动态精准帮扶服务，完善跨区域、跨部门执法合作机制，确保一江清水绵延后世、惠泽人民。
      </p>
      <img src="img/6.jpg" >
    </div>
</body>
</html>
```

上述代码，最终经过浏览器的解析渲染之后，效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891458462-7f2b3e41-6464-4962-a4b3-1c5d07e09efb.png)

#### 盒子模型
##### 介绍
- 盒子：页面中所有的元素（标签），都可以看做是一个 盒子，由盒子将页面中的元素包含在一个矩形区域内，通过盒子的视角更方便的进行页面布局。
- 盒子模型组成：内容区域（content）、内边距区域（padding）、边框区域（border）、外边距区域（margin）。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891458475-6d46eab7-727e-423a-990d-efabfbf85325.png)

 CSS盒子模型，其实和日常生活中的包装盒是非常类似的，就比如：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891458863-0d339498-ed44-4219-b032-80970a4f491c.png)

盒子的大小，其实就包括三个部分： border、padding、content，而margin外边距是不包括在盒子之内的。

##### 布局标签
- 布局标签：实际开发网页中，会大量频繁的使用 div 和 span 这两个没有语义的布局标签。
- 标签：`<font style="color:rgb(46,161,33);"><div></font>``<font style="color:rgb(46,161,33);"><span></font>`
- 特点：
- `<font style="color:rgb(46,161,33);"><div></font>`标签：
    - 一行只显示一个（独占一行）
    - 宽度默认是父元素的宽度，高度默认由内容撑开
    - 可以设置宽高（width、height）
- `<font style="color:rgb(46,161,33);"><span></font>`标签：
    - 一行可以显示多个
    - 宽度和高度默认由内容撑开
    - 不可以设置宽高（width、height）
- 测试：

```plain
<body>
    <div>
        A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 
    </div>
    <div>
        A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 
    </div>

    <span>
        A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 
    </span>
    <span>
        A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 
    </span>
</body>
```

浏览器打开后的效果:

1). div会独占一行，默认宽度为父元素 body 的宽度。可以设置宽高（width、height）

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891458931-923981e4-bfa2-431e-92e7-674e245be704.png)

2). span一行会显示多个，用来组合行内元素，默认宽度为内容撑开的宽度。不可以设置宽高（width、height）

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891458958-ce1a2b48-56b4-4daa-b774-de2facfb81d1.png)

##### 代码实现
代码如下: 

```plain
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>盒子模型</title>
    <style>
        div {
            width: 200px;  /* 宽度 */
            height: 200px;  /* 高度 */
            box-sizing: border-box; /* 指定width height为盒子的高宽 */
            background-color: aquamarine; /* 背景色 */
            
            padding: 20px 20px 20px 20px; /* 内边距, 上 右 下 左 , 边距都一行, 可以简写: padding: 20px;*/ 
            border: 10px solid red; /* 边框, 宽度 线条类型 颜色 */
            margin: 30px 30px 30px 30px; /* 外边距, 上 右 下 左 , 边距都一行, 可以简写: margin: 30px; */
        }
    </style>
</head>

<body>
        
    <div>
        A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 
    </div>
    
</body>
</html>
```

代码编写好了, 可以通过浏览器打开该页面, 通过开发者工具,我们就可以看到盒子的大小 , 以及盒子各个组成部分(内容、内边距、边框、外边距)：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891459309-c910937a-3998-47e4-9944-4163141fe676.png)

我们也可以，通过浏览器的开发者工具，清晰的看到这个盒子，以及每一个部分的大小：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891459382-8aa14150-4eb8-40e8-ad6e-cf92ceb06460.png)

**备注：**

- 上述的padding、margin属性值，可以是4个值、也可以是两个值、也可以是一个值，具体的含义如下：
- `padding: 20px 20px 20px 20px;` -------> 表示上、右、下、左都是20px；
- `padding: 20px 10px;` ----------------------> 表示上下是20px，左右是10px；
- `padding: 20px;` -----------------------------> 表示上、右、下、左都是20px；

### 案例
#### 需求
通过一个央视新闻页面的制作，大家已经熟悉了HTML中的常见标签及CSS中基础样式的写法及作用。 那接下来呢，我们就要通过一个案例，来加深大家对于这些标签和样式的掌握和使用，那么在完成这个案例的过程中呢，我们依然可以直接基于AI来辅助我们快速实现。

**需求：参照Tlias智能学习辅助系统，完成员工管理页面的制作。 **

产品经理制作的页面原型如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891459474-fa535864-8d75-4698-8f17-819431086685.png)

#### 代码实现
##### 顶部导航栏
###### 基本实现
原型效果：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891459543-c4d24f6a-4c1f-48e9-afe0-4a5d2639ebb3.png)

<font style="background-color:rgb(255,245,235);">提示词（prompt）：</font>

<font style="background-color:rgb(255,245,235);">你是一名前端开发工程师，帮我生成一个HTML页面，页面整体有4个部分组成，先来实现第一个部分：</font>

<font style="background-color:rgb(255,245,235);">1. 顶栏</font>

<font style="background-color:rgb(255,245,235);">内容：包含左侧的标题“Tlias智能学习辅助系统”，字体需加大加粗，以突出显示；右侧则放置“退出登录”文字链接。</font>

<font style="background-color:rgb(255,245,235);">布局：确保标题与退出登录文本位于同一行内，分别左对齐与右对齐 。</font>

页码代码如下：

```plain
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tlias智能学习辅助系统</title>
    <style>
      body {
        margin: 0;
      }

      /* 顶栏样式 */
      .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #f1f1f1;
          padding: 10px 20px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      }
      
      /* 加大加粗标题 */
      .header h1 {
          margin: 0;
          font-size: 24px;
          font-weight: bold;
      }

      /* 文本链接样式 */
      .header a {
          text-decoration: none;
          color: #333;
          font-size: 16px;
      }
    </style>
</head>
<body>
    <!-- 顶栏 -->
    <div class="header">
        <h1>Tlias智能学习辅助系统</h1>
        <a href="#">退出登录</a>
    </div>

    <!-- 其他部分可以在这里添加 -->
</body>
</html>
```

页面展示效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891459686-b4857bba-6610-4473-b67f-09d28bc831d3.png)

###### flex布局
那在上述的案例代码中，其实我们用到了一种布局模式，叫 **flex布局**。

- flex是flexible Box的缩写，意为"弹性布局"。采用flex布局的元素，称为Flex容器（container），它的所有子元素自动成为容器成员，称为Flex项目（item）。
- <font style="color:rgb(216,57,49);">通过给父容器添加flex属性,来控制子元素的位置和排列方式。</font>

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891459922-9aea19d7-f3ef-4aca-ad9f-99b871cfcc6e.png)

测试代码如下：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    #container {
      display: flex;
      /* justify-content: space-between; */ /* 先两边贴边，再平分剩余空间 */
      /* justify-content: flex-start;*/ /* 从头开始排列  */
      /* justify-content: flex-end; */ /* 从尾开始排列 */
      /* justify-content: center; */ /* 居中排列 */
      /* justify-content: space-around; */ /* 两边留白，中间平分，平分剩余空间 */
      flex-direction: row;
      justify-content: space-between;
      background-color: #aeea6a;
      width: 400px;
      height: 300px;
    }

    #container div {
      background-color: #e866ef;
      width: 100px;
      height: 50px; 
    }
  </style>
</head>
<body>
  <div id="container">
    <div>Flex Item</div>
    <div>Flex Item</div>
    <div>Flex Item</div>
  </div>
</body>
</html>
```

- flex布局相关的CSS样式：

| **<font style="color:#1f2329;">属性</font>** | **<font style="color:#1f2329;">说明</font>** | **<font style="color:#1f2329;">取值</font>** | **<font style="color:#1f2329;">含义</font>** |
| :---: | :---: | :---: | --- |
| <font style="color:rgb(40, 45, 44);">display</font> | <font style="color:rgb(40, 45, 44);">模式</font> | <font style="color:rgb(40, 45, 44);">flex</font> | <font style="color:rgb(40, 45, 44);">使用flex布局</font> |
| <font style="color:rgb(40, 45, 44);">flex-direction</font> | <font style="color:rgb(40, 45, 44);">设置主轴</font> | <font style="color:rgb(40, 45, 44);">row</font> | <font style="color:rgb(40, 45, 44);">主轴方向为x轴，水平向右。（默认）</font> |
| | | <font style="color:rgb(40, 45, 44);">column</font> | <font style="color:rgb(40, 45, 44);">主轴方向为y轴，垂直向下。</font> |
| <font style="color:rgb(40, 45, 44);">justify-content</font> | <font style="color:rgb(40, 45, 44);">子元素在主轴上的对齐方式</font> | <font style="color:rgb(40, 45, 44);">flex-start</font> | <font style="color:rgb(40, 45, 44);">从头开始排列</font> |
| | | <font style="color:rgb(40, 45, 44);">flex-end</font> | <font style="color:rgb(40, 45, 44);">从尾部开始排列</font> |
| | | <font style="color:rgb(40, 45, 44);">center</font> | <font style="color:rgb(40, 45, 44);">在主轴居中对齐</font> |
| | | <font style="color:rgb(40, 45, 44);">space-around</font> | <font style="color:rgb(40, 45, 44);">平分剩余空间</font> |
| | | <font style="color:rgb(40, 45, 44);">space-between</font> | <font style="color:rgb(40, 45, 44);">先两边贴边，再平分剩余空间</font> |

如果主轴设置为row，其实就是横向布局。 主轴设置为column，其实就是纵向布局。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460010-c801615b-0d7a-46d2-aa05-259ee417a579.png)

##### 搜索表单
那接下来，我们要完成的是第二个部分，也就是搜索栏的制作。 页面原型展示如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460123-0577c4fd-eb62-492d-8095-0f5b630a2948.png)

那这里呢，需要用到HTML中的表单。 那接下来，我们先来介绍一下表单标签，然后再来实现搜索表单栏的制作。

###### 表单标签
那表单呢,在我们日常的上网的过程中,基本上每天都会遇到。比如，我们经常在访问网站时，出现的登录页面、注册页面、个人信息提交页面，其实都是一个一个的表单 。 当我们在这些表单中录入数据之后，一点击 "提交"，就会将表单中我们填写的数据采集到，并提交， 那其实这个数据呢，一般会提交到服务端，最终保存在数据库中 （后面的课程中会讲到）。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460067-720e47fd-7b12-4602-ade9-5f79f7779e29.png)

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460127-287ba6ce-e3f4-403f-915e-22ff5b68d0a7.png)

那其实，上述的整个窗口是一个表单，而表单是一项一项的，这个我们称为表单项 或 表单元素。

- 表单场景: 表单就是在网页中负责数据采集功能的，如：注册、登录的表单。 
- 表单标签: `<form>`
- 表单属性:
    - `action`: 规定表单提交时，向何处发送表单数据，表单提交的URL。
    - `method`: 规定用于发送表单数据的方式，常见为： GET、POST。
        * `GET`：表单数据是拼接在url后面的， 如： xxxxxxxxxxx?username=Tom&age=12，url中能携带的表单数据大小是有限制的。
        * `POST`： 表单数据是在请求体（消息体）中携带的，大小没有限制。
- 表单项标签: 不同类型的input元素、下拉列表、文本域等。
    - `input`: 定义表单项，通过type属性控制输入形式
    - `select`: 定义下拉列表
    - `textarea`: 定义文本域

**演示：**

1). GET方式提交的表单

```plain
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML-表单</title>
</head>
<body>
    <!-- 
    form表单属性: 
        action: 表单提交的url, 往何处提交数据 . 如果不指定, 默认提交到当前页面
        method: 表单的提交方式 .
            get: 在url后面拼接表单数据, 比如: ?username=Tom&age=12 , url长度有限制 . 默认值
            post: 在消息体(请求体)中传递的, 参数大小无限制的.
    -->   
        
    <form action="" method="get">
        用户名: <input type="text" name="username">
        年龄: <input type="text" name="age">

        <input type="submit" value="提交">
    </form>
        
</body>
</html>
```

表单编写完毕之后，通过浏览器打开此表单，然后再表单项中录入值之后，点击提交，我们会看到表单的数据在url后面提交到服务端，格式为：?username=Tom&age=12。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460492-90f29547-d450-49c5-ae3f-a5410a91e113.png)

2). POST方式提交表单

将上述的表单提交方式由get，改为post

```plain
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML-表单</title>
</head>
<body>
    <!-- 
    form表单属性: 
        action: 表单提交的url, 往何处提交数据 . 如果不指定, 默认提交到当前页面
        method: 表单的提交方式 .
            get: 在url后面拼接表单数据, 比如: ?username=Tom&age=12 , url长度有限制 . 默认值
            post: 在消息体(请求体)中传递的, 参数大小无限制的.
    -->   
        
    <form action="" method="post">
        用户名: <input type="text" name="username">
        年龄: <input type="text" name="age">

        <input type="submit" value="提交">
    </form>
        
</body>
</html>
```

表单编写完毕之后，通过浏览器打开此表单，然后再表单项中录入值之后，点击提交，我们会看到表单的数据在url后面提交到服务端，格式为：?username=Tom&age=12。

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460637-8b67fb64-2cc0-4063-90bc-5eda8f305d77.png)

**<font style="color:rgb(216,57,49);">注意事项：</font>**

表单中的所有表单项，要想能够正常的采集数据，在提交的时候能提交到服务端，表单项必须指定name属性。 否则，无法提交该表单项。

```plain
用户名: <input type="text" name="username">
```

###### 表单项标签
在一个表单中，可以存在很多的表单项，而虽然表单项的形式各式各样，但是表单项的标签其实就只有三个，分别是：

- `<input>`: 表单项 , 通过type属性控制输入形式。

| **<font style="color:rgb(0, 0, 0);">type取值</font>** | **<font style="color:rgb(0, 0, 0);">描述</font>** |
| --- | --- |
| <font style="color:rgb(0, 0, 0);">text</font> | <font style="color:rgb(0, 0, 0);">默认值，定义单行的输入字段</font> |
| <font style="color:rgb(0, 0, 0);">password</font> | <font style="color:rgb(0, 0, 0);">定义密码字段</font> |
| <font style="color:rgb(0, 0, 0);">radio</font> | <font style="color:rgb(0, 0, 0);">定义单选按钮</font> |
| <font style="color:rgb(0, 0, 0);">checkbox</font> | <font style="color:rgb(0, 0, 0);">定义复选框</font> |
| <font style="color:rgb(0, 0, 0);">file</font> | <font style="color:rgb(0, 0, 0);">定义文件上传按钮</font> |
| <font style="color:rgb(0, 0, 0);">date/time/datetime-local</font> | <font style="color:rgb(0, 0, 0);">定义日期/时间/日期时间</font> |
| <font style="color:rgb(0, 0, 0);">number</font> | <font style="color:rgb(0, 0, 0);">定义数字输入框</font> |
| <font style="color:rgb(0, 0, 0);">email</font> | <font style="color:rgb(0, 0, 0);">定义邮件输入框</font> |
| <font style="color:rgb(0, 0, 0);">hidden</font> | <font style="color:rgb(0, 0, 0);">定义隐藏域</font> |
| <font style="color:rgb(0, 0, 0);">submit / reset / button</font> | <font style="color:rgb(0, 0, 0);">定义提交按钮 / 重置按钮 / 可点击按钮</font> |

- `<select>`: 定义下拉列表, `<option>` 定义列表项
- `<textarea>`: 文本域

**演示：**

创建一个新的表单项的html文件，具体内容如下：

```plain
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML-表单项标签</title>
</head>
<body>

<!-- value: 表单项提交的值 -->
<form action="/save" method="post">
     姓名: <input type="text" name="name"> <br><br>

     密码: <input type="password" name="password"> <br><br> 

     性别: <input type="radio" name="gender" value="1"> 男
          <label><input type="radio" name="gender" value="2"> 女 </label> <br><br>
     
     爱好: <label><input type="checkbox" name="hobby" value="java"> java </label>
          <label><input type="checkbox" name="hobby" value="game"> game </label>
          <label><input type="checkbox" name="hobby" value="sing"> sing </label> <br><br>
     
     图像: <input type="file" name="image">  <br><br>

     生日: <input type="date" name="birthday"> <br><br>

     时间: <input type="time" name="time"> <br><br>

     日期时间: <input type="datetime-local" name="datetime"> <br><br>

     学历: <select name="degree">
               <option value="">----------- 请选择 -----------</option>
               <option value="1">大专</option>
               <option value="2">本科</option>
               <option value="3">硕士</option>
               <option value="4">博士</option>
          </select>  <br><br>

     描述: <textarea name="description" cols="30" rows="10"></textarea>  <br><br>
     
     <input type="hidden" name="id" value="1">

     <!-- 表单常见按钮 -->
     <input type="button" value="按钮">
     <input type="reset" value="重置"> 
     <input type="submit" value="提交">   
     <br>
</form>

</body>
</html>
```

通过浏览器打开上述的表单项html文件，最终展示出的表单信息如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460628-005d3620-b398-4038-85c6-dfaf065959f6.png)

而对于`<input type="hidden">`，是一个隐藏域，在表单中并不会显示出来，但是在提交表单的时候，是会提交到服务端的。 接下来，我们就点击提交按钮，来提交当前表单，看看提交的数据：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460673-2ef4785d-c977-46fa-87ce-71324b6de55e.png)

###### 搜索表单实现
那基本的表单标签和表单项标签，讲解完毕后，接下来呢，我们就来完成搜索表单的实现，同样，我们可以借助于AI帮我们完成对应的页面布局。

<font style="background-color:rgb(255,245,235);">提示词（prompt）：</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">再继续帮我生成第二个部分: 2. 搜索表单区域</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">组成：包括三个输入控件和两个操作按钮。输入控件具体为：姓名（文本输入框）、性别（下拉选择，选项包括 男/女， 默认为空）、职位（下拉选择，选项包括班主任、讲师、学工主管、教研主管、咨询师， 默认为空）。</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">按钮：“查询”与“清空”按钮，用于提交表单或重置表单项 。</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">布局：所有表单项及按钮需水平排列于一行 ，确保美观大气 。</font>

代码实现如下：

```plain
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tlias智能学习辅助系统</title>
    <style>
      body {
        margin: 0;
      }

      /* 顶栏样式 */
      .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #f1f1f1;
          padding: 10px 20px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      }
      
      /* 加大加粗标题 */
      .header h1 {
          margin: 0;
          font-size: 24px;
          font-weight: bold;
      }

      /* 文本链接样式 */
      .header a {
          text-decoration: none;
          color: #333;
          font-size: 16px;
      }

      /* 搜索表单区域 */
      .search-form {
          display: flex;
          align-items: center;
          padding: 20px;
          background-color: #f9f9f9;
      }

      /* 表单控件样式 */
      .search-form input[type="text"], .search-form select {
          margin-right: 10px;
          padding: 5px 10px;
          border: 1px solid #ccc;
          border-radius: 4px;
          width: 200px;
      }

      /* 按钮样式 */
      .search-form button {
          padding: 5px 15px;
          margin-left: 10px;
          background-color: #007bff;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
      }

      /* 清空按钮样式 */
      .search-form button.clear {
          background-color: #6c757d;
      }
    </style>
</head>
<body>
    <!-- 顶栏 -->
    <div class="header">
        <h1>Tlias智能学习辅助系统</h1>
        <a href="#">退出登录</a>
    </div>

    <!-- 搜索表单区域 -->
    <form class="search-form">
      <input type="text" name="name" placeholder="姓名" />
      <select name="gender">
          <option value="">性别</option>
          <option value="1">男</option>
          <option value="2">女</option>
      </select>
      <select name="job">
          <option value="">职位</option>
          <option value="1">班主任</option>
          <option value="2">讲师</option>
          <option value="3">学工主管</option>
          <option value="4">教研主管</option>
          <option value="5">咨询师</option>
      </select>
      <button type="submit">查询</button>
      <button type="reset" class="clear">清空</button>
    </form>

</body>
</html>
```

浏览器呈现效果为：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460664-29d599da-95ad-4d82-a910-c5635bdd6d62.png)

##### 表格数据展示
###### 基本实现
页面效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891460974-2d49c919-768a-47b5-862b-0c20c74abe35.png)

<font style="background-color:rgb(255,245,235);">提示词（prompt）：</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">再继续帮我生成第三个部分: 3. 表格展示区</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">表格结构：展示列包括姓名、性别（显示男/女）、头像（小图标展示）、职位（显示班主任/讲师/学工主管/教研主管/咨询师）、入职日期、最后操作时间、操作（里包含两个按钮 编辑 与 删除）。</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">数据模拟：基于《笑傲江湖》小说人物生成4条虚拟数据，每条数据应包含上述所有列的信息，以体现实际应用场景 。</font>

<font style="color:rgb(143,149,158);background-color:rgb(255,245,235);">样式：可适当调整表格样式，确保美观大气。</font>

代码实现为：

```plain
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tlias智能学习辅助系统</title>
    <style>
      body {
        margin: 0;
      }

      /* 顶栏样式 */
      .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #f1f1f1;
          padding: 10px 20px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      }
      
      /* 加大加粗标题 */
      .header h1 {
          margin: 0;
          font-size: 24px;
          font-weight: bold;
      }

      /* 文本链接样式 */
      .header a {
          text-decoration: none;
          color: #333;
          font-size: 16px;
      }

      /* 搜索表单区域 */
      .search-form {
          display: flex;
          align-items: center;
          padding: 20px;
          background-color: #f9f9f9;
      }

      /* 表单控件样式 */
      .search-form input[type="text"], .search-form select {
          margin-right: 10px;
          padding: 5px 10px;
          border: 1px solid #ccc;
          border-radius: 4px;
          width: 200px;
      }

      /* 按钮样式 */
      .search-form button {
          padding: 5px 15px;
          margin-left: 10px;
          background-color: #007bff;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
      }

      /* 清空按钮样式 */
      .search-form button.clear {
        background-color: #6c757d;
      }

      .table {
         min-width: 100%; 
         border-collapse: collapse;
         margin: 0 20px;
      }

      /* 设置表格单元格边框 */
      .table td, .table th { 
        border: 1px solid #ddd; 
        padding: 8px; 
        text-align: center;
      }
      
      .avatar { 
        width: 50px; 
        height: 50px; 
        object-fit: cover; 
        border-radius: 50%; 
      }

    </style>
</head>
<body>
    <!-- 顶栏 -->
    <div class="header">
        <h1>Tlias智能学习辅助系统</h1>
        <a href="#">退出登录</a>
    </div>

    <!-- 搜索表单区域 -->
    <form class="search-form" action="#" method="post">
      <input type="text" name="name" placeholder="姓名" />
      <select name="gender">
          <option value="">性别</option>
          <option value="1">男</option>
          <option value="2">女</option>
      </select>
      <select name="job">
          <option value="">职位</option>
          <option value="1">班主任</option>
          <option value="2">讲师</option>
          <option value="3">学工主管</option>
          <option value="4">教研主管</option>
          <option value="5">咨询师</option>
      </select>
      <button type="submit">查询</button>
      <button type="reset" class="clear">清空</button>
    </form>

    <table class="table table-striped table-bordered">
      <thead>
          <tr>
              <th>姓名</th>
              <th>性别</th>
              <th>头像</th>
              <th>职位</th>
              <th>入职日期</th>
              <th>最后操作时间</th>
              <th>操作</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>令狐冲</td>
              <td>男</td>
              <td><img src="https://via.placeholder.com/50" alt="令狐冲" class="avatar"></td>
              <td>讲师</td>
              <td>2021-03-15</td>
              <td>2023-07-30T12:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>任盈盈</td>
              <td>女</td>
              <td><img src="https://via.placeholder.com/50" alt="任盈盈" class="avatar"></td>
              <td>学工主管</td>
              <td>2020-04-10</td>
              <td>2023-07-29T15:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>岳不群</td>
              <td>男</td>
              <td><img src="https://via.placeholder.com/50" alt="岳不群" class="avatar"></td>
              <td>教研主管</td>
              <td>2019-01-01</td>
              <td>2023-07-30T10:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>宁中则</td>
              <td>女</td>
              <td><img src="https://via.placeholder.com/50" alt="宁中则" class="avatar"></td>
              <td>班主任</td>
              <td>2018-06-01</td>
              <td>2023-07-29T09:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
      </tbody>
  </table>

</body>
</html>
```

页面展示的效果为：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891461284-6278b28e-ac06-45bb-943d-a8b41040267c.png)

###### 表格标签
| <font style="color:#1f2329;">标签</font> | <font style="color:#1f2329;">描述</font> |
| :---: | :---: |
| <font style="color:rgb(192, 0, 0);"><table></font> | <font style="color:#1f2329;">定义表格整体</font> |
| <font style="color:rgb(192, 0, 0);"><thead></font> | <font style="color:#1f2329;">用于定义表格头部(可选)</font> |
| <font style="color:rgb(192, 0, 0);"><tbody></font> | <font style="color:#1f2329;">定义表格中的主体部分(可选)</font> |
| <font style="color:rgb(192, 0, 0);"><tr></font> | <font style="color:#1f2329;">表格的行，可以包裹多个 <td></font> |
| <font style="color:rgb(192, 0, 0);"><td></font> | <font style="color:#1f2329;">表格单元格(普通)，可以包裹内容；如果是表头单元格，可以替换为 <th></font> |

##### 底部版权区域
页面原型展示如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891461133-299d742c-71ca-48d3-9051-2cb7703346d3.png)

<font style="background-color:rgb(255,245,235);">提示词（prompt）:</font>

<font style="background-color:rgb(255,245,235);">再继续帮我生成第二个部分: 4. 页脚版权区域</font>

<font style="background-color:rgb(255,245,235);">内容：第一行显示公司全称“江苏传智播客教育科技股份有限公司”；第二行展示版权信息，“版权所有 Copyright 2006-2024 All Rights Reserved”。</font>

<font style="background-color:rgb(255,245,235);">设计：该区域应具有灰色背景，字体颜色为白色，居中对齐，以营造专业且统一的视觉效果 。</font>

页面代码如下：

```plain
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tlias智能学习辅助系统</title>
    <style>
      body {
        margin: 0;
      }

      /* 顶栏样式 */
      .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #f1f1f1;
          padding: 10px 20px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      }
      
      /* 加大加粗标题 */
      .header h1 {
          margin: 0;
          font-size: 24px;
          font-weight: bold;
      }

      /* 文本链接样式 */
      .header a {
          text-decoration: none;
          color: #333;
          font-size: 16px;
      }

      /* 搜索表单区域 */
      .search-form {
          display: flex;
          align-items: center;
          padding: 20px;
          background-color: #f9f9f9;
      }

      /* 表单控件样式 */
      .search-form input[type="text"], .search-form select {
          margin-right: 10px;
          padding: 5px 10px;
          border: 1px solid #ccc;
          border-radius: 4px;
          width: 200px;
      }

      /* 按钮样式 */
      .search-form button {
          padding: 5px 15px;
          margin-left: 10px;
          background-color: #007bff;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
      }

      /* 清空按钮样式 */
      .search-form button.clear {
        background-color: #6c757d;
      }

      .table {
         min-width: 100%; 
         border-collapse: collapse;
         margin: 0 20px;
      }

      /* 设置表格单元格边框 */
      .table td, .table th { 
        border: 1px solid #ddd; 
        padding: 8px; 
        text-align: center;
      }
      
      .avatar { 
        width: 50px; 
        height: 50px; 
        object-fit: cover; 
        border-radius: 50%; 
      }

      /* 页脚版权区域 */
    .footer {
        background-color: #8f8c8c;
        color: white;
        text-align: center;
        padding: 20px 0;
        margin-top: 30px;
    }

    .footer .company-name {
        font-size: 1.1em;
        font-weight: bold;
    }

    .footer .copyright {
        font-size: 0.9em;
    }
    </style>
</head>
<body>
    <!-- 顶栏 -->
    <div class="header">
        <h1>Tlias智能学习辅助系统</h1>
        <a href="#">退出登录</a>
    </div>

    <!-- 搜索表单区域 -->
    <form class="search-form" action="#" method="post">
      <input type="text" name="name" placeholder="姓名" />
      <select name="gender">
          <option value="">性别</option>
          <option value="1">男</option>
          <option value="2">女</option>
      </select>
      <select name="job">
          <option value="">职位</option>
          <option value="1">班主任</option>
          <option value="2">讲师</option>
          <option value="3">学工主管</option>
          <option value="4">教研主管</option>
          <option value="5">咨询师</option>
      </select>
      <button type="submit">查询</button>
      <button type="reset" class="clear">清空</button>
    </form>

    <table class="table table-striped table-bordered">
      <thead>
          <tr>
              <th>姓名</th>
              <th>性别</th>
              <th>头像</th>
              <th>职位</th>
              <th>入职日期</th>
              <th>最后操作时间</th>
              <th>操作</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>令狐冲</td>
              <td>男</td>
              <td><img src="https://via.placeholder.com/50" alt="令狐冲" class="avatar"></td>
              <td>讲师</td>
              <td>2021-03-15</td>
              <td>2023-07-30T12:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>任盈盈</td>
              <td>女</td>
              <td><img src="https://via.placeholder.com/50" alt="任盈盈" class="avatar"></td>
              <td>学工主管</td>
              <td>2020-04-10</td>
              <td>2023-07-29T15:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>岳不群</td>
              <td>男</td>
              <td><img src="https://via.placeholder.com/50" alt="岳不群" class="avatar"></td>
              <td>教研主管</td>
              <td>2019-01-01</td>
              <td>2023-07-30T10:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>宁中则</td>
              <td>女</td>
              <td><img src="https://via.placeholder.com/50" alt="宁中则" class="avatar"></td>
              <td>班主任</td>
              <td>2018-06-01</td>
              <td>2023-07-29T09:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
      </tbody>
  </table>

  <!-- 页脚版权区域 -->
  <footer class="footer">
    <p class="company-name">江苏传智播客教育科技股份有限公司</p>
    <p class="copyright">版权所有 Copyright 2006-2024 All Rights Reserved</p>
  </footer>

</body>
</html>
```

页面展示如下：

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891461238-34b92a69-2f5c-40bb-9a7c-fe9b29a8dc1d.png)

##### 版心居中
这个案例类似于央视新闻页面，页面中的内容，都需要居中显示，所以这里呢，我们就可以使用盒子模型来进行布局。具体代码如下：

```plain
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tlias智能学习辅助系统</title>
    <style>
      body {
        margin: 0;
      }

      /* 顶栏样式 */
      .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color:  #c2c0c0;
          padding: 10px 20px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      }
      
      /* 加大加粗标题 */
      .header h1 {
          margin: 0;
          font-size: 24px;
          font-weight: bold;
      }

      /* 文本链接样式 */
      .header a {
          text-decoration: none;
          color: #333;
          font-size: 16px;
      }

      /* 搜索表单区域 */
      .search-form {
          display: flex;
          align-items: center;
          padding: 20px;
          background-color: #f9f9f9;
      }

      /* 表单控件样式 */
      .search-form input[type="text"], .search-form select {
          margin-right: 10px;
          padding: 5px 10px;
          border: 1px solid #ccc;
          border-radius: 4px;
          width: 200px;
      }

      /* 按钮样式 */
      .search-form button {
          padding: 5px 15px;
          margin-left: 10px;
          background-color: #007bff;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
      }

      /* 清空按钮样式 */
      .search-form button.clear {
        background-color: #6c757d;
      }

      .table {
         min-width: 100%; 
         border-collapse: collapse;
      }

      /* 设置表格单元格边框 */
      .table td, .table th { 
        border: 1px solid #ddd; 
        padding: 8px; 
        text-align: center;
      }
      
      .avatar { 
        width: 30px; 
        height: 30px; 
        object-fit: cover; 
        border-radius: 50%; 
      }

      /* 页脚版权区域 */
    .footer {
        background-color: #c2c0c0;
        color: white;
        text-align: center;
        padding: 10px 0;
        margin-top: 30px;
    }

    .footer .company-name {
        font-size: 1.1em;
        font-weight: bold;
    }

    .footer .copyright {
        font-size: 0.9em;
    }

    #container {
      width: 80%;
      margin: 0 auto;
    }
    </style>
</head>
<body>
    
  <div id="container">
    <!-- 顶栏 -->
    <div class="header">
      <h1>Tlias智能学习辅助系统</h1>
      <a href="#">退出登录</a>
    </div>

    <!-- 搜索表单区域 -->
    <form class="search-form" action="#" method="post">
      <input type="text" name="name" placeholder="姓名" />
      <select name="gender">
          <option value="">性别</option>
          <option value="male">男</option>
          <option value="female">女</option>
      </select>
      <select name="position">
          <option value="">职位</option>
          <option value="班主任">班主任</option>
          <option value="讲师">讲师</option>
          <option value="学工主管">学工主管</option>
          <option value="教研主管">教研主管</option>
          <option value="咨询师">咨询师</option>
      </select>
      <button type="submit">查询</button>
      <button type="reset" class="clear">清空</button>
    </form>

    <table class="table table-striped table-bordered">
      <thead>
          <tr>
              <th>姓名</th>
              <th>性别</th>
              <th>头像</th>
              <th>职位</th>
              <th>入职日期</th>
              <th>最后操作时间</th>
              <th>操作</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>令狐冲</td>
              <td>男</td>
              <td><img src="https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/1.jpg" alt="令狐冲" class="avatar"></td>
              <td>讲师</td>
              <td>2021-03-15</td>
              <td>2023-07-30T12:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>任盈盈</td>
              <td>女</td>
              <td><img src="https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/1.jpg" alt="任盈盈" class="avatar"></td>
              <td>学工主管</td>
              <td>2020-04-10</td>
              <td>2023-07-29T15:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>岳不群</td>
              <td>男</td>
              <td><img src="https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/1.jpg" alt="岳不群" class="avatar"></td>
              <td>教研主管</td>
              <td>2019-01-01</td>
              <td>2023-07-30T10:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
          <tr>
              <td>宁中则</td>
              <td>女</td>
              <td><img src="https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/1.jpg" alt="宁中则" class="avatar"></td>
              <td>班主任</td>
              <td>2018-06-01</td>
              <td>2023-07-29T09:00:00Z</td>
              <td class="btn-group">
                  <button>编辑</button>
                  <button>删除</button>
              </td>
          </tr>
      </tbody>
    </table>

    <!-- 页脚版权区域 -->
    <footer class="footer">
      <p class="company-name">江苏传智播客教育科技股份有限公司</p>
      <p class="copyright">版权所有 Copyright 2006-2024 All Rights Reserved</p>
    </footer>

  </div>

</body>
</html>
```

页面效果如下:

![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1752891461344-eddcfe09-3dd4-44cb-bf63-56c278581a71.png)
