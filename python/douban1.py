import requests
from bs4 import BeautifulSoup  # 从bs4引入BeautifulSoup

#请求网页
url = "https://movie.douban.com/cinema/later/chengdu/"  # URL不变
# 新增伪装成浏览器的header
fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
response = requests.get(url, headers=fake_headers)  # 请求参数里面把假的请求header加上
# print(response.text)

# 解析网页
# 初始化BeautifulSoup方法一：利用网页字符串自带的编码信息解析网页
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
# 初始化BeautifulSoup方法二：手动指定解析编码解析网页
# soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')

# print(soup.text)  # 输出BeautifulSoup转换后的内容
all_movies = soup.find('div', id="showing-soon")  # 先找到最大的div
# print(all_movies)  # 输出最大的div的内容
for each_movie in all_movies.find_all('div', class_="item"):  # 从最大的div里面找到影片的div
    # print(each_movie)  # 输出每个影片div的内容
    all_a_tag = each_movie.find_all('a')
    all_li_tag = each_movie.find_all('li')
    all_img_tag = each_movie.find_all('img')
    movie_name = all_a_tag[1].text
    moive_href = all_a_tag[1]['href']
    pic_hef=all_img_tag[0]['src']
    movie_date = all_li_tag[1].text
    movie_type = all_li_tag[1].text
    movie_area = all_li_tag[2].text
    movie_lovers = all_li_tag[3].text

    print('名字：{}，图片链接：{}，日期：{}，类型：{}，地区：{}， 关注者：{}'.format(
        movie_name, pic_hef, movie_date, movie_type, movie_area, movie_lovers))