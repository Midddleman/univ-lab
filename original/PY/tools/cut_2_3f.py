import pandas as pd

names = ["Basin_yield","Region_yield"]
# names = ["BIIbasin","BIIregion"]
for name in names:
    df = pd.read_csv(f"./original/CSV/IAMC/{name}.csv")


    num_cols = df.columns[2:]
    df[num_cols] = df[num_cols].applymap(lambda x: f"{x:.3f}" if isinstance(x, (int, float)) else x)

    df.to_csv(f"./original/CSV/IAMC/{name}.csv", index=False)