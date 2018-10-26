import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
f=open("poisson_params.txt",'w')
s = np.random.poisson(5, 36000)
plt.title("Number of requests per unit second")
plt.ylabel("y")
plt.xlabel("x")
count, bins, ignored = plt.hist(s, 14, density=True)

print s
for i in s:
    f.write(str(i)+"\n")
plt.show()
