from collections import deque

n,m = map(int,input().split())
answer = 0
hexagon = [[0] * (m+2)] + [[0] + list(map(int,input().split()))+[0] for _ in range(n)] + [[0]*(m+2)]
d = [[[0,-1],[0,1],[-1,-1],[-1,0],[1,-1],[1,0]],[[0,-1],[0,1],[-1,1],[-1,0],[1,1],[1,0]]]

def inRange(x,y):
    return 0 <= x < n+2 and 0 <= y < m+2

def dfs(x,y):
    if not inRange(x,y):
        return

    if hexagon[x][y] != 0:
        return
    
    global answer
    hexagon[x][y] = 2
    if x % 2 == 0 :
        d_1 = 0
    else:
        d_1 = 1

    for d_2 in d[d_1]:
        n_x,n_y = x + d_2[0] , y + d_2[1]
        if inRange(n_x,n_y) and hexagon[n_x][n_y] == 1:
            answer += 1
        
        dfs(n_x,n_y)

dfs(0,0)
print(answer)