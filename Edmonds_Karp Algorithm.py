import time

def edmondskarp(capacitymatrix, s, t):
    n = len(capacitymatrix)
                
    flow = 0
    flowmatrix = [[0 for y in range(n)] for x in range(n)]
    while True:
        pathflow, path = breadfirstsearch(capacitymatrix, s, t, flowmatrix)
        if pathflow == 0:
            break
        flow = flow + pathflow
        v = t
        while v != s:
            u = path[v]
            flowmatrix[u][v] = flowmatrix[u][v] + pathflow
            flowmatrix[v][u] = flowmatrix[v][u] - pathflow
            v = u
    return flow


def breadfirstsearch(capacitymatrix, s, t, flowmatrix):
    n = len(capacitymatrix)
    
    queue = [s]
    path = ['untouched-edge' for x in range(n)]
    pathflow = [0 for x in range(n)]
    pathflow[s] = float('inf')
    while (len(queue) > 0):
        u = queue.pop(0)
        for v in range(n):
            if capacitymatrix[u][v] > flowmatrix[u][v] and path[v] == 'untouched-edge':
                path[v] = u
                pathflow[v] = min(pathflow[u], capacitymatrix[u][v] - flowmatrix[u][v])
                if v == t:
                    return pathflow[t], path
                queue.append(v)
    return 0, path


capacitymatrix = [[0, 3, 3, 0, 0, 0],
                 [0, 0, 2, 3, 0, 0], 
                 [0, 0, 0, 0, 2, 0], 
                 [0, 0, 0, 0, 4, 2], 
                 [0, 0, 0, 0, 0, 2], 
                 [0, 0, 0, 0, 0, 3]] 

s = 0
t = 5

ti = time.time()
maxflow = edmondskarp(capacitymatrix, s, t)
tf = time.time()

print("edmondkarp solution :",maxflow,"\ntime :", tf-ti) # time print
