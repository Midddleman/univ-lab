import pandas as pd

df = pd.read_csv("./CSV/RISOG.csv")

# 要检查的列名
col = "G"

# 找到重复的值（只保留出现次数 > 1 的）
dup_values = df[col][df[col].duplicated()].unique()

# 打印所有重复项所在的行
for v in dup_values:
    print(f"重复值: {v}")
    print(df[df[col] == v])
    print("-" * 40)
