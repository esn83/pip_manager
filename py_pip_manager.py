import subprocess
import sys

def update_pip():
	subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'pip'])

def get_installed_packages():
	subprocess.check_call([sys.executable, "-m", "pip", 'freeze'])

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def get_outdated():
	#subprocess.check_call([sys.executable, "-m", "pip", "list", "--outdated"])
	outdated = subprocess.check_output([sys.executable, "-m", "pip", "list", "--outdated"], shell=False)	
	outdated_str = outdated.decode('utf-8')
	for x in outdated_str.split('\n'):
		print(x)

def update_package(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])

def update_all_packages(package_list):
	for package in package_list:
		print('Updating package : '+package)
		update_package(package)
		print()

package_list = [
				'auto-py-to-exe',
			   ]

# --------------------------------------

#update_pip()

#get_installed_packages()

#get_outdated()

# -- update package_list with outdated packages --

#update_all_packages(package_list)

# -- save log --