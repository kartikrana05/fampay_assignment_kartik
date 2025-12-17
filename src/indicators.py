import pandas as pd


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate SMA and EMA indicators based on monthly closing prices.
    
    SMA: Simple Moving Average over N periods
    EMA: Exponential Moving Average, using SMA as the initial seed value
    """
    # Simple Moving Averages
    df["sma_10"] = df["close"].rolling(window=10).mean()
    df["sma_20"] = df["close"].rolling(window=20).mean()
    
    # Exponential Moving Averages
    # adjust=False uses the recursive formula: EMA_t = α * price_t + (1-α) * EMA_{t-1}
    # where α = 2 / (span + 1)
    df["ema_10"] = df["close"].ewm(span=10, adjust=False).mean()
    df["ema_20"] = df["close"].ewm(span=20, adjust=False).mean()
    
    return df