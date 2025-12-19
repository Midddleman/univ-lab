import pandas as pd

# ---------- 1. 读入 ----------
df = pd.read_csv("./original/CSV/IAMC/Region_yield_filtered.csv")

# ---------- 2. 只保留 CEREAL ----------
df_cereal = df[df["land"] == "CEREAL"].copy()

# ---------- 3. pivot：行=basin，列=year ----------
df_wide = df_cereal.pivot(
    index="basin",
    columns="year",
    values="Value"
).reset_index()

# ---------- 4. 加 mode 列，并放在第一列 ----------
df_wide.insert(0, "mode", "region")

# ---------- 5. 输出 ----------
df_wide.to_csv("./original/CSV/IAMC/yield_cereal.csv", index=False)

print("Saved: cereal_region_longtable.csv")
