"""
THIS SCRIPT IS RESPONSIBLE FOR CHACKIING AND DOWNLOADING
NEW UPDATES FROM THE PROJECT REPO
"""
import urllib
import socket
import os
import sys
import time
from datetime import datetime

""""
FROM THIS POINT ON PLEASE DO NOT TOUCH ANYTHING
IF YOU HAVE NO IDEA WHATS GOING ON HERE
FOR YOUR OWN SAFETY AND THOSE WHO RELAY ON THIS
APPLICATION
"""
class Updater(object):
	def __init__(self):
		self.link_file = open("qtsys/update/updatelink","r").readlines()
		self.update_link=self.link_file
		self.current_version = open("qtsys/update/versioninfo","r").readlines()
		self.new_version = False
		self.update = True
		self.version = '1.0.0'


	def check_update(self):
		check_net = socket.socket()
		update_link = self.update_link[1].strip("\n")
		if(check_net.connect((f"{update_link}",80)) == 0):
			new_update = urllib.requiest.urlopen(f"{self.update_link[0]}").readlines()
			if(self.current_version[1][8:].strip("\n") < new_update[1][8:].strip("\n") and self.update == True):
				self.new_version = True
				self.download_update(self.update_link[0],new_update)



	def download_update(self,update_url,update_string):
		Update = open("QtBuilder-"+update_string+".zip","wb")
		cache_data = urllib.request.urlopen(update_url).read()
		Update.write(cache_data)
		Update.close()
		self.Log(datetime.utcnow(),update_string)

	def log(self,log_date,log_info):
		Log = open("log.txt","a")
		Log.write(f"Successfully downloaded:\n version:{log_info}\nDate:{log_date}\n")
		Log.close()

	def install_update(self):
		pass


Message = f'''
name:QtBuild Updater
version:{Updater().version}
'''
print(Message)
