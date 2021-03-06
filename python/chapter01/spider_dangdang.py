import requests
from lxml import html


def spider(sn, books=[]):
    """ 爬取当当网的数据"""
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)
    # 获取HTML文档
    html_doc = requests.get(url).text
    #  print(html_doc)
    # 获取xpath对象
    selector = html.fromstring(html_doc)
    # 找到列表的集合
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))
    # 解析对应的内容、标题、价格，链接

    for li in ul_list:
        # 标题
        title = li.xpath('a/@title')[0]
        print('标题：', title)
        # 购买链接
        link = li.xpath('a/@href')[0]
        print('购买链接：', link)
        # 价格
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        print('价格：', price[0].replace('¥', ''))  # 把￥符号变成空格
        # 商家
        store = li.xpath('p[@class="search_shangjia"]/a/text()')
        store = '当当自营' if len(store) == 0 else store[0]  # 如果长度等于0这是当当自营
        print('店铺：', store)
        # print('{title}:{price}:{link}:{store}'.format(
        #     title:title,
        #     price=price,
        #     link=link,
        #     store=store
        # ))
        books.append({
            'title': title,
            'link': 'https:' + link,
            'price': price[0].replace('¥', ''),
            'store': store[0]
        })
        print('==========================================================')


if __name__ == '__main__':
    sn = 9787559430540
    spider(sn)
