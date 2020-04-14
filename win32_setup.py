'''
this file is meant to check if you have Qt5 installed
and install it for you if not installed
'''
import os
import time
try:
	import PyQt5
except ImportError:
	print("[+] Qt5 is not isntalled")
	print("[+]install it now? y/n:")
	install = str(input(":"))

	if(install == "y" or install == "yes"):
		os.system("install.bat")
	else:
		if(install == "n" or install == "no"):
			print("[+] Qt Builder will not function")
			print("[+] Exiting...")
			time.sleep(3)
			exit()

