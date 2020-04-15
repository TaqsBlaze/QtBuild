"""
THIS SCRIPT IS RESPONSIBLE FOR CHACKIING AND DOWNLOADING
NEW UPDATED FROM THE PROJECT REPO
"""
import urllib
import socket
import os
import sys
import time
from datetime import datetime


class Updater(object)
	def __init__(self):
		self.update_link=open("updatelink","r").readlines()
		self.current_version = open("versioninfo","r").readlines()
		self.new_version = False
		self.update = True


	def check_update(self):
		check_net = socket.socket()
		if(check_net.connect((f"{update_link[1].strip('\n')}",80)) == 0):
			new_update = urllib.requiest.urlopen(f"{self.update_link[0]}").read()
			if(self.current_version[1][8:].strip("\n") < new_update and self.update == True):
				self.new_version = True
				self.download_update(self.update_link[0],new_update)



	def download_update(self,update_url,update_string):
		Update = open("QtBuilder-"+update_string+"zip","wb")
		cache_data = urllib.request.urlopen(update_url).read()
		Update.write(cache_data)
		Update.close()
		self.Log(datetime.utcnow(),update_string)

	def log(self,log_date,log_info):
		Log = open("log.txt","a")
		Log.write(f"Successfully downloaded:\n version:{log_info}\nDate:{log_date}")
		Log.close()

	def install_update(self):
		pass
