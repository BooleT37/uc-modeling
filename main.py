import pandas as pd
import numpy as np
from fbprophet import Prophet

df = pd.read_csv('data/events.csv', delimiter=";")
df.head()
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
m.plot(forecast)
