import xarray as xr
import numpy as np


# --- 读入数据 ---

luh3= xr.open_dataset("./NC/luh32005.nc")

# --- 定义一个函数（对 Dataset 生成大类） ---
def generate_classes(ds):
    out = {}

    out["agri"] =  ds["c3ann"] + ds["c3nfx"] + ds["c3per"] + ds["c4ann"] + ds["c4per"]
    
    out["grassland"] = ds["pastr"] + ds["range"]

    out["forest"] = ds["primf"] + ds["secdf"] + ds["pltns"]

    return out

luh3_cls = generate_classes(luh3)

# --- 把所有内容合并到一个 Dataset ---
newnc = xr.Dataset()

for name, data in luh3_cls.items():
    newnc[f"{name}"] = data

# --- 保存 ---
newnc.to_netcdf("./NC/compareluh3.nc")

print("Saved compare.nc successfully!")
