from pathlib import Path

import pandas as pd

app_dir = Path(__file__).parent
df_mean = pd.read_csv(app_dir / "df_mean.csv")
line_mean = pd.read_csv(app_dir / "line_mean.csv")
