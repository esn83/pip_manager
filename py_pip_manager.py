import subprocess
import sys
import os
from datetime import datetime

class py_pip_manager():

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
		
		outdated_split = outdated_str.split('\n')
		
		print('Outdated packages')
		print('--------------------------------')
		for line in outdated_split:
			print(line)
		print('--------------------------------')

		outdated_split = outdated_split[2:] # remove first 2 lines
		outdated_split = outdated_split[:-1] # remove last 1 empty line
		for line in outdated_split:
			package = line.split(' ')[0]
			self.outdated_package_list.append(package)

		print('self.outdated_package_list:')
		for package in self.outdated_package_list:
			print(package)
		print('--------------------------------')

	def update_package(self, package):
		#subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])
		updated = subprocess.check_output([sys.executable, "-m", "pip", "install", package, "--upgrade"], shell=False)	
		
		# write to log
		updated_str = updated.decode('utf-8')
		today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
		self.log = today + '\n\n' + updated_str + '\n\n'
		script_dir = os.path.dirname(__file__) # <-- absolute dir the script is in
		rel_path = "log.txt"
		abs_file_path = os.path.join(script_dir, rel_path)
		with open(abs_file_path, 'a') as log:
			log.write(self.log)

	def update_all_packages(self):
		self.get_outdated() # updates self.outdated_package_list
		for package in self.outdated_package_list:
			print('updating package :',package)
			self.update_package(package)
		print('--------------------------------')

# --------------------------------------

ppm = py_pip_manager() # class instance

#ppm.update_pip()

#ppm.get_installed_packages()

#ppm.get_outdated()

ppm.update_all_packages()

# -- save log --