import pandas as pd

regions_17 = [
    "USA", "XE25", "XER", "TUR", "XOC",
    "CHN", "IND", "JPN", "XSE", "XSA",
    "CAN", "BRA", "XLM", "CIS", "XME",
    "XNF", "XAF"
]

# 读入 CSV
df = pd.read_csv("./CSV/RIJ.csv")

# 从第一列筛选，只保留 region ∈ 17地域 的行
df_filtered = df[df.iloc[:, 0].isin(regions_17)]

# 保存
df_filtered.to_csv("./CSV/RIJ_17regions.csv", index=False)
