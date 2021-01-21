#_*_ coding: utf-8 _*_
import queue
import time
import pymysql;
import ClsDB
import csv
from ClsLogHandler import ClsLogHandler
import openpyxl

q = queue.Queue()


def fConnCreate(_type):
    """
        DB 컨넥션 객체 생성 
    """
    if(str(_type).upper() == "LOCAL"):
        pmyConnection = pymysql.connect(host='localhost',
                              user='cloud',
                              password='Ww62187732!',
                              port=3306,
                              db='cloud',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    else:
        pmyConnection = None
        
    return pmyConnection


def main():
    
    dbconn = fConnCreate("LOCAL") 
    dbcls = ClsDB.ClsDB(dbconn) 
    
    
    # 작업할 파일 목록
    excel_document = openpyxl.load_workbook('sample.xlsx')
    print(type(excel_document)) # 객체 타입 출력
    print("sheet 목록:", excel_document.get_sheet_names()) #Sheet 목록 출력
    try:
        sheet1 = excel_document.get_sheet_by_name("year_2000")
        for _val in sheet1:
            _date=_val[0].value
            _open=_val[1].value
            _high=_val[2].value
            _low=_val[3].value
            _close=_val[4].value
            _adj_close=_val[5].value
            _volume=_val[6].value
            
            if _date == None or str(_date).lower() == "date":       #제목 행은 skip
                continue
            
            print("일자:", _date, ", 시가:", _open, ", 고가:", _high, ", 저가:", _low, ", 종가:", _close, ", Adj_종가:", _adj_close, ", 거래량:", _volume);
            #DB 저장 
            query = "INSERT INTO TBL_STOCK(type_code, basic_date, open_value, high_value, low_value, close_value, adj_close_value, volume_value) VALUES('0000', '%s', %s, %s, %s, %s, %s, %s); commit;" % (_date, _open, _high, _low, _close, _adj_close, _volume)
            dbcls.fCSVinDB(query)
            
    except Exception as ex:
        ClsLogHandler.fErrorLogSaveFile(None,"main()", str(ex)) #시트면이 잘못됐을 경우 오류 발생 
        
    try:
        sheet1 = excel_document.get_sheet_by_name("year_2001")    
        for _val in sheet1:
            _date=_val[0].value
            _open=_val[1].value
            _high=_val[2].value
            _low=_val[3].value
            _close=_val[4].value
            _adj_close=_val[5].value
            _volume=_val[6].value
            if _date == None or str(_date).lower() == "date":
                continue
            print("일자:", _date, ", 시가:", _open, ", 고가:", _high, ", 저가:", _low, ", 종가:", _close, ", Adj_종가:", _adj_close, ", 거래량:", _volume);
            query = "INSERT INTO TBL_STOCK(type_code, basic_date, open_value, high_value, low_value, close_value, adj_close_value, volume_value) VALUES('0000', '%s', %s, %s, %s, %s, %s, %s); commit;" % (_date, _open, _high, _low, _close, _adj_close, _volume)
            dbcls.fCSVinDB(query)
            
    except Exception as ex:
        ClsLogHandler.fErrorLogSaveFile(None,"main()", str(ex))
                
    return


if __name__ == '__main__':
    main()
