from operator import itemgetter
from datetime import datetime
import requests
import json
import re
import unicodedata
import os
import time
# To work with the .env file

html = ""
whole_list = {}
total = {}
main = {}
maker = {}

url="http://127.0.0.1:80/v3/guild/{}"
bot_guild = "bastex"



start = time.time()

response = requests.get(url.format(bot_guild))
json_data = response.json()
json_data["guilds"]["guild"]["in_war"]
guild_name=json_data["guilds"]["guild"]["name"]
server=json_data["guilds"]["guild"]["world"]
members_json=json_data["guilds"]["guild"]


def organize(json_members):
	return "hi"

def writejsonfile(filename,data):
	with open(filename,"w") as whatever:
		json.dump(data,whatever)

writejsonfile("testing.json",json_data)


end = time.time()
total_time = end - start
print("It took {} seconds to make the API call and process".format(total_time))
print('You did it!')

