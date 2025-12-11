import pandas as pd

df = pd.read_csv("./CSV/moran/world_moran.csv")


num_cols = df.columns[1:]
df[num_cols] = df[num_cols].applymap(lambda x: f"{x:.3f}" if isinstance(x, (int, float)) else x)

df.to_csv("./CSV/moran/world_moran_3f.csv", index=False)