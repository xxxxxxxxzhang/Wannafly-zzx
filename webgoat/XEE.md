# XEE

### 概念

这节课将教您如何执行XML外部实体攻击，以及如何滥用和保护它。

**目标**

- 用户应该具有基本的XML知识

- 用户将理解XML解析器是如何工作的

- 用户将学习执行XXE攻击和如何保护它

  

[XML实体注入学习](jianshu.com/p/a1ea825aa485)

### 什么是XML实体?



XML实体允许定义将在解析XML文档时由内容替换的标记。一般有三种实体:

- 内部实体

- 外部实体

- 参数实体。

一个实体必须在文档类型定义(DTD)中创建，让我们从一个例子开始:

```xml
<?xml version="1.0" standalone="yes" ?>
<!DOCTYPE author [
  <!ELEMENT author (#PCDATA)>
  <!ENTITY js "Jo Smith">
]>
<author>&js;</author>
```

所以无论你在哪里使用实体&js;解析器将用实体中定义的值替换它。

### 什么是XXE注入?

XML外部实体攻击是针对解析XML输入的应用程序的一种攻击。当包含对外部实体的引用的XML输入被弱配置的XML解析器处理时，就会发生这种攻击。这种攻击可能导致机密数据泄露、拒绝服务、服务器端请求伪造、从解析器所在机器的角度进行端口扫描，以及其他系统影响。

攻击可以包括使用系统标识符中的file:  scheme或相对路径公开本地文件，这些文件可能包含密码或私有用户数据等敏感数据。由于攻击是相对于处理XML文档的应用程序发生的，所以攻击者可以使用这个受信任的应用程序转向其他内部系统，可能通过http(s)请求披露其他内部内容，或者对任何未受保护的内部服务发起CSRF攻击。在某些情况下，可以通过解除对恶意URI的引用来利用容易出现客户端内存损坏问题的XML处理器库，这可能允许在应用程序帐户下执行任意代码。其他攻击可以访问可能不会停止返回数据的本地资源，如果没有释放太多的线程或进程，可能会影响应用程序的可用性。



一般来说，我们可以区分以下类型的XXE攻击:

- Classic:在这种情况下，外部实体包含在局部DTD中

- Blind:响应中不显示输出和错误

- Error :尝试在错误消息中获取资源的内

### 现代其他框架

在现代REST框架中，服务器可能能够接受您作为开发人员没有考虑到的数据格式。因此，这可能导致JSON端点容易受到XXE攻击。



# XXE DOS 攻击

什么是DOS攻击



 使用相同的XXE攻击，我们可以对服务器执行DOS服务攻击。这种攻击的一个例子是: 

```xml-dtd
<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
 <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
 <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
 <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
 <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
 <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>
```

当XML解析器加载这个文档时，它会看到它包含一个根元素“lolz”，其中包含文本“&lol9;”。然而，“&lol9”是一个被定义的实体，它扩展成一个包含10个“&lol8”字符串的字符串。每个“&lol8”字符串都是一个已定义的实体，它扩展为10个“&lol7”字符串，依此类推。在处理完所有的实体扩展之后，这一小块(< 1 KB) XML实际上将占用近3 gb的内存。

这被称为“十亿笑”，更多信息可以在这里找到:https://en.wikipedia.org/wiki/billion_laughing

# 解题

* lesson3

 在提交表单时，您将在照片中添加一条注释，并尝试执行带有注释字段的XXE注入。试着列出文件系统的根目录。 

![](img/XEE1.png)

* lesson4

  修改content-Type类型json修改为xml

  ![](img/XEE3.png)

  ![](img/XEE2.png)