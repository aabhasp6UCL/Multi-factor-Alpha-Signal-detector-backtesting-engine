from data import loadData
from features import buildFeatureMatrix
from Gradient_Descent_Algorithm import implementGradDescent
from plots import plotLoss, plotPredictions

data = yf.download("MU",
                 start="2025-06-01",
                 end="2026-06-01")
df = load_data(data)

feature_matrix, acc_returns = buildFeatureMatrix(df)
weights,loss = implementGradDescent(feature_matrix)
print(weights)

plotLoss(iterations,loss)
plotPredictions(feature_matrix,weights,acc_returns)