# 5. How do you Count The Number Of Times Each Value Appears In An Array Of
# Integers?
# [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
# Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) which means 0 comes 4 times,
# 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so o
from collections import Counter
myArray=[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
print(Counter(myArray))
ConterDetails=Counter(myArray)
print(ConterDetails.values())



