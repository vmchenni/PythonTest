# Create csv file from the data below and read in pandas data frame
# Phase 1 -Reading Data
# Phase 2 –Describe the data
# Describe the data on the unit price
# Phase 3 –filter the data
# Create new dataframe having columns 'name','net_price','date' and group all the
# records according to name
# Phase 4 –Plotting graph
# Plot the graph after calculating total sales by each customer. Customer name should be
# on x axis and total sales in y axis.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample-salesv2.csv",skipinitialspace=True,usecols=['name','net_price','date'])
df.groupby(df['name'])['net_price'].sum().plot.bar()
plt.xlabel("Name")
plt.ylabel("Net Price")
plt.show()