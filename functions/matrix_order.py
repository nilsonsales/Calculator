import sys

def f(i,j):
    return str(i)+','+str(j)

#a entrada p é caracterizada como o exemplo: matrizes 30x35, 35x15, 15x5 = (30, 35, 15, 5)
def matrix_chain_order(p): 
    n = len(p)-1 																						# numero de matrizes a serem multiplicadas
    m, s = {}, {} 																					# m[i,j] guardará o menor numero de operacoes 
																											# para se multiplicar as matrizes de i a j;
    for i in range(1, n+1):
        m[f(i, i)] = 0 																				# salva em m[i,i] o numero de operacoes com uma 
																											# unica matriz = 0
    for l in range(2, n+1): 																		# inicia com cadeia de duas matrizes: l=2 e vai 
																											# aumentando
        for i in range(1, n-l+2):
            j = i+l-1
            m[f(i, j)] = sys.maxsize 															# m[i,j] = infinito
            for k in range(i, j): 																# obtencao de m[i,j] por meio de solucao de 
																											# recursao: step 2 pag.374 livro Cormen 
                q = m[f(i, k)]+m[f(k+1, j)]+(p[i-1]*p[k]*p[j]) 						# aqui entra programacao dinamica, pois varios 
																											# valores da arvore de recursao ja foram calculados 
																											# e sao trazidos de m
                if q<m[f(i, j)]:
                    m[f(i, j)] = q 																# obtencao de m otimo para multiplicacao da cadeia 
																											# de matrizes de i a j
                    s[f(i, j)] = k 																# onde ocorreu a divisao otima da cadeia de matrizes 
																											# de i a j
    return m, s

def get_optimal_parens(s, i, j): 																#step 4 pag 377 livro Cormen
    res = ''
    if i == j:
        return "A"+str(j)
    else:
        res += "("
        res += get_optimal_parens(s, i, s[f(i, j)])
        res += get_optimal_parens(s, s[f(i, j)]+1, j)
        res +=  ")"
        return res
