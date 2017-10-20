import fileinput
with open('running-config.cfg') as f:
	data = f.readlines()
	for line in data:
#		with open('newconfig.txt') as g:
			words = line.split()
			print(line.replace('172','192'))
