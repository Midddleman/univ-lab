import pandas as pd


df = pd.read_csv('./CSV/compare_region_basin/Area_basin.csv')

df['country'] = df['region'].str.split('_').str[0]

df['basin_id'] = df['region'].str.split('_').str[1]

basin_count_summary = df.groupby('country')['basin_id'].nunique().reset_index()

basin_count_summary.rename(
    columns={'basin_id': 'Unique_Basin_Count'},
    inplace=True)

output_filename = './CSV/country_basin_count.csv'
basin_count_summary.to_csv(output_filename, index=False)
