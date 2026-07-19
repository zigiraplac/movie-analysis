from pathlib import Path

import pandas as pd


def save_dataframe(df, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def load_dataframe(path):

    return pd.read_csv(path)
