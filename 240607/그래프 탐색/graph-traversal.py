n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    for c_v in graph[node]:
        if not visit[c_v]:
            visit[c_v] = 1
            dfs(c_v)

visit[1] = 1
dfs(1)
print(sum(visit) -1)