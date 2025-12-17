import pandas as pd


def calculate_monthly_ohlc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resample daily price data to monthly OHLC aggregates.
    
    - Open: First trading day price of the month
    - High: Maximum price during the month
    - Low: Minimum price during the month
    - Close: Last trading day price of the month
    """
    monthly_df = (
        df.set_index("date")
        .resample("ME")
        .agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last"
        })
        .dropna()
    )
    
    return monthly_df
    
