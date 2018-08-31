#!/usr/bin/env python
# encoding: utf-8
import requests

"""
拉取首页视频
/aweme/v1/feed/?iid=11111111&idfa=A0AB88AF-1C5D-284A-1111-1ACA5CA7914B&version_code=2.0.0&device_type=iPhone8.1&channel=App%20Stroe&os_version=11.0&screen_width=1111&vid=11111-4225-4E0F-82F0-111111&device_id=1111111&os_api=18&app_name=aweme&build_number=20005&device_platform=iphone&app_version=2.0.0&ac=WIFI&aid=1128&openudid=1111111111&count=6&feed_style=0&filter_warn=0&max_cursor=0&min_cursor=0&pull_type=1&type=0&volume=0.00&mas=1111111&as=111&ts=1111
Host: aweme.snssdk.com
User-Agent: Aweme/2.0.0 (iPhone; iOS 8.3; Scale/2.00)
"""

# 常量
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
    "User-Agent": "Aweme/2.0.0 (iPhone; iOS 8.0; Scale/2.00)"
}

# 获取Token       有效期60分钟
resp = requests.get(API + "/token/douyin").json()
token = resp['token']
print("Token: " + token)

# 获取新的设备信息  有效期60分钟永久
resp = requests.get(API + "/douyin/device/new").json()
device_info = resp['data']
print("设备信息: " + str(device_info))

# 拼装参数
params = {
    "iid":              device_info['iid'],
    "idfa":             device_info['idfa'],
    "vid":              device_info['vid'],
    "device_id":        device_info['device_id'],
    "openudid":         device_info['openudid'],
    "device_type":      device_info['device_type'],
    "os_version":       device_info['os_version'],
    "os_api":           device_info['os_api'],
    "screen_width":     device_info['screen_width'],
    "device_platform":  device_info['device_platform'],
    "version_code": APPINFO['version_code'],
    "channel":      APPINFO['channel'],
    "app_name":     APPINFO['app_name'],
    "build_number": APPINFO['build_number'],
    "app_version":  APPINFO['app_version'],
    "aid":          APPINFO['aid'],
    "ac":           "WIFI",
    "count":        "6",
    "feed_style":   "0",
    "filter_warn":  "0",
    "filter_warn":  "0",
    "max_cursor":   "0",
    "min_cursor":   "0",
    "pull_type":    "1",
    "type":         "0",
    "volume":       "0.00"
}
query = ""
for k, v in params.items():
    query += "%s=%s&" % (k, v)
query = query.strip("&")
print("Sign str: " + query)


# 使用拼装参数签名
resp = requests.post(API + "/sign", json={"token": token, "query": query}).json()
print("签名返回: " + str(resp))
sign = resp['data']
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']

# 拉取首页视频列表
resp = requests.get("https://aweme.snssdk.com/aweme/v1/feed/", params=params, headers=header).json()
print(resp)

