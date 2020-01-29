import requests
from lxml import  html

def spider():
    """ 爬取当当网的数据"""
    url = ""
    # 获取HTML文档
    html_doc = requests.get(url).text

    # 获取xpath对象
    selector=html.fromstring(html_doc)
    # 找到列表的集合
    ul_list=selector.xpath()
    print(len(ul_list))
    # 解析对应的内容、标题、价格，链接
    for li in ul_list:
        # 标题
    title= li.xpath('div/')
