# 1. You are given a dataset, which is present in the LMS, containing the number of
# hurricanes occurring in the United States along the coast of the Atlantic. Load the
# data from the dataset into your program and plot a Bar Graph of the data, taking
# the Year as the x-axis and the number of hurricanes occurring as the Y-axis.

import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_csv("Hurricanes.csv")
table.head()
# plt.plot(table.Year,table.Hurricanes)
# plt.show()
print(table.Year)
plt.bar(table.Year,table.Hurricanes)
plt.xlabel("Year")
plt.ylabel("Hurricanes")
plt.show()