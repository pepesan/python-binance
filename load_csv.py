import os.path
import pandas as pd


def load_data_binance(symbol, kline_size):
    filename = 'binance-%s-%s-data.csv' % (symbol, kline_size)
    if os.path.isfile(filename):
        data_df = pd.read_csv(filename)
    else:
        data_df = pd.DataFrame()
    return (data_df, filename)


if __name__ == '__main__':
    # Const
    value_pair = "BTCUSDT"
    period = "15m"
    # load data
    print("Loading Data")
    (data, filename) = load_data_binance(value_pair, period)
    print(filename)
    print(data.shape)
    print(data.columns)
    print(data.head(1))

