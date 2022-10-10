from operator import itemgetter
from datetime import datetime
from discord_webhook import DiscordWebhook
import requests
import json
import re
import unicodedata
import os
import time
import jsondiff
from jycm.helper import make_ignore_order_func
from jycm.jycm import YouchamaJsonDiffer
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
guild_name=json_data["guilds"]["guild"]["name"]
server=json_data["guilds"]["guild"]["world"]


#List of functions
def write_json(filename,data):
	with open(filename,"w") as whatever:
		json.dump(data,whatever)

def read_json(filename):
	with open(filename,"r") as whatever:
		return json.load(whatever)

def send_msg(uname,msg,webhook_url):
	webhook = DiscordWebhook(username=uname, url=webhook_url, content=msg)
	response = webhook.execute()

def compare_json(latest_file,current_data):
	right=read_json(latest_file)["guilds"]["guild"]["members"]
	left=current_data["guilds"]["guild"]["members"]
	#result=current_data
	return right

def convert_json(json_data):
	data= {}
	for each in json_data["guilds"]["guild"]["members"]:
		data[each["name"]]=each
	#return json.dumps(data)
	return data
		

#results=compare_json("testing.json",json_data)
right=convert_json(json_data)
#print(results)
#right = json_data
left=convert_json(read_json("testing.json"))
write_json("testing2.json",left)
ycm = YouchamaJsonDiffer(left, right, ignore_order_func=make_ignore_order_func(["^data",]))


#ycm = YouchamaJsonDiffer(left, right)
ycm.diff()

print(ycm.to_dict())


#write_json("testing.json",json_data)




end = time.time()
total_time = end - start
print("It took {} seconds to make the API call and process".format(total_time))
print('You did it!')

