import pandas as pd
names = ["agri","grassland","forest"] 
modes = ["basin","region"]

variables = [f"{m}_{n}" for n in names for m in modes]
for v in variables:
    df = pd.read_csv(f"./CSV/moran/{v}_moran.csv")


    num_cols = df.columns[1:]
    df[num_cols] = df[num_cols].applymap(lambda x: f"{x:.3f}" if isinstance(x, (int, float)) else x)

    df.to_csv(f"./CSV/moran/{v}_moran.csv_3f.csv", index=False)