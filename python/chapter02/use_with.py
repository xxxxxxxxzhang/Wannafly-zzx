
def open_file():
    """ 使用with语法打开一个文件"""
    # try:
    #     f= open('./static/test.txt','r',encoding='utf-8') # 以只读方式打开
    #     rest =f.read()
    #     print(rest)
    #     f.close()
    # except:
    #     pass
    # finally: # 都会执行
    #     f.close()
    with open_file('./static/text.txt','r',encoding='utf-8') as f:
        rest=f.read()
        print(rest)


if __name__ == '__main__':
    open_file()
