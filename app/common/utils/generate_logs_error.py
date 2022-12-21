from helper import getFile
from datetime import datetime
class GenerateLogError:
    log_file_name:str = "error_logs.txt"
    log_path_save:str = "logs/"

    def save(self,message:str):
        try:
            with open(getFile(self.log_path_save + self.log_file_name),"a") as file_log:
                file_log.write(f'''\n
Error: {message}
DateTime: {datetime.now().__str__()}
                ''')
        except Exception as error:
            print(error)