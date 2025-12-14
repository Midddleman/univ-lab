import pandas as pd
import xarray as xr
import numpy as np

# ---------------------------------------------------------
# 手动选择要处理的变量名
# 这些将被扩展为 basin_{name} 与 region_{name}
# ---------------------------------------------------------
name_list = ["forest", "agri", "grassland"]

# 年份列表：2005 + 2010–2100 每 10 年
year_list = list(range(2010, 2101, 10))
year_list.insert(0, 2005)

print("将处理的年份 =", year_list)
print("将处理的变量 =", name_list)

# ---------------------------------------------------------
# Step 1: 读取国家对应表 & 面积数据
# ---------------------------------------------------------
country_map = pd.read_csv("./CSV/grid_country_output.csv")  # country, I, J
area_df     = pd.read_csv("./CSV/GAIJ.csv")                    # I, J, area

grid_info = country_map.merge(area_df, on=["I","J"], how="left")

# ---------------------------------------------------------
# Step 2: 读取 nc 文件
# ---------------------------------------------------------
ds = xr.open_dataset("./NC/compare.nc")

# 标准化 time 变量为年份整数
ds_years = pd.to_datetime(ds["time"].values).year

# ---------------------------------------------------------
# Step 3: 构建国家矩阵 & 面积矩阵
# ---------------------------------------------------------
lat_size = len(ds["lat"])
lon_size = len(ds["lon"])

country_matrix = np.empty((lat_size, lon_size), dtype=object)
area_matrix = np.zeros((lat_size, lon_size)) * np.nan

for _, r in grid_info.iterrows():
    I = int(r["I"])   # lat index
    J = int(r["J"])   # lon index
    country_matrix[I, J] = r["country"]
    area_matrix[I, J]    = r["Value"]

# ---------------------------------------------------------
# Step 4: 汇总国家面积
# ---------------------------------------------------------
results = []

for name in name_list:

    var_basin  = f"basin_{name}"
    var_region = f"region_{name}"

    for varname in [var_basin, var_region]:

        if varname not in ds.variables:
            print(f"变量 {varname} 不存在，跳过。")
            continue

        da = ds[varname]                # shape: (time, lon, lat)
        da_fixed = da.transpose("time", "lat", "lon")   # 关键：变成 time × lat × lon

        for year in year_list:

            if year not in ds_years:
                print(f"年份 {year} 不存在，跳过。")
                continue

            t = np.where(ds_years == year)[0][0]

            frac = da_fixed[t].values          # lat × lon
            real_area = frac * area_matrix     # 面积 × 占比 = 作物面积

            # 对国家聚合
            for country in np.unique(country_matrix):
                if country is None or pd.isna(country):
                    continue

                mask = (country_matrix == country)
                total_area = np.nansum(real_area[mask])

                results.append([varname, country, year, total_area])

# ---------------------------------------------------------
# Step 5: 输出结果 CSV
# ---------------------------------------------------------
out = pd.DataFrame(results, columns=["variable", "country", "year", "area"])
out.to_csv("./CSV/country_area_timeseries.csv", index=False)

print("完成：已生成 country_area_timeseries.csv")
