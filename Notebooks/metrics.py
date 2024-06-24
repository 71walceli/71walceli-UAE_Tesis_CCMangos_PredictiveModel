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