import threading

class Log:
    def __init__(self, logFile):
        self.__logFile = logFile
        self.__lock = threading.Lock()
        self.__log = open(logFile, 'w')

    def error(self, msg):
        with self.__lock:
            self.__log.write("ERROR: " + str(msg) + "\n")
    
    def warning(self, msg):
        with self.__lock:
            self.__log.write("WARNING: " + str(msg) + "\n")

    def debug(self, msg):
        with self.__lock:
            self.__log.write("DEBUG: " + str(msg) + "\n")
    
    def close(self):
        self.__log.close()