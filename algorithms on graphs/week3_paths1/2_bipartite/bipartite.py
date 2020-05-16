#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    partition = [len(adj)] * len(adj)
    partition=[0 for i in range(len(adj))]
    partition[0] = 1
    queue = []
    queue.append(0)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if partition[v] == partition[u]:
                return 0
            if partition[v] ==0:
                partition[v]=-partition[u]
                queue.append(v)
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
