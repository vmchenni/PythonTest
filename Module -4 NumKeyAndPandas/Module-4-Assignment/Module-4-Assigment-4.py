# 4. Calculate the total number of people who have a PhD degree from SalaryGender
# CSV file.
import pandas
tables=pandas.read_csv("SalaryGender.csv",usecols=['Age','PhD'])
# pridatant(tables)
tables=tables[tables.PhD !=0]
print("People with PHD are", tables.shape[0])