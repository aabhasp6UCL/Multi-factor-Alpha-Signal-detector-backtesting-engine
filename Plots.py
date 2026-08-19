def plotLoss(iterations,loss):
    plt.title("Loss minimisation")
    plt.plot(iterations,loss)
    plt.xlabel("Iteration")
    plt.ylabel("loss")
    plt.show()

def plotPredictions(feature_matrix,weights,acc_returns):
    plt.title("Predicted returns vs Actual returns")
    weighted_returns = x_train @ weights
    plt.scatter(weighted_returns,y_train)
    plt.xlabel("weighted returns")
    plt.ylabel("acctual returns")
    plt.show()