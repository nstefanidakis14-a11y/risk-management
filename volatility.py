import pandas as pd
#Import the collected data
data = pd.read_csv("S&P_500.data.csv", index_col=0, parse_dates=True)
#error with the labeling of the columns adjust to retrieve values
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")
#Turn that raw data into the Dailyreturn with percent change of the closing value
data["Daily_Return"] = data["Close"].pct_change()
#Create our 20 day rolling volatility 
data["Volatility"] = data["Daily_Return"].rolling(20).std()
#display the data and only first 25 rows
print(data[["Close", "Daily_Return", "Volatility"]].head(25))
#Annualizing the data so that we are comparing everything by year and. not days or moneths to years
data["Ann_Volatility"] = data["Volatility"]*(252**0.5)
data = data.dropna()
print(data[["Close", "Daily_Return", "Volatility", "Ann_Volatility"]])
#Our target annual volatility we are using 
target_vol = 0.15
#dividing against our target volatility to size our position accordingly
data["position_size"] = target_vol / data["Ann_Volatility"]

data.to_csv("volatility_data.csv")
print("Volatility data saved successfully")