import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./CSV/moran/world_moran.csv")

variables = ["agri", "forest", "grassland"]

for var in variables:
    plt.figure(figsize=(6,4))
    
    plt.plot(df["year"], df[f"basin_{var}"], marker="o", label=f"basin_{var}")
    plt.plot(df["year"], df[f"region_{var}"], marker="o", label=f"region_{var}")
    
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.ylim(0.5, 1)
    plt.legend(loc = "lower left")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"./plot/moran/{var}_moran.png", dpi=600, bbox_inches="tight")