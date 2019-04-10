from . import potency

def binary_search(a, n, int_part=False):
    # Busca binaria de 0 ate a/2

    min = 0

    if(int_part):
        max = 999999
        int_part = float(int_part)
    else:
        max = int(a)+1

    # Seta o ponto de corte no meio pra iniciar a busca
    point = int((min + max) / 2)

    while (min+1 < max):
        #print(min, max)

        if(int_part):
            result = potency.potency(int_part + (point / 1000000), n)
        else:
            result = potency.potency(point, n)

        # Se o resultado foi maior do que o numero que vc ta procurando, seta como max
        if result > a:
            max = point
        else:
            min = point

        point = int((min + max) / 2)

    if(int_part):
        return min/1000000
    else:
        return min
