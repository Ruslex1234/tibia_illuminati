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
import time
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
		
#ROD REMIND TO WRITE ALL THE LEFTOVER INTO FUNCTIONS NEXT TIME YOU CODE PRETTY PRINT EVERYTHING!!!


#results=compare_json("testing.json",json_data)
right=convert_json(json_data)
#print(results)
#right = json_data
left=convert_json(read_json("testing.json"))
write_json("testing2.json",left)
ycm = YouchamaJsonDiffer(left, right, ignore_order_func=make_ignore_order_func(["^data",]))


#ycm = YouchamaJsonDiffer(left, right)
ycm.diff()

dict_diff=ycm.to_dict()

dict_diff.pop("just4vis:pairs",None)
for each in dict_diff["value_changes"]:
	name=each["right_path"].split("->")[0]
	hyper_name=name.replace(" ","+")
	attribute=each["right_path"].split("->")[1]
	msg=""
	icon=""
	if attribute == "status":
		if each["new"] == "online":
			icon=":green_circle:"
		else:
			icon=":red_circle:"
		msg="{} [{}](https://www.tibia.com/community/?name={}) {} is now {}.".format(icon,name,hyper_name,attribute,each["new"])
	elif attribute == "level":
		if int(each["new"]) > int(each["old"]):
			icon=":star2:"
		else:
			icon=":skull:"
		msg="{} [{}](https://www.tibia.com/community/?name={}) {} went from {} to {}.".format(icon,name,hyper_name,attribute,each["old"],each["new"])
	elif attribute == "rank":
		icon=":medal:"
		msg="{} [{}](https://www.tibia.com/community/?name={}) {} went from {} to {}.".format(icon,name,hyper_name,attribute,each["old"],each["new"])
	else:
		msg="{} [{}](https://www.tibia.com/community/?name={}) went from {} to {}.".format(name,hyper_name,attribute,each["old"],each["new"])
	#will need to come up with a difference program that sends the messages to discord on a sleep seconds basis
	send_msg("Bastex Activity", msg, webhook)
	print(msg)
	time.sleep(1)


#write_json("testing.json",json_data)




end = time.time()
total_time = end - start
print("It took {} seconds to make the API call and process".format(total_time))
print('You did it!')

