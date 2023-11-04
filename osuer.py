#我要找我爸爸
#coding=UTF-8
import requests
import json
url = 0
key = input("俄亥俄州立大学钥匙：")#密钥  获取(有osu账号即可):https://osu.ppy.sh/home/account/edit
user = input("俄亥俄州立大学播放器名称/身份：")
urls = input("选择api \n osu!stable(stb)  osu!lazer（测试）(lazer)")
if urls == "stb":
    url = "https://osu.ppy.sh/api/get_user?" + "k=" + key +" &u=" + user
elif urls =="lazer":
    url = "https://lazer.ppy.sh/api/get_user?" + "k=" + key +" &u=" + user
else:
    print ("铸币")
    exit (0)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 EdgA/110.0.0.0"}
#UA
response = requests.request("GET", url, headers=headers )
data = json.loads(response.text)
print ("解析成功")
ouid = data[0]["user_id"]
name = data[0]["username"]
jd = data[0]["join_date"]
ct = data[0]["country"]
ttscore = data[0]["total_score"]
counprank = data[0]["pp_country_rank"]
prank = data[0]["pp_rank"]
print("播放器身份",ouid)
print("播放器名称",name)
print("加入约会",jd)
print("乡村",ct)
print("总伤痕",ttscore)
print("pp排名",prank)
print("乡村pp排名",counprank)
