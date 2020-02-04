# python学习笔记-爬取数据格式化

### 主要知识点

* with语法

  ![with](img\with.png)

  一下两种语法等价

  

  ```python
      try:
          f= open('./static/test.txt','r',encoding='utf-8') # 以只读方式打开
          rest =f.read()
          print(rest)
          f.close()
      except:
          pass
      finally: # 都会执行
  ```

  ```python
   with open_file('./static/text.txt','r',encoding='utf-8') as f:
          rest=f.read()
          print(rest)
  ```

* Python操作excel

  

* mysql数据库

* Python操作数据库

  

  