import math


def logistic(z):
    return 1 / (1 + math.exp(-z))


def squared_error_cost(y, t):
    return 0.5 * (y - t)**2


if __name__ == '__main__':
    x = 1
    w_1 = 1.0986123
    w_2 = 4
    t = 5
    h = logistic(x * w_1)
    y = h * w_2
    print("The squared error cost incurred by the network given in "
          "Question 11 is: {0:.5f}".format(squared_error_cost(y, t)))
    print("The derivative of the squared error cost with respect to "
          "w_1 for the network given in Question 12 is: {0:.5f}".format(
              (y - t) * w_2 * h * (1 - h) * x))
