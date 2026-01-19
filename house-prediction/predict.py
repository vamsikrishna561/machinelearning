import numpy as np

# Example usage:
if __name__ == "__main__":

    # Dummy model for demonstration purposes
    house_size = np.array([500, 527, 555])
    prices = np.array([100884, 101222, 106790])    
    theta0 = 0.0
    theta1 = 0.0
    change = 1.0
    learning_rate = 1e-7
    y_hat = theta0 + (theta1 * house_size)
    resisuals = y_hat - prices
    tolerance = 1e-3
    while change > tolerance:
        theta0_old = theta0
        theta1_old = theta1
        theta0 -= learning_rate * np.sum(resisuals)
        theta1 -= learning_rate * np.sum(resisuals * house_size)
        y_hat = theta0 + (theta1 * house_size)
        resisuals = y_hat - prices
        change = max(abs(theta0 - theta0_old), abs(theta1 - theta1_old))
    print(theta0, theta1)
    original_size = 583
    print(theta0 + theta1 * original_size)
