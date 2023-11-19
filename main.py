import yfinance as yf
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

valmet_he = yf.Ticker("VALMT.HE")
# print(valmet_he.calendar)
# print(valmet_he.institutional_holders)
# print(valmet_he.recommendations)
# get all stock info
# valmet_he.info

# get historical market data
# hist = valmet_he.history(period="1mo")
# save data
stock_symbol = "VALMT.HE"
start_date = "2013-01-01"
end_date = "2023-11-03"
# Fetch the daily historical data
# data = yf.download(stock_symbol, start=start_date, end=end_date)
# data.to_csv('daily_valmetHE_stock_data.csv')
# --------------------------------------------------------------------------------------------------------

# Load your data into a DataFrame
data = pd.read_csv("your_data.csv")

# Data Preprocessing
data["Date"] = pd.to_datetime(data["Date"])
data.set_index("Date", inplace=True)

# Create a target variable by shifting the open and close prices by one day
data["Next_Open"] = data["Open"].shift(-1)
data["Next_Close"] = data["Close"].shift(-1)

# Feature Engineering (if desired)
# You can add additional features here

# Data Splitting
X = data[["Open", "Close"]].iloc[:-1]  # Features
y = data[["Next_Open", "Next_Close"]].iloc[:-1]  # Target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest Model
rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# Prediction
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
