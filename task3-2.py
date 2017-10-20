import fileinput
with open('running-config.cfg') as f:
        data = f.readlines()
        for line in data:
                words = line.split()
                for word in words:
                	if word=='interface' or word=='vlan':
                          print (line)
