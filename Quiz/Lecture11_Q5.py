def Hopfield_energy(a, b, c, d, e):
    """Calculates the global energy for the Hopfield network
    given in Question 5."""

    W_ac = 1
    W_bc = 1
    W_ce = 2
    W_cd = 2
    W_be = -3
    W_ad = -2
    W_de = 3

    E = -(W_ac * a * c
          + W_bc * b * c
          + W_ce * c * e
          + W_cd * c * d
          + W_be * b * e
          + W_ad * a * d
          + W_de * d * e)

    return E


if __name__ == '__main__':
    pos_E_states = {}
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        pos_E_states[str(a) + str(b) + str(c) + str(d) +
                                     str(e)] = Hopfield_energy(a, b, c, d, e)

    sort_low_E_states = sorted(pos_E_states, key=pos_E_states.get)
    print("The lowest and second lowest energy configurations for the "
          "Hopfield network given in Question 5 are: {0} and {1} with "
          "energies {2} and {3}, respectively.".format(
              sort_low_E_states[0], sort_low_E_states[1],
              pos_E_states[sort_low_E_states[0]],
              pos_E_states[sort_low_E_states[1]]))
