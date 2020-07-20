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
import  numpy as np
#
# df = pd.read_csv("sample-salesv2.csv",skipinitialspace=True,usecols=['name','net_price','date'])
# df.groupby(df['name'])['net_price'].sum().plot.bar()
# plt.xlabel("Name")
# plt.ylabel("Net Price")
# plt.show()
df=pd.read_csv("BigMartSalesData.csv",skipinitialspace=True)
# # print(df)
# # df.groupby(df.Year=='2011')['Amount'].sum().plot.bar()
# dfYear2011=df[df.Year=='2011']
# print(dfYear2011)
data = df.copy()
#Get the sales for perticular year
data=data.drop(data[data.Year!=2011].index)
# print(data)
#Plotting the sales data for year 2011
total=data.groupby('Month').agg({'Amount':np.sum})
print(total)
data.groupby('Month').agg({'Amount':np.sum}).plot(kind='line',color='red')
plt.xlabel('Year of 2011')
plt.ylabel('Total Sales')
plt.title('Sales per month')
plt.show()

#Plot Total Sales Per Month for Year 2011 as Bar Chart
data.groupby('Month').agg({'Amount':np.sum}).plot(kind='bar', color='orange')
plt.xlabel('Year of 2011')
plt.ylabel('Total Sales')
plt.title('Sales Per Month in 2011')
plt.show()


#Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
plt.figure(figsize=(10,10))
sales_country = data.groupby('Country').agg({'Amount':np.sum})
plt.pie(sales_country.values, labels=sales_country.index,autopct='%1.1f%%')
plt.show()