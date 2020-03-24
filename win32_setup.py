'''
this file is meant to check if you have Qt5 installed
and install it for you
'''
import os
try:
	import PyQt5
except:
	print("[+] Qt5 is not isntalled")
	print("[+]install it now? y/n:")
	isnatall = str(input(":"))

	if(install == "y" or install == "yes"):
		os.system("install.bat")
	else:
		if(install == "n" or isntall == "no"):
			print("[+] Qt Builder will not function")
			exit()

