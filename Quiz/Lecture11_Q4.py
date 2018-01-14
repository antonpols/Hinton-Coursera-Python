from math import exp


def Boltzmann_energy(V_1, V_2, h):
    """Calculates the energy of a joint configuration for the Boltzmann
    machine given in Question 4."""

    W_1 = 3
    W_2 = -1
    b_h = -2

    E = -(b_h * h + W_1 * V_1 * h + W_2 * V_2 * h)

    return E


def partition_function():
    """Calculates the partition function for the Boltzmann machine given in
    Question 4."""

    result = 0
    for V_1 in range(2):
        for V_2 in range(2):
            for h in range(2):
                result += exp(-Boltzmann_energy(V_1, V_2, h))

    return result


def prob_joint_config(V_1, V_2, h):
    """Calculates the probability of a joint configuration for the Boltzmann
    machine given in Question 4."""

    return exp(-Boltzmann_energy(V_1, V_2, h)) / partition_function()


def prob_visible_config(V_1, V_2):
    """Calculates the probability of a configuration of the visible units for
    the Boltzmann machine given in Question 4."""

    result = 0
    for h in range(2):
        result += prob_joint_config(V_1, V_2, h)

    return result


if __name__ == '__main__':
    print("The probability of the asked configuration of the visible units "
          "for the Boltzmann machine given in Question 4 is: "
          "{0:.3f}".format(prob_visible_config(1, 0)))
