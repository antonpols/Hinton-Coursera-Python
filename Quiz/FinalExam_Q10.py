import numpy as np


def logistic(input):
    return 1 / (1 + np.exp(-input))


def visible_state_to_hidden_probabilities(rbm_w, bias_h, visible_state):
    # <rbm_w> is a matrix of size <number of hidden units> by
    # <number of visible units>
    # <bias_h> is a matrix of size <number of hidden units> by <1>
    # <visible_state> is a binary matrix of size <number of visible units> by
    # <number of configurations that we're handling in parallel>.
    # The returned value is a matrix of size <number of hidden units> by
    # <number of configurations that we're handling in parallel>.
    # This takes in the (binary) states of the visible units, and returns the
    # activation probabilities of the hidden units conditional on those states.

    num_configs = visible_state.shape[1]

    return logistic(
        np.tile(bias_h, num_configs) + np.dot(rbm_w, visible_state))


if __name__ == '__main__':
    v_1 = 0
    v_2 = 1
    w_1 = 1
    w_2 = -1.5
    b = -0.5
    rbm_w = np.array([[w_1, w_2]])
    bias_h = np.array([[b]])
    visible_state = np.array([[v_1], [v_2]])
    print("The probability of the asked conditional probablilty "
          "for the Restricted Boltzmann Machine given in Question 10 is: "
          "{0:.5f}".format(visible_state_to_hidden_probabilities(
              rbm_w, bias_h, visible_state).item()))
