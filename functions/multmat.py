"""
Problem: Multiplicação de Matrizes
Author: nilsonsales
"""
def multi_matrix(A,B):
	# NxM, and MxO matrix
	n = len(A)
	m = len(B)
	o = len(B[0])
	#print (n,m,o)

	# initializing matrix
	C = [[0 for i in range(o)] for j in range(n)]

	# multiplying lines times column, i for lines, j for columns
	for i in range(n):
		 for j in range(o):
		     # loads line from A and column from B
		     A_line = A[i]
		     B_column = [row[j] for row in B]

		     for k in range(m):
		         C[i][j] += int(A_line[k]) * int(B_column[k])

	#for i in range(n):
		 #print(*C[i])
	return C


#B = [[1,2,3],[4,1,2],[3,4,1],[2,3,4]]
#A = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#print (multi_matrix(B,A))
