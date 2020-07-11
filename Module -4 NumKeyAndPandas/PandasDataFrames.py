import pandas
# listx=[10,20,30,40]
# tables=pandas.DataFrame(listx)
# print(tables)
# print(type(tables))
#
# data=[{'a':1,'b':2},{'a':1,'b':2,'c':3}]
# tables=pandas.DataFrame(data)
# print(tables)
#
# data=[{'a':1,'b':2},{'a':1,'b':2,'c':3}]
# tables=pandas.DataFrame(data,index=['First','Second'])
# print(tables)

data1={
        'one':pandas.Series([1,2,3],index=['a','b','c']),
        'two':pandas.Series([1,2,3,4], index=['a','b','c','d',])
      }
tables=pandas.DataFrame(data1)
tables['three']=pandas.Series([10,20,30],index=['a','b','c'])

row=pandas.DataFrame([[11,13],[17,19]],columns=['one','three'])
tables=tables.append(row)
print(tables)

# print(tables)

# # print(tables.loc['c'])
# print(tables.iloc[2])

