"""
    Projeto e Análise de Algoritmos
        Calculadora
    Membros:
        Jonathas Silva
        Luiz Antônio
        Nilson Sales
"""



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
            result = potency(int_part + (point / 1000000), n)
        else:
            result = potency(point, n)

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


def sum(a, b):
    return a+b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


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


def root(a, n):
    int_part = binary_search(a, n)

    decimal_part = binary_search(a, n, int_part)

    total = str(int_part) + str(decimal_part)[1:]

    return float(total)


def matrix_to_int(matrix, row, col):
    for i in range(row):
        for j in range(col):
            matrix[i][j] = int(matrix[i][j])
    return matrix


def number_operation():
    print("Enter your simple equation (e.g.: 2 ^ 3 )")
    a, operator, b = input().split(" ")

    if operator == '+':
        result = sum(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mult(a, b)
    elif operator == '/':
        result = div(a, b)
    elif operator == '^':
        result = potency(int(a), int(b))
    elif operator == 'root':
        result = root(float(a), int(b))

    print("= ", result)
    return 0


def matrix_operation():
    # Enter the number of matrices followed by number of lines
    print("How many matrices to multiply?")
    n_matrices = int(input())

    # list of matrices
    M = []
    sizes = []

    for i in range(n_matrices):
        # Enter the matrix elements separated by space
        print("Enter the size (lines columns) of the matrix followed by its elements separated by space")
        lines, cols = input().split(" ")

        rows = int(lines)
        cols = int(cols)

        temp = []

        for row in range(rows):
            temp.append(input().split(" "))

        #print(temp)
        temp = matrix_to_int(temp, rows, cols)

        M.append(temp)
        sizes.append(rows)


    # printing the matrices
    for element in M:
        print(element)

    # Now we have two lists:
    # M, where each position correspond to one array
    # sizes, which correspond to the number of lines from each matrix

    return 0


def main():
    # TYPE OF OPERATION
    # 1 - Numeric operation
    # 2 - Matrix multiplication

    print("Enter the type of the operation:\n1 - Numeric\n2 - Matrix\n0 - Exit calculator")

    user_option = int(input())

    while user_option != 0:

        if user_option == 1:
            number_operation()
        elif user_option == 2:
            matrix_operation()
        else:
            print("invalid option")

        print("\n\nEnter the type of the operation:\n1 - Numeric\n2 - Matrix\n0 - Exit calculator")
        user_option = int(input())

    print("Exiting calculator")


if __name__ == '__main__':
    main()
