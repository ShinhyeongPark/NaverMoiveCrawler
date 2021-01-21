import openpyxl
import operator
import re


wb=openpyxl.load_workbook('2019년 영화.xlsx')
ws=wb.active

def InputTitle():
    print("         ┌────────────────────────────────────────────────────────────────────────┐")
    print("         │                        영화 평점 감정분석 프로그램                          │")
    print("         └────────────────────────────────────────────────────────────────────────┘")

    title = input("             영화 제목을 입력하시오 : ")

    for i in ws.rows:
        if (operator.eq(i[0].value, title)):
            return str(title+i[1].value)
    print("             일치하는 영화가 없습니다.")

