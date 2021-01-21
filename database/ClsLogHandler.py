'''

'''
import os
import time;

class ClsLogHandler(object):
    '''
        로그 저장 클래스 
    '''

    def __init__(self, dbconn):
        '''
        Constructor
        '''
        self.dbconn = dbconn
        return
    
    
    def fErrorLogSaveFile(self,functionName, logText):
        """
            파일에 로그 저장 
        """
        errorlogfilename="Excel_Insert_Err_Log"
        
        thisDirectory = str(os.getcwd())    #Crontab 으로 실행시 /root 경로에 파일이 생성됨 
        print(thisDirectory)
        try:
            f = open(thisDirectory + "/" + errorlogfilename, "a")
            data = time.strftime("%Y-%m-%d %I:%M:%S", time.localtime()) + " - [" + functionName + "] - " + logText + "\n"
            f.write(data)
        except Exception as ex:
            print(ex)
        return
    