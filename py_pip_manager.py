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
	
	count = 0
	for line in outdated_str.split('\n'):
		print(str(count),line)
		count += 1

	outdated_split = outdated_str.split('\n')
	outdated_split = outdated_split[2:] # remove first 2 lines
	outdated_split = outdated_split[:-1] # remove last empty line
	for line in outdated_split:
		print('line : ',line)
		line_split = line.split(' ')
		print('line_split : ',line_split)
		print('package name? :', line_split[0]) # <- is getting the package name like this working?

def update_package(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])

def update_all_packages(package_list):
	for package in package_list:
		print('updating package : '+package)
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