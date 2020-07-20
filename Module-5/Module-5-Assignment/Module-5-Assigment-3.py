#3.  Plot a pie-chart of the number of models released by every manufacturer,
# recorded in the data provide. Also mention the name of the manufacture with
# the largest releases
import pandas as pd
from matplotlib.pyplot import pie, axis, show

df = pd.read_csv("Cars2015.csv",skipinitialspace=True)
sums = df.groupby(df["Make"])["Model"].count()
print("Maximum Number of Cars From",sums.idxmax())
print(sums)
# print(sums.max())
axis('equal')
pie(sums, labels=sums.index,autopct='%.2f')
show()