import time

def dinics(capacitymatrix, s, t):
    n = len(capacitymatrix)
    flowmatrix = [n*[0] for u in range(n)]
    flow = 0
    while True:
        level = breadthfirstsearch(capacitymatrix, flowmatrix, s, t)
        if level[t] == 0:
            break
        flow = flow + depthfirstsearch(capacitymatrix, flowmatrix, t, level, s, float('inf'))
    return flow

def breadthfirstsearch(capacitymatrix, flowmatrix, s, t):
    n = len(capacitymatrix)
    queue = [s]
    level = [0]*n
    level[s] = 1
    while queue:
        v = queue.pop(0)
        for u in range(n):
            if (flowmatrix[v][u] < capacitymatrix[v][u]) and (level[u] == 0):
                level[u] = level[v] + 1
                queue.append(u)
    return level

def depthfirstsearch(capacitymatrix, flowmatrix, t, level, v, inflow):
    if v == t:
        return inflow
    pathflow = 0
    for u in range(len(capacitymatrix)):
        if (level[u] == level[v] + 1) and (flowmatrix[v][u] < capacitymatrix[v][u]):
            outflow = min(inflow, capacitymatrix[v][u] - flowmatrix[v][u])
            f = depthfirstsearch(capacitymatrix, flowmatrix, t, level, u, outflow)
            flowmatrix[v][u] = flowmatrix[v][u] + f
            flowmatrix[u][v] = flowmatrix[u][v] - f
            inflow = inflow - f
            pathflow = pathflow + f
    return pathflow

capacitymatrix = [[0, 3, 3, 0, 0, 0],
                 [0, 0, 2, 3, 0, 0],
                 [0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 4, 2],
                 [0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 3]]

s = 0
t = 5

ti = time.time()
maxflow = dinics(capacitymatrix, s, t)
tf = time.time()

print("dinic's solution :", maxflow, "\ntime :", tf-ti)
