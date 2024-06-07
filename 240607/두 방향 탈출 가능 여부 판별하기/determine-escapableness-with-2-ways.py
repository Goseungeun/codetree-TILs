n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
flag = False

def can_go(x,y):
    if not(0 <= x < n and 0 <= y < m):
        return False
    if board[x][y] != 1:
        return False
    return True

def dfs(cur_x,cur_y):
    global flag
    if cur_x == n-1 and cur_y == m-1:
        flag = True
        return

    move = [(0,1),(1,0)]
    for dx,dy in move:
        next_x,next_y = cur_x + dx, cur_y + dy

        if can_go(next_x,next_y):
            board[next_x][next_y] = 2
            dfs(next_x,next_y)

board[0][0] = 2
dfs(0,0)
if flag:
    print(1)
else:
    print(0)