import os
import sys

__version__ = '1.0.0'
__BUILD_ERROR_0__ = """
If you have Qt tools installed make sure you
have included pyuic5 in the environment settings
"""
__BUILD_SUCCESS__ = """
Script was successfully built
"""
Build_Dir = "Script"

def Message(message):
	print(message)
	sys.exit()
	

if(len(sys.argv) < 3):
	src = str(input("Enter UI file:"))
	scp = str(input("Enter script name:"))
else:
	if(len(sys.argv) == 3):
		src = sys.argv[1]
		scp = sys.argv[2]
		

try:
	os.system("mkdir {}".format(Build_Dir))
except:
	pass
	
build = os.system("""pyuic5 -x {} -o {}""".format(src,Build_Dir +"/" + scp))

if(build > 0):
	Message(__BUILD_ERROR_0__)
else:
	if(build < 1):
		Message(__BUILD_SUCCESS__)
