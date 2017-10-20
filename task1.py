import re
import os
from collections import Counter
c, directory=Counter(), '/home/inwkstudent/Desktop/final task/programming-task-final-nisarg-goo7/Mydir'
for x in os.listdir(directory):
	""" Using a seperate folder so that can use all the text files in that folder. Making the program scalable   """
long=''
fname=os.path.join(directory,x)
if os.path.isfile(fname):
		with open(fname) as f:
			for line in f:
				line=line.rstrip()
				words=line.split(' ')
				for word in words:
					re.sub(r'!+(?=.*\!)','',word)
					if len(word)>len(long):
						long=word
print (long)
