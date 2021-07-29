import requests
from bs4 import BeautifulSoup

req = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

result = soup.find_all('td', 'title')
# movie_rank = []
for i in range(len(result)):
    print('{:2} 위 : {}'.format(i + 1, result[i].get_text().strip()))
    # movie_rank.append(i.find('a')['title'])
# print(movie_rank)
