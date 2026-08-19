def EvaluatePerformance(y_test,position_size):
    portfolio_value,pos_size,invested = 10000,0,0
    gross_pnl = 0
    unr_PnL,equity_curve = [],[]
    for returns,position in zip(y_test,position_size):
        target_pos = portfolio_value*position #how much you want to own
        trade_size = target_pos - invested #how much more you should buy/sell to reach the desired position
        invested += trade_size #how much you have invested so far
        portfolio_value += (invested*(returns) #investment value once stocks increase/decrease
        portfolio_value -= (brokerage + slippage + spread)
        gross_pnl += invested*(returns) #cummulative gross profit
        brokerage = 0.003*abs(trade_size)
        slippage = 0.004*abs(trade_size)
        spread = 0.005*abs(trade_size)
        net_pnl = gross_pnl - brokerage - slippage - spread
        unr_PnL.append(net_pnl)
        equity_curve.append(portfolio_value)

    


