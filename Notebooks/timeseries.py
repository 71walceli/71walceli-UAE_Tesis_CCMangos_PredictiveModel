
import numpy as np

def train_test_split(timeseries, cutoff):
    train = timeseries.loc[:cutoff]
    test = timeseries.loc[cutoff:]
    return train, test

def fit_moving_average(data, period, period_len,):
    # Of the moving avg, the last period_len elements are None, so they're dropped.
    ma = data.resample(period).mean(numeric_only=True).rolling(period_len).mean(numeric_only=True)[period_len:]
    return ma

def time_ranges(timeseries):
    return timeseries.index[0], timeseries.index[-1]
def overlapping_range(timeseries1, timeseries2):
    range1 = time_ranges(timeseries1)
    range2 = time_ranges(timeseries2)
    min_range = range1[0] if range1[0] > range2[0] else range2[0]
    max_range = range1[1] if range1[1] < range2[1] else range2[1]
    return min_range, max_range
def measure_rmse(test,predictions):
    overlap_range = overlapping_range(test, predictions)
    return np.sqrt(mean_squared_error(
        test.loc[
            overlap_range[0].to_pydatetime()
            :
            overlap_range[1].to_pydatetime()
        ], 
        predictions["value"].loc[
            overlap_range[0].to_pydatetime()
            :
            overlap_range[1].to_pydatetime()
        ]
    ))
