from statsmodels.tsa.arima.model import ARIMA

def arima_model(train_data, order=(5,1,0)):
    model = ARIMA(train_data, order=order)
    model_fit = model.fit()
    return model_fit
