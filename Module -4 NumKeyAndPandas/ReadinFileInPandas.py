import pandas
table=pandas.read_csv("mysample.csv")
print(table)

data1={
        'one':pandas.Series([1,2,3],index=['a','b','c']),
        'two':pandas.Series([1,2,3,4], index=['a','b','c','d',])
      }
tables=pandas.DataFrame(data1)
tables['three']=pandas.Series([10,20,30],index=['a','b','c'])

row=pandas.DataFrame([[11,13],[17,19]],columns=['one','three'])
tables=tables.append(row)
tables.to_csv("output.csv")


data={'sample':pandas.Series([1,2,3,4],index=['a','b','c','d'])}
table=pandas.DataFrame(data)
print(table)
table.to_csv("data.csv")