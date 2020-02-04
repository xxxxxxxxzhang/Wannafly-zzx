import requests
from lxml import html


def spider(sn, books=[]):
    """ 爬取京东的数据 """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    url = 'https://search.jd.com/Search?keyword={sn}'.format(sn=sn)
    # 获取HTML文档
    html_doc = requests.get(url, headers=headers).content.decode('utf-8')
    # print(html_doc)
    resp = requests.get(url)
    print('当前编码：', resp.encoding)  # 打印当前编码
    resp.encoding = 'utf-8'
    # 获取xpath对象
    selector = html.fromstring(html_doc)
    print('selector:', selector)
    # 找到列表的集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print('列表集合长度', len(ul_list))
    # 解析对应的内容、标题、价格，链接

    for li in ul_list:
        # 标题
        title = li.xpath('./div[@class="gl-i-wrap"]/div[@class="p-name"]/a/em/text()')[0]
        print(title)
        # 购买链接
        link = li.xpath('./div/div[@class="p-img"]/a/@href')[0]
        print('购买链接：http:', link)
        # 价格
        price = li.xpath('./div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')[0]
        print('价格:', price)  # 把￥符号变成空格
        # 商家
        store = li.xpath('./div/div[@class="p-shopnum"]/a/@title')
        # store = '当当自营' if len(store) == 0 else store[0]  # 如果长度等于0这是当当自营
        # print(store)
        if store == ['自营']:
            pass
        else:
            store = li.xpath('./div/div[@class="p-shopnum"]/a/@title')
        print(store[0])

        books.append({
            'title': title,
            'link': 'https:' + link,
            'price': price,
            'store': store[0]
        })
        print('======================================================================')


if __name__ == '__main__':
    sn = 9787559430540
    spider(sn)
