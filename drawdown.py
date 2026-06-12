import pandas as pd

data = pd.read_csv("volatility_data.csv", index_col = 0, parse_dates = True)
#daily return again just percent change at close 
data["Daily_Return"] = data["Close"].pct_change()
data = data.dropna()
#total cumulative return if started with $1 and used the strategy daily
data["Cumulative_Return"] = (1 + data["Daily_Return"]).cumprod()

#Finds the rolling max by taking the cumulative ruturn and sumulative max for the selected set of values
data["Rolling_Max"] = data["Cumulative_Return"].cummax()
data["Drawdown"] = (data["Cumulative_Return"] - data["Rolling_Max"]) / data["Rolling_Max"]

#Finds the max drawdown
max_drawdown = data["Drawdown"].min()

print("Maximum Drawdown", round(max_drawdown, 4))

#Worst draw down point and the day it came
worst_date = data["Drawdown"].idxmin()
print("Worst Drawdown Date:", worst_date)
data.to_csv("drawdown_data.csv")
print("Drawdown data saved successfully")