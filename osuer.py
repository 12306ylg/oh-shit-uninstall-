#coding=UTF-8
import requests

import json

import os

key = input("俄亥俄州立大学匙：")

user = input("俄亥俄州立大学名称/身份：")

url = "https://osu.ppy.sh/api/get_user?" + "k=" + key +" &u=" + user

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 EdgA/110.0.0.0"}

response = requests.request("GET", url, headers=headers )

print("response")

exit()

url = "https://devapi.qweather.com/v7/weather/now"

querystring = {"location":city_id,"key":key}

"""response = requests.request("GET", url, headers=headers, params=querystring)

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

code = data["code"]

update_time = data["updateTime"]

fx_link = data["fxLink"]

now_data = data["now"]

obs_time = now_data["obsTime"]

temp = now_data["temp"]

feels_like = now_data["feelsLike"]

icon = now_data["icon"]

text = now_data["text"]

wind360 = now_data["wind360"]

wind_dir = now_data["windDir"]

wind_scale = now_data["windScale"]

wind_speed = now_data["windSpeed"]

humidity = now_data["humidity"]

precip = now_data["precip"]

pressure = now_data["pressure"]

vis = now_data["vis"]

cloud = now_data["cloud"]

dew = now_data["dew"]

print("网页视图链接",fx_link)

print("天气更新时间",obs_time)

print("当前温度为",temp,"℃")

print("体感温度",feels_like,"℃")

print("天气状况",text)

print("风向360角度",wind360,"°")

print("风向",wind_dir)

print("风力等级",wind_scale)

print("风速",wind_speed,"公里/小时")

print("相对湿度",humidity,"％")

print("当前小时累计降水量",precip,"毫米")

print("大气压强",pressure,"百帕")

print("能见度",vis,"公里")

print("云量",cloud,"％")

print("露点湿度",dew)"""
