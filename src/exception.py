import sys

# function that get error details from sys
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()                      # returns info of exception
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{0}] line number[{1}] error message [{2}]".format(
        file_name,                                            # error filename
        exc_tb.tb_lineno,                                     # line of error
        str(error)                                            # error
    )
    return error_message

class CustomException(Exception):                                
    '''Inherited class that has constructor getting error_message and 
    __str__ help in returning error_message when object is called as string
    '''
    def __init__(self, error_message, error_detail:sys):      
        super().__init__(error_message)                      # get from Exception class i.e error_message
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message                             # when class is called as string it returns