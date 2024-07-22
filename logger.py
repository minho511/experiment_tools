import os

class mylogger:
    def __init__(self, log_path):
        self.log_path = log_path
        self.logtxt = None
        self.make_logfile()

    def make_logfile(self):
        self.logtxt = os.path.join(self.log_path, "log.txt") 
        print(f"make log file >> {self.logtxt}")
        if not os.path.isdir(self.log_path):
            os.makedirs(self.log_path)
        f = open(self.logtxt, 'w')
        f.write("init logger ... \n")
        f.close()
                
    def write_log(self, log):
        print(log)
        f = open(self.logtxt, 'a')
        f.write(log+'\n')
        f.close()