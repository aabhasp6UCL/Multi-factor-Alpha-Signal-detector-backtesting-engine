def testStrategy(y_test,position_size):

    portfolio_value,invested,prev_position = 10000,0,0
    unr_net_pnl,r_net_pnl = 0,0
    unr_PnL,r_PnL,equity_curve,daily_returns,win_loss = [],[],[],[],[]

    for returns,position in zip(y_test,position_size):

        prev_pv = portfolio_value

        if position != prev_position:
            target_pos = portfolio_value*position #how much you want to own
            trade_size = target_pos - invested #how much more you should buy/sell to reach the desired position
        else:
            trade_size = 0

        brokerage = 0.003*abs(trade_size)
        slippage = 0.004*abs(trade_size)
        spread = 0.005*abs(trade_size)
        costs = brokerage + slippage + spread
        
        if trade_size < 0: #if you sell - to reduce your current position
            r_net_pnl = (abs(trade_size)/(invested-trade_size))*unr_net_pnl - costs #profit size depedning on full or partial sell
            unr_net_pnl -= (r_net_pnl + costs)
            r_PnL.append(r_net_pnl)
            win_loss.append("WIN" if r_net_pnl > 0 else "LOSS")

        invested += trade_size #how much you have invested so far
        profit = invested*returns #gain from the investment
        prev_position = position
    
        invested += profit    
        portfolio_value += profit 
        portfolio_value -= costs #account for transaction costs
        daily_returns.append(((portfolio_value - prev_pv) / prev_pv)*100)
        prev_pv = portfolio_value

        unr_net_pnl += profit #cummulative net profit
        unr_PnL.append(unr_net_pnl)
        equity_curve.append(portfolio_value)

    return unr_PnL,r_PnL,equity_curve,daily_returns,win_loss


    


