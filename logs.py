import threading

class Log:
    def __init__(self, logFile):
        self.__logFile = logFile
        self.__lock = threading.Lock()
    
    def printLog(self, type, msg):
        with self.__lock:
            log = open(self.__logFile, 'a+')

            if type.lower() == "debug":
                log.write("DEBUG: " + str(msg) + "\n")   
            elif type.lower() == "warning":
                log.write("WARNING: " + str(msg) + "\n")
            elif type.lower() == "error":
                log.write("ERROR: " + str(msg) + "\n")
            
            log.close()