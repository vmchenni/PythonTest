import numpy as np

arr = np.loadtxt('sample.txt')
print(arr)
np.save('newfile.txt',arr)

# arr=np.genfromtxt()
