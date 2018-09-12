#!/usr/bin/env python
# encoding: utf-8
import requests

API = "https://api.appsign.vip:2688"
APPINFO = {
    "version_code": "2.0.0",
    "channel": "App%20Stroe",
    "app_name": "aweme",
    "build_number": "20005",
    "app_version": "2.0.0",
    "aid": "1128",
}
header = {
    "User-Agent": "Aweme/2.0.0 (iPhone; iOS 11.0; Scale/2.00)"
}

# 获取Token       有效期60分钟
def getToken():
    resp = requests.get(API + "/token/douyin").json()
    token = resp['token']
    print("Token: " + token)
    return token

# 获取新的设备信息  有效期60分钟永久
def getDevice():
    resp = requests.get(API + "/douyin/device/new").json()
    device_info = resp['data']
    print("设备信息: " + str(device_info))
    return device_info

# 拼装参数
def params2str(params):
    query = ""
    for k, v in params.items():
        query += "%s=%s&" % (k, v)
    query = query.strip("&")
    print("Sign str: " + query)
    return query

# 使用拼装参数签名
def getSign(token, query):
    if isinstance(query, dict):
        query = params2str(query)
    resp = requests.post(API + "/sign", json={"token": token, "query": query}).json()
    print("签名返回: " + str(resp))
    sign = resp['data']
    return sign

# 混淆手机号码和密码
def mixString(pwd):
    password = ""
    for i in range(len(pwd)):
        password += hex(ord(pwd[i]) ^ 5)[-2:]
    return password

