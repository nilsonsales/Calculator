def potency(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    elif (exp % 2) == 0:  # Se exp par
        new_exp = (exp/2)
        p = potency(base, new_exp)

        return p*p

    else:  # Se exp impar
        new_exp = ((exp-1) / 2)
        p = potency(base, new_exp)

        return p * p * base
