#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *

"""
/passport/mobile/send_code/v1/?
iid=37676557806&
idfa=A736DBCE-EC63-4D0B-8747-F55A65241C8D&
version_code=2.0.0&
device_type=iPhone5,3&
channel=pp&
os_version=8.3&
screen_width=640&
vid=FF92F382-4225-4E0F-82F0-9AE01074F1D2&
device_id=54917871480&
os_api=18&
app_name=aweme&
build_number=20005&
device_platform=iphone&
app_version=2.0.0&
ac=WIFI&
aid=1128&
openudid=f7e5628db6d36c0dd3f0197f0ae24944d9aae532&
mix_mode=1&
mobile=2e3d333430343633343d333d3230&
type=3731&
mas=0073ad03d143383960c8383ee41593da62fe5a2fbad26a04ba08de&
as=a14538d81ed89b0eda4463&
ts=1535807118
"""

token = getToken()
device_info = getDevice()

phone = "+86" + "xxxxxxxxxxx"

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
    "mobile":       mixString(phone),
    "mix_mode":     "1",
    "type":         "3731"
}

sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

session = requests.session()
resp = session.get("https://lf.snssdk.com/passport/mobile/send_code/v1/", params=params, headers=header).json()
print resp
if resp['message'] != "success": 
    print "发送验证码失败!!!"
    exit(-1)

code = raw_input("input code: ")

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
    "mobile":   mixString(phone),
    "mix_mode": "1",
    "code": mixString(code)
}

sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

resp = session.get("https://lf.snssdk.com/passport/mobile/sms_login/", params=params, headers=header)
print resp.text



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
}

sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

resp = session.get("https://aweme.snssdk.com/aweme/v1/user/", params=params, headers=header)
print(resp.text)

# 修改密码
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
    "mix_mode": "1",
    "password": mixString("xxxxxxxx"),
}

sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

resp = session.get("https://is.snssdk.com/passport/password/check/", params=params, headers=header)
print(resp.text)