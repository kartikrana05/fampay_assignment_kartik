from src.loader import load_data
from src.monthly import calculate_monthly_ohlc
from src.indicators import add_indicators
from src.writer import write_output


def main():
    df = load_data("data/output_file.csv")

    for ticker, tdf in df.groupby("ticker"):
        monthly = calculate_monthly_ohlc(tdf)
        monthly = add_indicators(monthly)

        # Safety check
        assert len(monthly) == 24, f"{ticker} does not have 24 months"

        write_output(monthly, ticker)

    print("✅ All stock-wise files generated successfully.")


if __name__ == "__main__":
    main()
