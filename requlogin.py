# _*_ coding: utf-8 _*_ 
# time: 2020-12-07  16:40
# name: requlogin

import  unittest

import requests
import json

class HttpRequest:

    def login(self,url,data,method,authorization=None):
        # authorization = res.headers.get('Authorization')

        headers = {'Accept': 'application/json, text/plain, */*',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                   'Authorization':authorization
                   }
        if method.lower()=='get':
            res = requests.get(url,params=data, headers=headers)
        else:
            res=requests.post(url, headers=headers,data=data)

        return  (res)
        # authorization = res.headers.get('Authorization')

        # return (res.headers[Authorization]),(res)
if __name__=='__main__':
    # headers = {'Accept': 'application/json, text/plain, */*',
    #            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    #            'Authorization': authorization
    #            }
    # headers= {'Accept': 'application/json, text/plain, */*',
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    #             'Authorization': 'authorization'
    #             }

    url='http://api.longpean.com/ss/login/login'

    data={'mobile' : '13333333333',
          'password' : '123123'
    }
    res=HttpRequest().login(url,data,'post' )
    print("请求头:",res.headers)
    print("Authorization:",res.headers['Authorization'])
    print("结果：",res.json())

    authorization=res.headers.get('Authorization')
    print(authorization)

    url_1='http://api.longpean.com/smt/smt/publish/getDetails1'
    data_1={"pSkuId":"396324"}
    res_1=HttpRequest().login(url_1,data_1,'get',authorization)
    print("请求头:", res_1.headers)
    print("结果2：", res_1.json())
    # print("123:",Authorization)
# #
    print("code:",res_1.request.headers)
    # print("正文：",res.content)
