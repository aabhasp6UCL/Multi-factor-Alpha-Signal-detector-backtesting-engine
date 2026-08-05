plt.title("Loss minimisation")
plt.plot(iterations,loss)
plt.xlabel("Iteration")
plt.ylabel("loss")
plt.show()

plt.title("Predicted returns vs Actual returns")
weighted_returns = feature_matrix @ weights
plt.scatter(weighted_returns,acc_returns)
plt.xlabel("weighted returns")
plt.ylabel("acctual returns")
plt.show()