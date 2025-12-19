import gdxpds
import pandas as pd

# ---------- 第一次运行：读取 GDX ----------
gdx = gdxpds.to_dataframes("./GDX/SSP2_BaU_NoCC_World.gdx")

df = gdx["Yld2_load"].copy()
df.columns = ["category","basin","country" ,"year","Value"]

# 保存为 CSV（这是关键）
df.to_csv("./original/CSV/aglu/yield.csv", index=False)

print("第一次处理完成，已保存csv！以后都不需要再读GDX。")
