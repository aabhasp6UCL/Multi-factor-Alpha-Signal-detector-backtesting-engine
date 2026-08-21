import yfinance as yf
from data import loadData
from features import buildFeatureMatrix
from Gradient_Descent_Algorithm import implementGradDescent
from signals import implementStrategy
from backtester import testStrategy
from performanceEvaluation import sharpeRatio, maxDrawdown, winRate
from Plots import plotLoss, plotPredictions, plotEquityCurve, plotPNL

# LOAD HISTORICAL DATA

data = yf.download(
    "MU",
    start="2025-06-01",
    end="2026-06-01"
)
df = loadData(data)

# BUILD FEATURES AND TRAIN/TEST SPLIT

x_train, x_test, y_train, y_test = buildFeatureMatrix(df)

# TRAIN LINEAR REGRESSION

weights, loss = implementGradDescent(x_train,y_train)
print("\nModel weights:")
print(weights)

# TRAINING LOSS

iterations = range(len(loss))
plotLoss(iterations,loss)

# PREDICTIONS ON TEST DATA

plotPredictions(x_test,weights,y_test)

# GENERATE TRADING SIGNALS

trading_signals, position_size = implementStrategy(x_test,weights)

# BACKTEST THE STRATEGY

(unrealised_pnl,realised_pnl,equity_curve,daily_returns,win_loss) = testStrategy(
    y_test,
    position_size
)

# PERFORMANCE EVALUATION

sharpe = sharpeRatio(daily_returns)
drawdown = maxDrawdown(equity_curve)
win_rate = winRate(win_loss)

# PERFORMANCE METRICS PLOT

plotEquityCurve(equity_curve)
plotPNL(r_PnL)

# PRINT RESULTS

print("BACKTEST RESULTS")

print(f"Initial Portfolio Value: £10,000.00")
print(f"Final Portfolio Value:   £{equity_curve[-1]:,.2f}")
print(f"Total Return:             "f"{((equity_curve[-1] / 10000) - 1) * 100:.2f}%")
print(f"Sharpe Ratio:             {sharpe:.4f}")
print(f"Maximum Drawdown:         {drawdown:.2f}%")
print(f"Trade Win Rate:           {win_rate * 100:.2f}%")
print(f"Number of Trades:         {len(realised_pnl)}")