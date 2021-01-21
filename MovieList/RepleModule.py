import requests
import time
import SearchingPage
from bs4 import BeautifulSoup as bs
import pymysql

db = pymysql.connect("54.210.217.19", "root", "1234", "Movies", charset='utf8mb4')
cursor = db.cursor()  # 객체 생성

titleNurl = SearchingPage.InputTitle()  # str형태 타이틀과 url 반환

endpoint = titleNurl.find("https")
title = titleNurl[0:endpoint]
url = titleNurl[endpoint:len(titleNurl)]

html = bs(requests.get(url).content, "html.parser", from_encoding='utf-8')
cnt = html.select("body > div > div > div.score_total > strong > em")[0].contents[0].replace(',', '')

sql = '''
CREATE TABLE MovieReple(
    movie_score INT NOT NULL,
    movie_like INT NOT NULL,
    movie_dislike INT NOT NULL,
    movie_rate INT NOT NULL,
    movie_reple CHAR(10000) NOT NULL
    ) DEFAULT CHARSET=utf8mb4;
'''
cursor.execute(sql)
db.commit()

while True:
    for x in range(1, int(cnt) // 10 + 1):
        html = bs(requests.get(url + "&page=" + str(x)).content, "html.parser", from_encoding="utf-8")
        score = html.select("body > div > div > div.score_result > ul > li > div.star_score > em")
        reple = html.select("body > div > div > div.score_result > ul > li > div.score_reple > p")
        like = html.select("body > div > div> div.score_result > ul > li > div.btn_area")
        for i in range(len(reple)):
            db_score = int(score[i].contents[0])  # 평점
            db_like = int(like[i].contents[1].contents[5].contents[0])  # 좋아요
            db_dislike = int(like[i].contents[3].contents[5].contents[0])  # 싫어요
            if int(like[i].contents[1].contents[5].contents[0]) == 0 or \
                    int(like[i].contents[3].contents[5].contents[0]) == 0:
                db_rate = 1
            else:
                db_rate = int(like[i].contents[1].contents[5].contents[0]) / int(
                    like[i].contents[3].contents[5].contents[0])
            tmp = reple[i].contents[5].contents[0].strip()
            if tmp == "":
                try:
                    tmp = reple[i].contents[5].contents[1].contents[1]['data-src']
                except:
                    continue
            db_reple = tmp
            sql = '''INSERT INTO MovieReple(movie_score, movie_like, movie_dislike, movie_rate, movie_reple) VALUES(%i, %i,%i,%i,%s)'''
            cursor.execute(sql, (db_score, db_like, db_dislike, db_rate, db_reple))
            db.commit()

db.close()
