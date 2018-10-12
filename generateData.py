from random import seed
from random import random
i = 0
seed(100)
f = open("data.txt", "w")
#min percentage of Cpu util
min = 0
#max percentage of Cpu util
max = 40
while i< 36100 :
	value = random()
	scaled_value = min + (value * (max - min))
	f.write(str(i)+" "+str(scaled_value))
	f.write('\n')
	#setting the min and max percentages at time=3600(after 1hr from beginning)
	if(i >= 3600):
		min = 20
		max = 70
	#setting the min and max percentages at time=7200(after 2hrs from beginning)
	if(i >= 7200):
		min = 60
		max = 80
	#setting the min and max percentages at time=20000(after 5.5hrs from beginning)	
	if(i >= 20000):
	 	min = 40
	 	max = 89	
	#setting the min and max percentages at time=30000(after 8.3hrs from beginning)	 	
	if(i >= 30000):
		min = 70
		max = 89
	#Getting the Value every 10 secs 
	i = i + 100

    	
		