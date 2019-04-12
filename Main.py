"""
    Projeto e Análise de Algoritmos
        Calculadora
    Membros:
        Jonathas Silva
        Luiz Antônio
        Nilson Sales
"""

from functions import binary_search, matrix_order, mult, multmat, potency, root, addition


def difference(a, b):
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


def print_matrix(matrix):
    lines = len(matrix)

    print(" ")
    for line in range(lines):
        print(matrix[line])
        


def number_operation():
    print("Enter your simple equation (e.g.: 2 ^ 3 )")
    a, operator, b = input().split(" ")

    if operator == '+':
        result = addition.addition(a, b)
    elif operator == '-':
        result = sub(int(a), int(b))
    elif operator == '*':
        result = mult(int(a), int(b))
    elif operator == '/':
        result = div(float(a), float(b))
    elif operator == '^':
        result = potency.potency(int(a), int(b))
    elif operator == 'root':
        result = root.root(float(a), int(b))

    print(result)
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
        if i == n_matrices-1:
            sizes.append(cols)
            

    if n_matrices == 1:
        result = M[0]
    elif n_matrices == 2: 
        result = multmat.multi_matrix(M[0],M[1])
    else: 
        result = matrix_order.mult_mat_cad(M)
        
    print_matrix(result)
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

        print("\nEnter the type of the operation:\n1 - Numeric\n2 - Matrix\n0 - Exit calculator")
        user_option = int(input())

    print("Exiting calculator")


if __name__ == '__main__':
    main()
