import xarray as xr
import numpy as np

# 打开文件
ncbasin = xr.open_dataset("../basin master/lumip_SSP2_BaU_NoCC.nc")
ncregion = xr.open_dataset("../region master/lumip_SSP2_BaU_NoCC.nc")

years = range(2010, 2110, 10)

for var in ncbasin.data_vars:
    difflist = []

    for i in years:
        # 读取单一年份值
        basin = ncbasin[var].sel(time=f"{i}-01-01")
        region = ncregion[var].sel(time=f"{i}-01-01")

        # 使用 float64 避免 overflow
        sum1 = float(basin.astype("float64").sum())
        sum2 = float(region.astype("float64").sum())

        diff = sum1 - sum2
        difflist.append(diff)

    # 安全平均
    avg = np.nanmean(difflist)

    print(f"From 2010–2100, {var}: averagediff = {avg:.6f}")
