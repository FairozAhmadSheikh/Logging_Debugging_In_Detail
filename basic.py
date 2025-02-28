import logging


# configure the logging and saving them in logs.log
logging.basicConfig(filename="logs.log",level=logging.DEBUG) 
# Other way to set level to DEBUG
logging.basicConfig(filename="logs.log",level=10) 


num1=int(input("enter First Num: "))
num2=int(input("enter Secnd Num: "))

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def per(num1,num2):
    return num1%num2

logging.debug(add(num1,num2))
logging.info(mul(num1,num2))
logging.warning(sub(num1,num2))
logging.error(div(num1,num2))
logging.critical(div(num1,num2))

