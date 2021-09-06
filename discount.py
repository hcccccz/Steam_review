import requests
from bs4 import BeautifulSoup
from redis import StrictRedis
import json

api_key = "cde859f3f3547c8bf77941b2cff1e214884d9d4b"

redis = StrictRedis(password="2921038")

keys = [ i.decode("utf-8") for i in redis.keys()]
i = redis.get(keys[0]).decode("utf-8")
print(json.loads(i)['name'])
# i = json.loads(i)

url = "https://isthereanydeal.com/game/tomclancysdivision/history/"
#
with open("plain.json") as file:
    plain = file.read()

dic = json.loads(plain)['data']['steam']
#
# succ = 0
# fai = 0
# for key in keys:
#
#     plain2 = "app/" +key
#     if plain2 in dic:
#         succ += 1
#     else:
#         fai+=1



r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
soup = soup.find("div",{"id":"historyLogContent"})
soup = soup.find_all("div",{"class":"lg2 game","data-shop":"steam"})

print(len(soup))