# Stock Data Monthly Aggregation & Technical Indicators

This project processes 2 years of daily stock price data for 10 different tickers and transforms them into monthly summaries with technical indicators. It was built as part of a data engineering assignment focusing on time-series resampling and financial metrics calculation.

## What This Does

The script takes a CSV file containing daily stock prices and does three main things:

1. **Resamples** daily data into monthly periods
2. **Calculates** proper OHLC (Open-High-Low-Close) values for each month
3. **Computes** technical indicators - specifically Simple Moving Averages (SMA) and Exponential Moving Averages (EMA) with 10-day and 20-day windows
4. **Outputs** separate CSV files for each of the 10 stock tickers

## The Tickers

The dataset includes these 10 stocks:
- AAPL (Apple)
- AMD (Advanced Micro Devices)
- AMZN (Amazon)
- AVGO (Broadcom)
- CSCO (Cisco)
- MSFT (Microsoft)
- NFLX (Netflix)
- PEP (PepsiCo)
- TMUS (T-Mobile)
- TSLA (Tesla)

## Project Structure

```
├── main.py              # Entry point - orchestrates the whole pipeline
├── src/
│   ├── loader.py        # Handles data loading and monthly aggregation
│   └── writer.py        # Manages file writing logic
├── data/
│   ├── input/           # Place your input CSV here
│   └── output/          # Generated monthly CSVs go here
└── README.md
```

## How It Works

### Monthly OHLC Logic

Getting the monthly OHLC values right was crucial. Here's how I approached it:

- **Open**: The opening price from the *first trading day* of the month (not an average!)
- **High**: The maximum price reached during the entire month
- **Low**: The minimum price reached during the entire month
- **Close**: The closing price from the *last trading day* of the month

### Technical Indicators

Both SMA and EMA are calculated based on the **monthly closing prices**, not the daily ones. This was an important design decision.

**Simple Moving Average (SMA)**:
```
SMA = Sum of last N closing prices / N
```

For example, SMA-10 takes the average of the last 10 monthly closing prices.

**Exponential Moving Average (EMA)**:
```
Multiplier = 2 / (N + 1)
EMA = (Current Close - Previous EMA) × Multiplier + Previous EMA
```

For the first EMA value, I use the SMA as a starting point since there's no "previous EMA" to reference.

## Installation & Usage

### Prerequisites

You'll need Python 3.7+ and pandas. That's it!

```bash
pip install pandas
```

### Running the Script

1. Download the dataset from the provided GitHub link and place it in the `data/input/` folder
2. Run the main script:

```bash
python main.py
```

3. Check the `data/output/` folder for your results - you should see 10 CSV files named `result_AAPL.csv`, `result_MSFT.csv`, etc.

Each output file will have exactly **24 rows** (one for each month in the 2-year period).

## Key Assumptions & Design Decisions

Here are some practical assumptions I made while building this:

1. **Missing Months**: If a stock somehow doesn't have trading data for a particular month, that month gets skipped rather than filled with dummy values. In the real dataset this shouldn't happen, but the code handles it gracefully.

2. **EMA Initialization**: For the first EMA calculation, I use the SMA value as the "previous EMA" since we don't have historical data before our 2-year window. This is a standard practice in financial analysis.

3. **Month-End Logic**: Pandas' resampling uses the 'MS' (month start) frequency for alignment, but I ensure the Open/Close values correctly represent the first/last trading days.

4. **NaN Handling**: For months where we don't have enough historical data to calculate a moving average (e.g., SMA-20 for the first few months), the value is left as NaN rather than making up a number.

5. **Vectorization**: I stuck to pandas' built-in functions (`.rolling()`, `.expanding()`, etc.) rather than pulling in external technical analysis libraries. This keeps the code simple and the dependencies minimal.

## Output Schema

Each output CSV has these columns:

```
date, open, high, low, close, sma_10, sma_20, ema_10, ema_20
```

- `date`: First day of the month (YYYY-MM-DD format)
- `open`, `high`, `low`, `close`: Monthly OHLC values
- `sma_10`, `sma_20`: Simple moving averages (10 and 20 periods)
- `ema_10`, `ema_20`: Exponential moving averages (10 and 20 periods)

## Code Structure

I kept the code modular as requested:

- **`loader.py`**: Contains all the calculation logic - reading the CSV, resampling to monthly, computing OHLC, and calculating technical indicators
- **`writer.py`**: Handles the file I/O - partitioning by ticker and writing individual CSV files
- **`main.py`**: Ties it all together in a clean pipeline

This separation makes it easy to test individual components and modify the logic without touching the file writing code.

## Testing the Results

You can verify the calculations manually:
1. Pick a stock (say AAPL)
2. Check that each month has exactly one row
3. Verify the High is greater than or equal to Low
4. Confirm SMAs are actually rolling averages of the close prices

## Dataset Source

The dataset comes from: https://github.com/sandeep-tt/tt-intern-dataset

## References

- [Exponential Moving Average - Investopedia](https://www.investopedia.com/terms/e/ema.asp)
- [EMA Calculation Guide - Groww](https://groww.in/p/exponential-moving-average)

---

Built with ☕ and pandas for the Data Engineering Intern Assignment
