import logging
import unittest
import datetime
class lgtest(unittest.TestCase):
logging.basicConfig(
    dateTime=datetime.date.today()
    filename='/var/log/Python-%(dateTime)/info.log',
    format='%(asctime)s, datefmt='[%Y-%m-%d %H:%M:%S]',level=logging.INFO')
）
def test(self):
logging.error("这是一条error信息的打印")
logging.info("这是一条info信息的打印")
logging.warning("这是一条warn信息的打印")
logging.debug("这是一条debug信息的打印")
if __name__=='__main__':
unittest.main()


