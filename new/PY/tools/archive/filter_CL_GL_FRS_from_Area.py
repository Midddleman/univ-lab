import pandas as pd
import io

df = pd.read_csv('./CSV/compare_region_basin/Area_basin.csv')


target_years = [2005,2050, 2100]
condition_year = df['year'].isin(target_years)

target_types = ['FRS', 'GL', 'CL']
condition_type = df['type'].isin(target_types)


df_filtered = df[condition_year & condition_type]


output_filename = './CSV/compare_region_basin/CL_GL_FRS_inbasin.csv'
df_filtered.to_csv(output_filename, index=False)

