import pandas as pd

# 输入输出文件名
input_file = "./CSV/region aggregated.csv"
output_file = "./CSV/sorted_region aggregated.csv"

# 读入
df = pd.read_csv(input_file)

# 按 region、year、type（字母顺序）排序
df_sorted = df.sort_values(by=["region", "year", "type"])

# 写出
df_sorted.to_csv(output_file, index=False)

print("排序完成，已输出到：", output_file)
