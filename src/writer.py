import os
import pandas as pd


def write_output(df: pd.DataFrame, ticker: str, out_dir: str = "output") -> None:
    os.makedirs(out_dir, exist_ok=True)
    df.reset_index().to_csv(f"{out_dir}/result_{ticker}.csv", index=False)
