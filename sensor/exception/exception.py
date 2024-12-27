import sys
from sensor.logging import logger

class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error message occured in [{0}] line no[{1}] error message[{2}]".format(
        self.file_name, self.lineno, str(self.error_message))

if __name__=='__main__':
    try:
        logger.logging.info('enter the try block')
        a=1/0
        print('this will not be printed',a)
    except Exception as e:
        raise SensorException(e,sys)