#!/usr/bin/env python
#-*- coding: utf-8 -*-

#author: huang
#date: 2018-04-20
#comment: zabbix接入微信报警脚本
#python huang 服务故障 无法连接服务器

import requests
import sys
import os
import json
import logging

import edata

corpid=edata.corpid#微信企业ID
appsecret=edata.appsecret#微信应用KEY
agentid=edata.agentid#微信应用ID

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s, %(filename)s, %(levelname)s, %(message)s',
                datefmt = '%a, %d %b %Y %H:%M:%S',
                filename = os.path.join('/tmp/','weixin.log'),
                filemode = 'a')

#获取accesstoken
token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + appsecret
req=requests.get(token_url)
accesstoken=req.json()['access_token']

#发送消息
msgsend_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken

touser=sys.argv[1]
subject=sys.argv[2]
#toparty='3|4|5|6'
message=sys.argv[3]

params={
        "touser": touser,#企业微信号
#       "toparty": toparty,#企业微信部门
        "msgtype": "text",
        "agentid": agentid,
        "text": {
                "content": message
        },
        "safe":0
}

req=requests.post(msgsend_url, data=json.dumps(params))

logging.info('sendto:' + touser + ';;subject:' + subject + ';;message:' + message)
