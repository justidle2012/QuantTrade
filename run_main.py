# coding: utf-8
import json
from utils.logger import Logger

class RunMain:
    def __init__(self):
        self.logger = Logger(__name__)

    def run(self):
        count = 5
        print(count)

        for i in range(1, count):
            if 0 == i%2 :
                self.logger.get_log().debug('第'+str(i)+'个接口的返回结果为:%s', i) # 输出接口响应内容
            else :
                self.logger.get_log().debug('第' + str(i) + '接口测试不通过') # 输出接口响应内容

        """写入一个json"""
        

if __name__ == '__main__':
    t = RunMain()
    t.run()


