import pandas as pd

df= pd.read_csv("./CSV/RIJ.csv")

df = df.drop(columns =["Text"])

df.to_csv("./CSV/RIJ.csv",index =False)