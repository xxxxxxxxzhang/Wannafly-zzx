import requests
from lxml import html


def spider():
    """ 爬取京东的数据"""
    url = "https://search.jd.com/Search?keyword=9787559430540"
    # 获取HTML文档
    html_doc = requests.get(url).text()
    resp = requests.get(url)
    print(resp.encoding)  # 打印当前编码
    resp.encoding = 'utf-8'  #
    print(html_doc)
    # 获取xpath对象
    selector = html.fromstring(html_doc)
    # 找到列表的集合
    ul_list = selector.xpath('//ul[@id="gl-warp clearfix"]/li')
    print(len(ul_list))
    # 解析对应的内容、标题、价格，链接

    for li in ul_list:
        # 标题
        title = li.xpath('div[@gl-i-wrap]/div[@p-name]/a/text()')
        print(title)
        # 购买链接
        link = li.xpath('/div[@gl-i-wrap]/div[@p-name]/@href)')
        print(link)
        # 价格
        price = li.xpath('div[@gl-i-wrap]/div[@p-operate]/a[@p-o-btn addcart]/i/text()')
        print(price)  # 把￥符号变成空格
        # 商家
        store=li.xpath('div[@gl-i-wrap]/div[@p-shopnum]/a/text()')
        store= '当当自营' if len(store) ==0 else store[0] # 如果长度等于0这是当当自营
        print(store)
    if __name__=='__main__':
        spider()

