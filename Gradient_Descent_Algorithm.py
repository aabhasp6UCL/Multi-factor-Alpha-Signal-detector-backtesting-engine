def implementGradDescent(x_train,y_train):
    loss = []
    iterations = []
    lr = 0.01
    n = len(x_train)

    weights = np.zeros(3)
    feature_matrix = (
    feature_matrix - np.mean(feature_matrix, axis=0)
    ) / np.std(feature_matrix, axis=0)

    for training in range(1000):

        expected_return = x_train @ weights
        error_vector = expected_return - y_train
        loss.append((1/n)*(error_vector @ error_vector))
        iterations.append(training)

        # loss_function =  (1/n)*sum(i = 1 to n) : (expected_return - returns)^2
        # PartiallossDerivative_wrt_w1 = (2/n)*sum(i = 1 to n) : (expected_return - returns)*x1
        # ... = (2/n)*sum(i = 1 to n) : e*x1 - where e denotes the error_vector
        # (since expected_return is a function of w1,w2 and w3 - so chain rule is used to further differentiate)
        # same for derivative wrt w2,w3
        # however this is summing the product of individual data points and since we have stored the data
        # ...vectors and matrices, the loss derivative will just the dot product of the error vector ahd the first column(x1)
        # ... of the feature matrix containing the first column of features
        # hence computing 3 dot product wrt w1,w2,w3 gives us the 3 entries for the loss vector - which tells us how much to modify all the
        # ... 3 weights by
        # Hence the loss vector turns out to be [(2/n)*e*x1^T, (2/n)*e*x2^T, (2/n)*e*x3^T]^T = (2/n)*e*[x1^T, x2^T, x3^T]
        # ... = [feature_matrix]^T*((2/n)*e)

    transpose = x_train.T
    loss_vector = (2/n)*(transpose @ error_vector)
    weights = weights - lr*loss_vector

    return weights,loss