import requests
import re
import pymysql
from bs4 import BeautifulSoup as bs

cnt = 901
url = "https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=2019"
html = bs(requests.get(url).content, "html.parser", from_encoding='utf8mb4')
db = pymysql.connect("54.210.217.19", "root", "1234", "Movies", charset='utf8mb4')
cursor = db.cursor()  # 객체 생성

sql = '''
CREATE TABLE Movie2019(
    movie_name VARCHAR(1000) NOT NULL,
    movie_url VARCHAR (150) NOT NULL
    ) DEFAULT CHARSET=utf8mb4;
'''
cursor.execute(sql)
db.commit()

for x in range(1, int(cnt)):
    html = bs(requests.get(url + "&page=" + str(x)).content, "html.parser", from_encoding="utf8mb4")
    for i in range(0, 20):
        title = html.select("#old_content > ul > li >a")[i]
        tt = str(title)  # title을 str로 변환 추출을 위해
        code = re.findall("\d+", tt[37:43])[0]
        endpoint = title.contents[0].find(" (")  # 제목의 끝점
        if endpoint >= 0:
            real_title = title.contents[0][0:endpoint]
        else:
            real_title = title.contents[0]
        sql = '''INSERT INTO Movie2019(movie_name,movie_url) VALUES(%s, %s)'''
        cursor.execute(sql, (real_title, "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code="+code+"&type=after&onlyActualPointYn=Y&onlySpoilerPointYn=N&order=sympathyScore"))
        db.commit()


db.close()
