import csv
import math

class grafo:
   def __init__(self, matriz,ids):
    self.matriz = matriz
    self.ids = ids


def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        ids = csv_reader.__next__()
        ids.pop(0)
        for row in csv_reader:
            aux = []
            for a in row[1:]:
                if(a=="i"):
                    aux.append(math.inf)
                else:
                    aux.append(int(a))
            matriz = matriz + [aux]
    return grafo(matriz, ids)

def BFS(matrizresidual, o, d, p):
    v = [False]*(len(matrizresidual))
    queue = []
    queue.append(o)
    v[o] = True
    while queue:
        u = queue.pop(0)
        for i in range(len(matrizresidual[u])):
            if v[i] == False and matrizresidual[u][i] > 0:
                if i == d:
                    v[i] = True
                    p[i] = u
                    return True
                queue.append(i)
                v[i] = True
                p[i] = u
    return False


def fordFulkerson(grafo, s, t):
    matrizresidual = grafo.matriz
    max_flow = 0
    p = [None]*len(grafo.matriz)
    while(BFS(matrizresidual, s, t, p)):
        d = t
        menor = float("inf")
        while(d!=s):
            if(matrizresidual[p[d]][d]<menor):
                menor = matrizresidual[p[d]][d]
            d = p[d]
        max_flow += menor
        n = t
        print("Fluxo: " + str(menor), end=" (")
        while(n != s):
            print( str(n) + " => ", end ="")
            matrizresidual[p[n]][n] -= menor
            matrizresidual[n][p[n]] += menor
            n = p[n]
        print(n, end =  ")\n")
        print("Matriz Residual: ")
        for mr in matrizresidual:
            for m in range(len(mr)):
                print(mr[m], end = "" )
                if(m!=len(mr)-1):
                    print(", ", end="")
            print("")
        print("\n")
    return max_flow

matriz = lerCSV("Atividade 12\grafo_ativ_12 - Página1.csv")
max_flow  = fordFulkerson(matriz, 1 ,5)

