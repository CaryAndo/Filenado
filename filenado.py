import sys
import os
import re

def sort_dir(dire, skip=''):
	"""
		Given a directory (string), sort all the files
		into folders based on their extension
	"""
	directory = str(dire)
	if os.path.isdir(directory):
		for file in os.listdir(directory):
			if os.path.isdir(file):
				continue
			if file[0] == '.':
				print('Hidden file: ' + file + ' skipping')
				continue
			if file == skip:
				continue
			splitted = re.split(r'\.\s*', file, maxsplit=1)
			if len(splitted) == 1:
				print('No file extension, skipping ' + file)
				continue
			extension = splitted[-1]
			if os.path.isdir(directory + '/' + extension):
				print("apparently " + directory + '/' + extension + ' is a folder!')
				try:
					print("tring to move to " + directory + '/' + extension + '/' + file)
					os.rename(directory + '/' + file, directory + '/' + extension + '/' + file)
					print('moved ' + file + ' to ' + '.' + extension + '/' + file)
				except OSError:
					print('Failed to move file: ' + file + '!')
			else:
				os.mkdir(directory + '/' + extension)
				print("created " + directory + '/' + extension)
				try:
					os.rename(directory + '/' + file, './'+extension+'/'+file)
				except OSError:
					print('Failed to move file: ' + directory + '!')
	elif os.path.isfile(directory):
		print(directory + ' is not a directory!')
	else:
		print(directory + ' does not exist.')

if __name__ == '__main__':
	for arg in sys.argv:
		if arg == sys.argv[0]:
			continue
		sort_dir(arg, sys.argv[0])
