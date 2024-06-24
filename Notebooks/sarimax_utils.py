import pandas as pd

def predict(sarimax, n_periods):
    forecast_auto, conf_int_auto = sarimax.predict(n_periods, return_conf_int=True)
    df = pd.DataFrame(
        {
            "min": conf_int_auto.T[0],
            "value": forecast_auto.values,
            "max": conf_int_auto.T[1],
        },
        index=forecast_auto.index
    )
    return df
