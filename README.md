# fake-tapechat
一个在朋友圈吹牛的产物(

~~但是这却是我第一个正经的开源项目~~

# 前期准备
	作为科技爱好者,并为了展现实力,一定会做全平台的应用
	我要做的,大概需要html+css+js+python+数据库+(Flutter/swift+swiftUI)+(java/kotlin)+(vercel/electron
## 网页
	家境贫寒没钱买云服务器,sb政府和运营商又不给公网ip了,所以就要利用白嫖的力量(
	web仅有姐姐上大学的html+css+js方面的书里的知识(css完全不会
### 网页搭建
	发现了vercel和github page两个可以白嫖的平台
### 后端
	会点python,但是完全不会后端
### 数据库
	完全不会(

## Android
	会点kotlin, java也还行,简单页面搞得定(搭配YouTube和BilBili)

## iOS
	非常熟练,swift非常人性化,代码很简单(

## 电脑端
	windows开发,也就会个hello world和五子棋

	macOS开发和iOS一起就做了

	Linux不会

	方案:electron(网页套壳)

	还是活成了讨厌的模样

哪位大佬可以提供帮助,请联系我,谢谢.

ps:本项目采用MIT协议开源.

# 0.0.1
基于Python的flask模块

## 配置
```shell
pip install flask
```

## 运行
```shell
python3 main.py
```

ps:感谢cyh提供的代码

# 0.0.3
~~0.0.2没啥更新就不写了~~
## new features
### Dark mode
css中添加这段代码，可以让网页在深色模式下背景改为黑色
```css
@media (prefers-color-scheme: dark) {
  body {
    background: #222;
    color: #eee;
  }
}
```
by:kyoukawa(jc)
### error.html
当密码错误，或重复注册（或有人试图盗号 时跳转至此网页
by:ChenYuHe
### 返回首页&&首页导航
```html
<!-- 返回首页 -->
<a href = "/"> 返回首页 </a>

<!-- 跳转，例如signup -->
<a href = "/signup"> 注册 </a>
```
by: kyoukawa(jc) && ChengYuHe

### 背景图片
~~已经被姜川删除(~~
by:ChengYuHe
