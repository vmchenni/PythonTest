# 1. Extract data from the given SalaryGender CSV file and store the data from each
# column in a separate NumPy array
# 2. Find:
# 1. The number of men with a PhD
# 2. The number of women with a PhD

import numpy as np
arr=np.genfromtxt("SalaryGender.csv",delimiter=",")
# print(arr)
# print ("Rows",arr.shape[0])
# print("column",arr.shape[1])
iRows=arr.shape[0]
iColumn=arr.shape[1]
iMenWithPHD=0
iWomanWithPHD=0
# Assume that 1 in Geneder column is considred as Men and 0 is woman
for x in range(0,iRows):
    isMale=arr[x,1]
    isPHD=arr[x,3]
    if isMale == 1:
        if isPHD==1:
            iMenWithPHD=iMenWithPHD + 1
    elif isMale==0:
        if isPHD==1:
            iWomanWithPHD=iWomanWithPHD +1
    else:
        pass

print("Men with PHD",iMenWithPHD)
print("Woman with PHD",iWomanWithPHD)