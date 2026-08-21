# Multi-Factor Alpha Signal Detector & Backtesting Engine

A from-scratch quantitative research pipeline that engineers alpha factors from historical price/volume data, trains a linear regression model via gradient descent to predict forward returns, converts predictions into position-sized trading signals, and evaluates the resulting strategy through a custom backtesting engine with realistic transaction costs.

Built to understand — end to end and without relying on existing quant libraries — how a signal goes from raw market data to a position, and how that position's performance should actually be measured.

---

## Overview

This project implements a complete (and still actively evolving) quant research workflow:

1. **Data ingestion** — pull historical OHLCV data for a given ticker.
2. **Feature engineering** — derive momentum, volatility, and relative volume factors from price/volume history.
3. **Model training** — fit a linear regression model to predict next-period returns using gradient descent implemented from first principles (no `sklearn`).
4. **Signal generation** — convert predicted returns into discrete trading signals (`BUY` / `SELL` / `HOLD`) and conviction-scaled position sizes.
5. **Backtesting** — simulate the strategy period-by-period against realized returns, accounting for brokerage, slippage, and spread costs.
6. **Performance evaluation** — compute risk-adjusted return metrics (Sharpe ratio, maximum drawdown, win rate) and visualize results.

The goal is a transparent, hand-built alternative to black-box backtesting libraries — every calculation, from the loss gradient to the transaction cost model, is explicit and inspectable.

---

## Project Structure

```
.
├── data.py                      # Historical price data loading
├── features.py                  # Feature engineering: momentum, volatility, relative volume
├── Gradient_Descent_Algorithm.py # Linear regression trained via gradient descent
├── signals.py                   # Converts predicted returns into trading signals & position sizes
├── backtester.py                # Core backtesting engine with transaction cost modeling
├── performanceEvaluation.py     # Sharpe ratio, max drawdown, win rate calculations
├── Plots.py                     # Visualization of training loss and prediction accuracy
├── main.py                      # Pipeline entry point
└── README.md
```

---

## Methodology

### 1. Feature Engineering (`features.py`)

For each point in the price history, three factors are computed over a rolling window:

| Factor | Description |
|---|---|
| **Momentum** | Percentage price change over a short lookback window, capturing short-term trend. |
| **Volatility** | Standard deviation of daily returns over the lookback window, capturing risk/uncertainty. |
| **Relative Volume** | Current volume relative to its 20-period average, capturing unusual market interest. |

Each row of the resulting feature matrix is paired with the *forward* realized return, which becomes the regression target.

### 2. Model Training (`Gradient_Descent_Algorithm.py`)

A multivariate linear regression model is trained to predict next-period returns from the feature matrix:

- Features are standardized (zero mean, unit variance) before training.
- Weights are learned by minimizing mean squared error via batch gradient descent, with the loss gradient derived and computed manually (documented in-line via the chain rule derivation).
- Training loss is tracked across iterations to verify convergence.

### 3. Signal Generation (`signals.py`)

Predicted returns are converted into trading signals using a z-score threshold:

- If a prediction is more than one standard deviation above the mean predicted return → **BUY**
- If more than one standard deviation below → **SELL**
- Otherwise → **HOLD**

Position size is conviction-scaled: the magnitude of the predicted return determines how large a position to take, capped at 75% of portfolio value to enforce a risk ceiling.

### 4. Backtesting Engine (`backtester.py`)

The backtester simulates the strategy period-by-period rather than assuming frictionless, instantaneous rebalancing:

- **Trades only execute when the target position actually changes** — the strategy isn't forced to pay transaction costs simply because the portfolio's market value moved; it trades when its view changes.
- **Transaction costs** are modeled as the sum of three components, each proportional to trade size: brokerage (0.3%), slippage (0.4%), and spread (0.5%).
- **PnL is tracked as both unrealized (running, mark-to-market) and realized** (booked proportionally when a position is trimmed or closed), giving a trade-level win/loss record in addition to the overall equity curve.

### 5. Performance Evaluation (`performanceEvaluation.py`)

- **Sharpe Ratio** — annualized risk-adjusted return, assuming a zero risk-free rate.
- **Maximum Drawdown** — largest peak-to-trough decline in portfolio value over the backtest period.
- **Win Rate** — proportion of closed/trimmed trades that were profitable.

---

## Tech Stack

- **Python 3**
- [`numpy`](https://numpy.org/) — vectorized numerical computation
- [`pandas`](https://pandas.pydata.org/) — data handling
- [`matplotlib`](https://matplotlib.org/) — visualization
- [`yfinance`](https://pypi.org/project/yfinance/) — historical market data

---

## Installation

```bash
git clone https://github.com/aabhasp6UCL/Multi-factor-Alpha-Signal-detector-backtesting-engine.git
cd Multi-factor-Alpha-Signal-detector-backtesting-engine
pip install numpy pandas matplotlib yfinance
```

## Usage

```bash
python main.py
```

By default, the pipeline pulls historical data for a single ticker, builds the feature matrix, trains the regression model, and generates loss/prediction diagnostic plots. Signal generation and backtesting are implemented as standalone modules (`signals.py`, `backtester.py`) and can be run independently while the end-to-end pipeline wiring in `main.py` is finalized (see Roadmap below).

---

## Roadmap

This project is under active development. Planned next steps:

- [ ] Finish wiring the full pipeline end-to-end in `main.py` (features → signals → backtest → evaluation, in one run)
- [ ] Add a drift-tolerance band to the backtester so positions rebalance on significant market-driven drift, not only on signal changes
- [ ] Extend signal generation and the backtester to support short positions
- [ ] Expand from a single-asset regression to a true multi-factor, multi-asset framework
- [ ] Add a `requirements.txt` and basic unit tests around the backtesting engine
- [ ] Walk-forward / out-of-sample validation instead of a single train/test split

---

## Disclaimer

This project is for educational and research purposes only. It does not constitute financial advice, and nothing here should be used to make real trading or investment decisions. Backtested performance does not guarantee future results.

---

## License

Distributed under the MIT License. See `LICENSE` for details.

## Author

**Aabhas** — [GitHub](https://github.com/aabhasp6UCL)
