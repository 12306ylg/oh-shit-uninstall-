#coding=UTF-8
import requests

import json

import os

key = input("俄亥俄州立大学钥匙：")#密钥  获取(有osu账号即可):https://osu.ppy.sh/home/account/edit
user = input("俄亥俄州立大学播放器名称/身份：")

url = "https://osu.ppy.sh/api/get_user?" + "k=" + key +" &u=" + user

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 EdgA/110.0.0.0"}
#UA
response = requests.request("GET", url, headers=headers )

data = json.loads(response.text)

uid = data["user_id"]
name = data["username"]
jd = data["join_date"]
ct = data["country"]
ttscore = data["total_score"]
counprank = data["pp_country_rank"]
prank = data["pp_rank"]
print("播放器身份",id)
print("播放器名称",name)
print("加入约会",jd)
print("乡村",ct)
print("总伤痕",ttscore)
print("pp排名",prank)
print("乡村pp排名",counprank)