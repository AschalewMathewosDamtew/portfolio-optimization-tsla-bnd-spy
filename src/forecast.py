import matplotlib.pyplot as plt

def plot_forecast(actual, forecast, conf_int):
    plt.plot(actual, label='Actual')
    plt.plot(forecast, label='Forecast')
    plt.fill_between(range(len(forecast)), conf_int[:, 0], conf_int[:, 1], alpha=0.3)
    plt.legend()
    plt.show()
