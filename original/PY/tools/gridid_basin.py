import pandas as pd
import numpy as np

# ---------------------------
# 读取数据
# ---------------------------
A = pd.read_csv("./CSV/GIJ.csv")   # 含 I, J, G
C = pd.read_csv("./CSV/landshareG.csv",
                header=None, names=["grid_id", "basin_raw", "value"])

# 强制 value 为 float
C["value"] = pd.to_numeric(C["value"], errors="coerce")

# ---------------------------
# 仅保留 basin（含 "_" 的记录）
# ---------------------------
C_basin = C[C["basin_raw"].str.contains("_", na=False)].copy()

# 三位小数
C_basin["value"] = C_basin["value"].round(3)

# ---------------------------
# 合并到 GIJ（使每个 IJ 拿到该格子所有 basin）
# ---------------------------
A["G"] = pd.to_numeric(A["G"], errors="coerce").astype("Int64")
C_basin["grid_id"] = C_basin["grid_id"].astype("Int64")

# 多对一 merge → 自动展成一行 IJ 对应多行 basin
result = A.merge(C_basin, left_on="G", right_on="grid_id", how="left")

# ---------------------------
# 输出 I, J, basin, frac
# ---------------------------
out = result[["I", "J", "basin_raw", "value"]]
out.columns = ["I", "J", "basin", "frac"]

out.to_csv("./CSV/grid_basin_output.csv", index=False)

print("完成：已生成 grid_basin_output.csv")
