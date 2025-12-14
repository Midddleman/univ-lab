import pandas as pd

df = pd.read_csv("./CSV/gridarea/Basin_area_filtered.csv")

df_1961_total = df[(df['year'] == 1961) & (df['land'] == 'total')].copy()

country_area_summary = df_1961_total.groupby('country')['Value'].sum().reset_index()

country_area_summary.rename(
    columns={'Value': 'Area'},
    inplace=True
)

output_filename = './CSV/Country_area.csv'
country_area_summary.to_csv(output_filename, index=False)
