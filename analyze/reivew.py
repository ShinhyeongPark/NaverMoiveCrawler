import requests
from bs4 import BeautifulSoup


def get_data(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    score_result = html.find('div', {'class': 'score_result'})
    lis = score_result.findAll('li')
    for li in lis:
        review_text = li.find('p').getText()
        score = li.find('em').getText()
        # 간단하게 프린트만 했습니다.
        print(review_text, score)


test_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=136873&type=after'
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')
score_result = html.find('div', {'class': 'score_result'})
lis = score_result.findAll('li')
review_text = lis[0].find('p').getText()
score = lis[0].find('em').getText()
score = lis[0].find('em').getText()
result = html.find('div', {'class': 'score_total'}).find('strong').findChildren('em')[0].getText()
total_count = int(result.replace(',', ''))

for i in range(1, int(total_count / 10) + 1):
    url = test_url + '&page=' + str(i)
    print('url: "' + url + '" is parsing....')
    get_data(url)
