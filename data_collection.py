import yfinance as yf
import pandas as pd
#The ticker we are calling
ticker = "ES=F"
#importing the data from yfinance
data = yf.download(ticker, start="2015-01-01", end="2025-01-01")
#What specific columns to call
data = data[["Close", "Volume"]]
#Labeling the columns
data.columns = ["Close", "Volume"]
#Print/display the data
print(data)
#save the data
data.to_csv("S&P_500.data.csv")