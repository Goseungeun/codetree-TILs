import sys
sys.setrecursionlimit(10 ** 5)

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

max_h = max(map(max,board))

def can_go(x,y,k):
    if not (0<=x<n and 0<=y<m):
        return False
    if board[x][y] <= k:
        return False
    if safe[x][y] == True:
        return False
    return True

def dfs(x,y,k):
    d_ij = [(1,0),(-1,0),(0,1),(0,-1)]

    for di,dj in d_ij:
        nx,ny = x + di, y + dj

        if can_go(nx,ny,k):
            safe[nx][ny] = True
            dfs(nx,ny,k)
    return
ans = {}
for k in range(1,max_h+1):
    cnt = 0
    safe = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] > k and not safe[i][j]:
                cnt += 1
                safe[i][j] = True
                dfs(i,j,k)
            ans[k] = cnt

key,value = -1,-1
for i,j in ans.items():
    if value < j:
        value = j
        key = i

print(key,value)