import requests
import re
import pymysql
import operator
from bs4 import BeautifulSoup as bs

db = pymysql.connect("54.210.217.19", "root", "1234", "Movies", charset='utf8mb4')
cursor = db.cursor()  # 객체 생성

title = input("영화 제목을 입력하시오 : ")

sql = '''SELECT movie_url FROM Movie2019 WHERE movie_name=%s'''
if cursor.execute(sql, title):
    result = cursor.fetchall()
    for row in result:
        print(row[0])
else:
    print("검색한 영화가 존재하지 않습니다.")


db.close()
