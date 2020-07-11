import  pandas,numpy
series=pandas.Series(int)
print(series)

arr=numpy.array([10,20,30,40,50])
series=pandas.Series(arr)
print(series)

data={"fname":"vish","lname":"chenni"}
series=pandas.Series(data)
print(series)

# Accessing values from pandas
data=[10,20,30,40,50]
series=pandas.Series(data)
print(series[1:4])