def implementStrategy(x_train,weights):
    predicted_returns = x_ train @ weights
    mean = np.mean(predicted_returns)
    std = np.std(predicted_returns)
    k = 3
    pos = 0
    current_position = 0
    trading_signals,position_size = [],[]
    for returns in predicted_returns:
        trade_amount = min(k * abs(returns), 0.75)
        if returns > mean + std :
            trading_signals.append("BUY")
            target_position = min(current_position + trade_amount, 0.75)
        elif returns < mean - std :
            trading_signals.append("SELL")
            target_position = max(current_position - trade_amount,0)
        else :
            trading_signals.append("HOLD")
            target_position = current_position
        current_position = trade_amount
        position_size.append(target_position)
        
    return trading_signals,position_size

