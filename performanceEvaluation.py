def sharpeRatio(daily_returns):
    mean = np.mean(daily_returns)
    sd = np.std(daily_returns)
    r_f = 0
    sharpe_daily = (mean - r_f) / sd
    sharpe_annual = sharpe_daily*np.sqrt(252)

    return sharpe_annual

def maxDrawdown(equity_curve):
    max_drawdown = []
    for i in range(len(equity_curve)):
        max_value = equity_curve[i]
        temp = max_value
        for j in range(i,len(equity_curve)):
            if equity_curve[j] < max_value:
                max_value = equity_curve[j] 
            else:
                drawdown = ((temp - max_value)/max_value)*100
                max_drawdown.append(drawdown)

    return np.max(max_drawdown)

    
def winRate(win_loss):
    win = np.sum(win_loss == "WIN")
    win_rate = win/len(win_loss)

    return win_rate