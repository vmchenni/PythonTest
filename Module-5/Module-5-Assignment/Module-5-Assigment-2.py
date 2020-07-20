# 2. The dataset given, records data of city temperatures over the years 2014 and
# 2015. Plot the histogram of the temperatures over this period for the cities of
# San Francisco and Moscow
import pandas as pd
import matplotlib.pyplot as plt

import numpy

table = pd.read_csv("CityTemps.csv")
table.head()
# plt.plot(table.Year,table.Hurricanes)
# plt.show()
# print(table.Year)
plt.hist(table.Moscow,bins=100)
plt.hist(table.Melbourne,bins=100)
# plt.xlabel("Year")
# plt.ylabel("Hurricanes")
plt.show()