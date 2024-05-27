
def train_test_split(timeseries, cutoff):
    train = timeseries.loc[:cutoff]
    test = timeseries.loc[cutoff:]
    return train, test

def fit_moving_average(data, period, period_len,):
    # Of the moving avg, the last period_len elements are None, so they're dropped.
    ma = data.resample(period).mean(numeric_only=True).rolling(period_len).mean(numeric_only=True)[period_len:]
    return ma

