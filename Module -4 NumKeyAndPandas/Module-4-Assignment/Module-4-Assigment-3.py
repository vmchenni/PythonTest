# 3. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all
# people who don’t have a PhD from SalaryGender CSV file
import pandas
tables=pandas.read_csv("SalaryGender.csv",usecols=['Age','PhD'])
# pridatant(tables)
tables=tables[tables.PhD !=0]
print(tables)