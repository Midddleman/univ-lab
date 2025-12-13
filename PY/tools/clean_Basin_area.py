import pandas as pd
import io

df = pd.read_csv('./CSV/gridarea/Basin_area.csv')


# --- 步骤 2: 定义筛选条件 ---
# 筛选条件 1: land 列的值为 'total'
condition_land = (df['land'] == 'total')

# 筛选条件 2: year 列的值为 1961
condition_year = (df['year'] == 1961)


# --- 步骤 3: 联合筛选并创建新的 DataFrame ---
# 使用 & 符号联合两个条件（逻辑 AND）
df_filtered = df[condition_land & condition_year]


# --- 步骤 4: 输出到新的 CSV 文件 ---
output_filename = './CSV/gridarea/Basin_area_filtered.csv'
df_filtered.to_csv(output_filename, index=False)

print(f"筛选完成，结果已保存到文件: {output_filename}")
