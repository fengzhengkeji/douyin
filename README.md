# 抖音通信协议签名

## 简介

通过抖音通信协议实现自动化爬取抖音视频，批量注册登录，点赞，评论, 视频下载上传等功能

抖音通信协议采用抖音 iOS 2.0.0版本协议，提供生成iOS设备信息功能，方便调用协议

提供生成签名服务，方便对抖音通信协议进行签名。签名参数: `as`, `mas`, `ts`

项目持续更新中...

## 使用说明

通过调用API加签服务来完成获取新的设备信息及协议签名。

实现过程:
1. 通过访问 `https://api.appsign.vip:2688/token/douyin` 获取抖音加签token，有效期为60分钟
2. 如果没有设备信息可以请求 `https://api.appsign.vip:2688/douyin/device/new` 获取新的设备信息，包括install_id, vid, device_id, openudid 等， 设备信息为永久使用
3. 有了设备信息和加签Token， 需要通过参数构造加签字符串，调用 `https://api.appsign.vip:2688/sign` 完成参数的加签

---

> token有效期为一个小时，支持多线程进行加签，token失效之前无效重复获取
> 设备信息依据需要进行获取

## API参数
1. 获取抖音加签Token
```
https://api.appsign.vip:2688/token/douyin
```
```
{
    "token":"5826aa5b56614ea798ca42d767170e74",
    "success":true
}
```

2. 生成新的设备属性
```
https://api.appsign.vip:2688/douyin/device/new
```
```
{
    "data":{
        "os_api":"23",
        "screen_width":"1334",
        "vid":"39******-ABCD-DA1D-C2C5-******995D7",
        "os_version":"11.0",
        "new_user":1,
        "install_id":4286******3,
        "iid":***********,
        "idfa":"95******-87D6-F152-04F1-88B******418",
        "device_type":"iPhone8.1",
        "device_platform":"iphone",
        "openudid":"b9f9a7c2c9******45c9aafec7b******24cc6",
        "device_id":57000******
    },
    "success":true
}
```

3. 参数加签
```
https://api.appsign.vip:2688/sign
{
    "token":"TOKEN",
    "query":"通过参数生成的加签字符串"
}
```
```
{
    "data":{
        "mas":"0041******cf******511116******1f17624******2e7******8e",
        "as":"a1a506881111aba6******",
        "ts":"153******4"
    },
    "success":true
}
```

## 实例

* [x] 爬取首页视频: `feed.py`
* [x] 视频搜索: `search.py`
* [ ] 注册
* [ ] 登录
* [ ] 点赞
* [ ] 评论
* [ ] 视频下载
* [ ] 视频上传
