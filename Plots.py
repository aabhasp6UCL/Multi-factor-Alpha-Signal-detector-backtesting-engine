def plotLoss(iterations,loss):
    plt.title("Loss minimisation")
    plt.plot(iterations,loss)
    plt.xlabel("Iteration")
    plt.ylabel("loss")
    plt.show()

def plotPredictions(x_train,weights,y_train):
    plt.title("Predicted returns vs Actual returns")
    weighted_returns = x_train @ weights
    plt.scatter(weighted_returns,y_train)
    plt.xlabel("weighted returns")
    plt.ylabel("acctual returns")
    plt.show()

def plotEquityCurve(equity_curve):
    plt.plot(equity_curve)
    plt.title("Strategy Equity Curve")
    plt.xlabel("Trading Period")
    plt.ylabel("Cummulative Portfolio Value (£)")
    plt.show()

def plotPNL(r_PnL):
    plt.title("Net profits over time")
    plt.xlabel("Trading Period")
    plt.ylabel("Cummulative net unrealised P&L (£)")
    time = [i for i in range(0, len(unr_PnL))]
    c_r_PnL = np.cumsum(r_PnL)
    plt.plot(time,c_r_PnL)
    plt.show()