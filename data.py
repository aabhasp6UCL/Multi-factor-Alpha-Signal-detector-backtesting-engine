import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

df = yf.download("MU",
                 start="2025-06-01",
                 end="2026-06-01")