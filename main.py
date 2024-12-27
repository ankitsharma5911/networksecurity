from networksecurity.exception import NetworkSecurityException
from networksecurity.logger import logging
import sys

if __name__=="__main__":
    try:
        logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)