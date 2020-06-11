import os
import sys
import requests


def install_python3():
	version = os.popen("python3 --version | grep -o 3[.][0-9]*[.][0-9]*$").read()
	if len(version) == 0 :
		return True
	else:
		v1, v2, v3 = [int(a.strip()) for a in version.split(".")]
		if v2 < 6:
			return True
		elif v3 < 9:
			return True
		else:
			return False

def is_python2_installed():
	if (sys.version_info[0] == 2) or (len(os.popen("ls /usr/bin | grep ^python$").read()) > 1):
		return " 1"
	else:
		return " 0"

def install_from_sh(file_name, par=""):
	os.system("chmod 775 ./" + file_name)	
	os.system("./"+ file_name + par)


def python_test():

	output = os.system("python3.6 -c 'import sys; print(sys.version_info[:])'")
	if output == 0:
		print("Python3.6 is installed.")
	else:
		print("Python3.6 not installed.")
		
def java_test():
	output = os.system("java -version")
	if output == 0:
		print("Java installed!")
	else:
		print("Java did not install correctly")	 

if __name__ == '__main__':

	#python installation
	if install_python3():
		install_from_sh("python.sh" + is_python2_installed())

	#java instalation
	install_from_sh("Java.sh")
	
	#eclipse instalation
	install_from_sh("eclipse.sh")

	python_test()
	java_test()

