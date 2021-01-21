import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook


class Test:
    def __init__(self, num, name):
        self.num = num
        self.name = name


def insert_test(test_obj):
    conn = pymysql.connect(host='localhost', user='root', password='비밀번호', db='python', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = 'insert into test values(%s, %s)'
            curs.execute(sql, (test_obj.num, test_obj.name))
        conn.commit()
    finally:
        conn.close()


def select_all_to_excel():
    conn = pymysql.connect(host='localhost', user='root', password='cloudcomputing', db='cloud', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = "select * from test"
            curs.execute(sql)
            rs = curs.fetchall()

            wb = Workbook()
            ws = wb.active

            # 첫행 입력
            ws.append(('번호', '이름'))

            # DB 모든 데이터 엑셀로
            for row in rs:
                ws.append(row)

            wb.save('/Users/박신형/Documents/cloudcomputing/숫자.xlsx')
    finally:
        conn.close()
        wb.close()


if __name__ == "__main__":
    # 데이터 1000개정도 넣기
    for i in range(1, 1000):
        test = Test(i, str(i) + '이름')
        insert_test(test)

        select_all_to_excel()
