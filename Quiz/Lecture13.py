from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


if __name__ == '__main__':
    w_1 = -6.90675478
    w_2 = 0.40546511

    h_1 = 0
    h_2 = 1
    v = 1

    prob_v_given_h = sigmoid(h_1 * w_1 + h_2 * w_2)
    print('Answer to Question 2: {0:.4f}'.format(prob_v_given_h))

    prob_h_1 = sigmoid(0)
    prob_h_2 = sigmoid(0)

    prob_full_config = (1 - prob_h_1) * prob_h_2 * prob_v_given_h
    print('Answer to Question 3: {0:.4f}'.format(prob_full_config))

    d_log_P_C_011_d_w_1 = h_1 * (v - prob_v_given_h)
    print('Answer to Question 4: {0:.4f}'.format(d_log_P_C_011_d_w_1))

    d_log_P_C_011_d_w_2 = h_2 * (v - prob_v_given_h)
    print('Answer to Question 5: {0:.4f}'.format(d_log_P_C_011_d_w_2))

    w_1 = 10
    w_2 = -4
    prob_v_given_h = sigmoid(h_1 * w_1 + h_2 * w_2)

    prob_v_given_h_1 = 0
    for val_h2, prob_state_h2 in zip([0, 1], [1 - prob_h_2, prob_h_2]):
        prob_v_given_h_1 += prob_state_h2 * sigmoid(h_1 * w_1 + val_h2 * w_2)

    prob_h_2_given_v_h_1 = (prob_v_given_h * prob_h_2) / prob_v_given_h_1
    print('Answer to Question 6: {0:.4f}'.format(prob_h_2_given_v_h_1))

    h_1 = 1
    prob_v_given_h = sigmoid(h_1 * w_1 + h_2 * w_2)

    prob_v_given_h_1 = 0
    for val_h2, prob_state_h2 in zip([0, 1], [1 - prob_h_2, prob_h_2]):
        prob_v_given_h_1 += prob_state_h2 * sigmoid(h_1 * w_1 + val_h2 * w_2)

    prob_h_2_given_v_h_1 = (prob_v_given_h * prob_h_2) / prob_v_given_h_1
    print('Answer to Question 7: {0:.4f}'.format(prob_h_2_given_v_h_1))
