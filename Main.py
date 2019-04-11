"""
    Projeto e Análise de Algoritmos
        Calculadora
    Membros:
        Jonathas Silva
        Luiz Antônio
        Nilson Sales
"""

from functions import potency,matrix_order,root



def sum(a, b):
    return a+b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


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
        result = potency.potency(int(a), int(b))
    elif operator == 'root':
        result = root.root(float(a), int(b))

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
        if i == n_matrices:
            sizes.append(cols)


    # printing the matrices
    for element in M:
        print(element)

    print("Sizes:\n", sizes)

    # Now we have two lists:
    # a list 'M' corresponding to the matrices
    # a list 'sizes', corresponding to the number of lines from each matrix
    # + the number of cols of the last matrix

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
