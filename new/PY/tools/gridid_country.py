import pandas as pd
import numpy as np
from tqdm import tqdm

tqdm.pandas()

# ---------------------------
# 读取文件
# ---------------------------
A = pd.read_csv("./CSV/GIJ.csv")   # 包含 I, J, G
C = pd.read_csv("./CSV/landshareG.csv", header=None, names=["grid_id", "country_raw", "value"])

# value 列强制转成 float（关键修复！！）
C["value"] = pd.to_numeric(C["value"], errors="coerce")

# 去掉国家后缀
C["country"] = C["country_raw"].str.split("_").str[0]

# ---------------------------
# 分组函数
# ---------------------------
def assign_group(df):
    # 防止 df 是 Series
    if isinstance(df, pd.Series):
        df = df.to_frame().T

    running_sum = 0.0
    groups = []
    group_id = 0

    for v in df["value"]:
        # 再保险：强制 v 是 float
        v = float(v)

        running_sum += v
        groups.append(group_id)

        if abs(running_sum - 1) < 1e-3:
            group_id += 1
            running_sum = 0.0

    return pd.Series(groups, index=df.index)

# ---------------------------
# 进度条 groupby
# ---------------------------
print("正在为每个 grid_id 分组（大区 / 国家 / 子区域）...")

C["group"] = (
    C.groupby("grid_id")
     .progress_apply(assign_group)
     .reset_index(level=0, drop=True)
)

# ---------------------------
# 选择 group == 1（国家组）
# ---------------------------
print("正在选择每个 grid_id 的主国家...")

country_group = C[C["group"] == 1]

best_country = (
    country_group.loc[
        country_group.groupby("grid_id")["value"].idxmax(),
        ["grid_id", "country"]
    ]
)

# ---------------------------
# 合并结果
# ---------------------------
print("正在合并结果到 GIJ.csv ...")

A["G"] = pd.to_numeric(A["G"], errors="coerce").astype("Int64")
best_country["grid_id"] = pd.to_numeric(best_country["grid_id"], errors="coerce").astype("Int64")
result = A.merge(best_country, left_on="G", right_on="grid_id", how="left")

result[["country", "I", "J"]].to_csv("./CSV/grid_country_output.csv", index=False)

print("完成：已生成 grid_country_output.csv")
