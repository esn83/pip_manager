import subprocess
import sys
import os
from datetime import datetime

class py_pyp_manager():

	def __init__(self):
		self.outdated_package_list = []
		self.log = ''

	def update_pip(self):
		subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'pip'])

	def get_installed_packages(self):
		subprocess.check_call([sys.executable, "-m", "pip", 'freeze'])

	def install(self, package):
	    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

	def get_outdated(self):
		self.outdated_package_list = []

		#subprocess.check_call([sys.executable, "-m", "pip", "list", "--outdated"])
		outdated = subprocess.check_output([sys.executable, "-m", "pip", "list", "--outdated"], shell=False)	
		outdated_str = outdated.decode('utf-8')
		
		count = 0
		for line in outdated_str.split('\n'):
			print(str(count),line)
			count += 1

		outdated_split = outdated_str.split('\n')
		outdated_split = outdated_split[2:] # remove first 2 lines
		outdated_split = outdated_split[:-1] # remove last 1 empty line
		for line in outdated_split:
			print('line :',line)
			line_split = line.split(' ')
			print('line_split :',line_split)
			print('package name? :', line_split[0]) # <- is getting the package name like this working?
			self.outdated_package_list.append(line_split[0])

		for package in self.outdated_package_list:
			print('self.outdated_package_list :', package)

	def update_package(self, package):
		#subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])
		updated = subprocess.check_output([sys.executable, "-m", "pip", "install", package, "--upgrade"], shell=False)	
		
		# write to log
		updated_str = updated.decode('utf-8')
		today = datetime.today().strftime('%Y-%m-%d')
		self.log = today + '\n'
		self.log = updated_str + '\n\n'
		script_dir = os.path.dirname(__file__) # <-- absolute dir the script is in
		rel_path = "log.txt"
		abs_file_path = os.path.join(script_dir, rel_path)
		with open(abs_file_path, 'a') as log:
    		log.write(self.log)

	def update_all_packages(self, package_list):
		for package in package_list:
			print('updating package :',package)
			self.update_package(package)
			print()

# --------------------------------------

ppm = py_pyp_manager() # class instance

#ppm.update_pip()

#ppm.get_installed_packages()

#ppm.get_outdated()

#ppm.update_all_packages(package_list)

# -- save log --