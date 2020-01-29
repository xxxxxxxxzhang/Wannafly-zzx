import requests


def get_book():
    """ 获取书本信息 """
    url = 'http://search.dangdang.com/'
    # rest = requests.get(url)
    rest = requests.get(url, params={
        'key': '9787115428028',
        'act': 'input'
    })
    print(rest.text)
    # json的方式获取数据
    rest.json()
    print(rest.status_code) # 打印http状态码就是一个数字


if __name__ == '__main__':
    get_book()
