# risk-management

# Overview
This project analyzes the volatility in the market over a 20 trading day or 1 month period to examine the standard deviation and then apply it annually. I set an annual volatility size of 15% and divded that by the actual annual volatility to create the appropriate sized position. If the volatility was greater than 15% the position size would shrink correspondantly and if the vlatility was lower than 15% it would rise accordingly. 

# Academic Foundation
This project tests volatility targeting, a strategy implemented by AQR Capital. The strategy is based around sizing your position based on the volatility of the market. If the volatility goes up your position size shrinks and if it goes down your position size increases which helps to maintain a constant risk exposure over time.

# Project Structure
`data_collection.py`
  This file collects the data through yFinance on the S&P 500.
`volatility.py`
  This file calculates the daily return and takes the standard deviation which is then used to calculate the rolling volatility and the   annual volatility to calculate the position size.
`drawdown.py`
  This file calculates the cumulative return and also finds the max drawdown and the date it occurrs
`performance.py`
  This file calculates the annual volatility, the max drawdown, the worst drawdown day, the final cumulative return  and the sharpe       ratio to determine the success of the strategy.

# Results
| Metric | Value |
|--------|-------|
| Annualized Volatility | 0.1783 |
| Sharpe Ratio | 0.6947 |
| Maximum Drawdown | -0.3445 |
| Worst Drawdown Date | 2020-03-23 |
| Final Cumulative Return | 2.9429 |

# How to Run
select the ticker you want to test and place it in the ticker value in the data collection file. Then run the data collection file. Then the volatility file and the drawdown file. FInally run the performance file to see the results.
