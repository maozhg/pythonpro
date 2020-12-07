# _*_ coding: utf-8 _*_ 
# time: 2020-11-25  11:03
# name: request
import requests
import json

class HttpRequest:

    def login(self,url,data,method,Authorization=None):
        headers = {'Accept': 'application/json, text/plain, */*',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                   'Authorization':'res.headers["Authorization"]'}
        if method.lower()=='get':
            res = requests.get(url, headers=headers, data=data)
        else:
            res=requests.post(url, headers=headers,data=data)

        return  (res)

        # return ((res.headers[Authorization]),(res))
if __name__=='__main__':
    # headers = {'Accept': 'application/json, text/plain, */*',
    #            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    #            }
    # headers_1= {'Accept': 'application/json, text/plain, */*',
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    #             'Authorization': Authorization
    #             }

    url='http://api.longpean.com/ss/login/login'

    data={'mobile' : '13333333333',
          'password' : '123123'
    }
    res=HttpRequest().login(url,data,'post',Authorization=Authorization)
    print("请求头:",res.headers)
    print("Authorization:",res.headers['Authorization'])
    print("结果：",res.json())

    # Authorization=res.headers["Authorization"]
    url_1='http://api.longpean.com//ebay/syncdata/ebayJson/133896'
    data_1={"itemId":"143741617004"}
    res_1=HttpRequest().login(url_1,data_1,'get',Authorization)
    print("请求头:", res_1.headers)
    print("结果2：", res_1.json())
    # print("123:",Authorization)
# #
    print("code:",res_1.request.headers)
    # print("正文：",res.content)
