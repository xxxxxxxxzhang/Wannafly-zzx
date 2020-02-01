from lxml import html


def parse():
    """ 将html 文件中的内容，使用xpath进行提取"""
    # 读取文件中的内容
    f = open('./static/index.html', 'r', encoding='utf-8')
    s = f.read()
    print(s)
    selector = html.fromstring(s)
    # 解析H3的标题
    h3 = selector.xpath('/html/body/h3/text')
    print(h3)  # 取
    # 到它的list
    print(h3[0])  # 取到它的第1个值
    # 解析ul下面的内容
    ul = selector.xpath('/html/body/ul/li')
    print(len(ul))

    for li in ul:
        # print(li)   #是元素
        print(li.xpath('text()')[0])
        # 解析ul指定的元素值
        ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
        print(ul2)
    # 获取a标签
    a = selector.xpath('//div[@id="container"]/a/text()')
    # 标签内的内容
    alink = selector.xpath('//div[@id="container"]/a/@href')

    print(alink[0])
    # 解析p标签
    # p = selector.xpath('html/body/p/text()') # 获取所有的p标签
    p = selector.xpath('html/body/p[last()]/text()')
    print(len(p))
    print(p[0])

    f.close()
    if __name__ == '__main__':
        print("111111111111111111")
        print("111111111111111111")
        parse()
