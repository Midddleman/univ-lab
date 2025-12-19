import pandas as pd

# 读入
df = pd.read_csv("./original/CSV/IAMC/Region_yield.csv")

# 目标年份：2005 + 每 10 年一次，直到 2100
target_years = [2005] + list(range(2010, 2101, 10))
land = ['CEREAL']
# 过滤
df_out = df[df["year"].isin(target_years)]
df_out = df_out[df_out["land"].isin(land)]
# 输出
df_out.to_csv("./original/CSV/IAMC/Region_yield_filtered.csv", index=False)
