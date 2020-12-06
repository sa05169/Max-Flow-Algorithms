import time

def push(u, v):
    send = min(overflow[u], capacitymatrix[u][v] - flowmatrix[u][v])
    flowmatrix[u][v] += send
    flowmatrix[v][u] -= send
    overflow[u] -= send
    overflow[v] += send

def relabel(u):
    min_height = float('inf')
    for v in range(n):
        if capacitymatrix[u][v] > flowmatrix[u][v]:
            min_height = min(min_height, height[v])
    height[u] = min_height + 1

def discharge(u):
    while overflow[u] > 0:
        if seen[u] < n:
            v = seen[u]
            if capacitymatrix[u][v] > flowmatrix[u][v] and height[u] > height[v]:
                push(u, v)
            else:
                seen[u] += 1
        else:
            relabel(u)
            seen[u] = 0
                
def push_relabel(source, sink):
    global height, overflow, seen, nodelist, capacitymatrix, flowmatrix, n
    flowmatrix = [[0] * n for _ in range(n)]

    height = [0] * n
    overflow = [0] * n
    seen   = [0] * n
    nodelist = [i for i in range(n) if i != source and i != sink]

    height[source] = n
    overflow[source] = float('inf')
    for v in range(n):
        push(source, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            nodelist.insert(0, nodelist.pop(p))
            p = 0
        else:
            p += 1

    return sum(flowmatrix[source])

capacitymatrix = [[0, 3, 3, 0, 0, 0],
                 [0, 0, 2, 3, 0, 0],
                 [0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 4, 2],
                 [0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 0, 3]]

s = 0
t = 5
n = len(capacitymatrix)
flowmatrix = []

ti = time.time()
maxflow = push_relabel(s, t)
tf = time.time()

print("push-relabel's solution :", maxflow, "\ntime :", tf-ti)
