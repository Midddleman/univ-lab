import gdxpds
import pandas as pd

# ---------- 第一次运行：读取 GDX ----------
gdx = gdxpds.to_dataframes("./GDX/base_region.gdx")

df = gdx["YIELDLDM_annual"].copy()
df.columns = ["basin","year" ,"land","Value"]

# 保存为 CSV（这是关键）
df.to_csv("./original/CSV/IAMC/Region_yield.csv", index=False)

print("第一次处理完成，已保存csv！以后都不需要再读GDX。")
