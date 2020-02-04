from chapter01.spider_JD import spider as jd
from chapter01.spider_dangdang import spider as dd


def main(sn):
    """ 图书比价工具"""
    book_list = []
    # 当当网的图书数据
    dd(sn, book_list)
    print('当当网数据爬取完成')
    # 打印所有数据列表

    # 京东网数据
    jd(sn, book_list)
    print('京东网数据爬取完成')
    for book in book_list:
        print(book)
    print('-------------------------开始排序-----------------')
    # 排序书的数据
    book_list = sorted(book_list, key=lambda item: float(item["price"]), reverse=True)
    for book in book_list:
        print(book)


if __name__ == '__main__':
    sn = input('请输入ISBN:')
    main(sn)
