# Python学习笔记2-web基础知识

### POST和GET请求区别

**GET和POST与数据如何传递没有关系**



GET和POST是由HTTP协议定义的。在HTTP协议中，Method和Data（URL， Body， Header）是正交的两个概念，也就是说，使用哪个Method与应用层的数据如何传输是没有相互关系的。

HTTP没有要求，如果Method是POST数据就要放在BODY中。也没有要求，如果Method是GET，数据（参数）就一定要放在URL中而不能放在BODY中。

那么，网上流传甚广的这个说法是从何而来的呢？我在HTML标准中，找到了相似的描述。这和网上流传的说法一致。但是这只是HTML标准对HTTP协议的用法的约定。怎么能当成GET和POST的区别呢？

而且，现代的Web Server都是支持GET中包含BODY这样的请求。虽然这种请求不可能从浏览器发出，但是现在的Web Server又不是只给浏览器用，已经完全地超出了HTML服务器的范畴



**HTTP协议对GET和POST都没有对长度的限制**

HTTP协议明确地指出了，HTTP头和Body都没有长度的要求。而对于URL长度上的限制，有两方面的原因造成：

1. 浏览器。据说早期的浏览器会对URL长度做限制。据说IE对URL长度会限制在2048个字符内（流传很广，而且无数同事都表示认同）。但我自己试了一下，我构造了90K的URL通过IE9访问live.com，是正常的。网上的东西，哪怕是Wikipedia上的，也不能信。



2. 服务器。URL长了，对服务器处理也是一种负担。原本一个会话就没有多少数据，现在如果有人恶意地构造几个几M大小的URL，并不停地访问你的服务器。服务器的最大并发数显然会下降。另一种攻击方式是，把告诉服务器Content-Length是一个很大的数，然后只给服务器发一点儿数据，嘿嘿，服务器你就傻等着去吧。哪怕你有超时设置，这种故意的次次访问超时也能让服务器吃不了兜着走。有鉴于此，多数服务器出于安全啦、稳定啦方面的考虑，会给URL长度加限制。但是这个限制是针对所有HTTP请求的，与GET、POST没有关系。

**安全不安全和GET、POST没有关系** 

### HTTP 状态码

 [*HTTP状态码*](http://tools.jb51.net/table/http_status_code)（英语：*HTTP* Status Code）是用以表示网页服务器超文本传输协议响应*状态*的3位数字代码。 

200 成功

4XX 404 页面不存在

5XX 500 服务器内部错误

### Beautifulsoup 和xpath的比较

###### 什么是XPath？

- XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历

###### 什么是BeautifulSoup4？

* 和 lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据 

###### BeautifulSoup4和XPath的区别

> Beautifulsoup4 要比Xpath解析数据要慢，因为beautifulsoup4载入的是整个html文档

[参考](https://www.jianshu.com/p/e43699b732e6)

[图书比价工具代码]( https://blog.csdn.net/weixin_41710054/article/details/102772649 )

