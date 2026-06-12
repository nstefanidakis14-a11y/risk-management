import pandas as pd
import numpy as np

#import the file
data = pd.read_csv("drawdown_data.csv", index_col=0, parse_dates=True)

#Daily return data
data["Daily_Return"] = pd.to_numeric(data["Close"].pct_change(), errors="coerce")
data = data.dropna()
avg_return = data["Daily_Return"].mean()
std_return = data["Daily_Return"].std()
sharpe_ratio = (avg_return / std_return) * np.sqrt(252)

#The annual volitility percentage change
ann_volatility = data["Daily_Return"].std() * np.sqrt(252)

# the biggest drop for set time frame and the date it occurred
max_drawdown = data["Drawdown"].min()
worst_date = data["Drawdown"].idxmin()

#Final return if using this startegy every day over the time period 
final_return = data["Cumulative_Return"].dropna().values[-1]

print("=========== S&P 500 FUtures Risk Report ===========")
print("Annuallized Volatility", round(ann_volatility, 4))
print("Sharpe Ratio", round(sharpe_ratio, 4))
print("Maximum Drawdown", round(max_drawdown, 4))
print("Worst Drawdown Day", worst_date)
print("Final Cumulative Return", round(float(final_returnw), 4))
