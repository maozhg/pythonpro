# _*_ coding: utf-8 _*_ 
# time: 2020-11-23  16:11
# name: dir
import os
import time

creat_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
picture_dir = os.path.join(base_dir,"picture","creat_time.html")
testcases_dir = os.path.join(base_dir,"Testcases")
common_dir = os.path.join(base_dir,"Common")