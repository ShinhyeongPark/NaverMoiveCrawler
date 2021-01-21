# -*- coding: utf-8 -*-


from ClsLogHandler import ClsLogHandler

class ClsDB(object):
    
    def __init__(self, conn):
        """
            DB작업 객체 생성 
        """
        self.dbconn = conn
        self.cursor = self.dbconn.cursor()
        return


    def fCSVinDB(self, _query):
        """
            csv의 내용을 DB에 저장
        """
        print(_query)
        try:
            cursor = self.dbconn.cursor()
            vResult = cursor.execute(_query)
            print("DB Insert Result:" , vResult)    #결과 출력 
            
        except Exception as ex:
            print("Error: ","fCSVinDB", str(ex))
            ClsLogHandler.fErrorLogSaveFile(self,"fCSVinDB", str(ex))
        
        return
