import pandas as pd

# Read the data
tableMaths=pd.read_csv("MathScoreTerm1.csv",usecols=['Name','Score','Age','Sex','ID'])
tablePhysics=pd.read_csv("PhysicsScoreTerm1.csv",usecols=['Score'])
tableDSScore=pd.read_csv("DSScoreTerm1.csv",usecols=['Score'])

# Fill the missing data with zeros
tableMaths.fillna(0)
tablePhysics.fillna(0)
tableDSScore.fillna(0)

tableMaths=tableMaths.rename({'Score':'Score_maths'},axis=1)
tablePhysics=tablePhysics.rename({'Score':'Score_Physics'},axis=1)
tableDSScore=tableDSScore.rename({'Score':'Score_DSScore'},axis=1)
# print(tableDSScore)

combined=tableMaths.join(tablePhysics).join(tableDSScore)
combined['Sex'].replace({'M':'1','F':'2'},inplace=True)
combined = combined[["Name", "Age", "Sex","ID","Score_maths","Score_Physics","Score_DSScore"]]
combined.to_csv("combined.csv")

# Consolidated=pd.merge(tablePhysics,tableMaths)
# print("Consolidated data", Consolidated)