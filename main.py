# _*_ coding: utf-8 _*_ 
# time: 2020-11-23  16:41
# name: main

import unittest
from HTMLTestRunner import  HTMLTestRunner
from Common.dir import *

s = unittest.defaultTestLoader.discover(testcases_dir,pattern="*.py")


# loader = unittest.TestLoader()
# s.addTests(loader.discover(testcases_dir))

fp = open(picture_dir,"w",encoding='UTF-8')
runner = HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = '单元测试报告',
            description ='用例执行情况'

            )
runner.run(s)