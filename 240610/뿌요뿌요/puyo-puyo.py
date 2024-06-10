import sys
sys.setrecursionlimit(50000)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

def can_go(x,y,t):
    if not(0<=x<n and 0<=y<n):
        return False
    if board[x][y] == 0 or board[x][y] != t:
        return False
    return True

def dfs(x,y,t):
    d_xy = [(1,0),(-1,0),(0,1),(0,-1)]
    cnt = 1

    for dx,dy in d_xy:
        nx,ny = x+dx,y+dy
        if can_go(nx,ny,t):
            board[nx][ny] = 0
            cnt += dfs(nx,ny,t)
    return cnt

max_cnt = -1
bomb = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            target = board[i][j]
            board[i][j] = 0
            cnt = dfs(i,j,target)
            if cnt >= 4:
                bomb += 1
            max_cnt = max(max_cnt,cnt)
print(bomb,max_cnt)