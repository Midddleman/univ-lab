import pandas as pd

df = pd.read_csv("./CSV/gridset/RIJ_17regions.csv")

# 找出 (I, J) 均重复的行
duplicates = df[df.duplicated(subset=["I", "J"], keep=False)]

duplicates.to_csv("./CSV/RIJ_duplicates.csv", index=False)