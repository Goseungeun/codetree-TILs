n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
move = [(-1,0),(1,0),(0,-1),(0,1)]
vilage_cnt = 0
people_num = 0
answer = []

def can_people(x,y):
    if not(0 <= x < n and 0 <= y < n):
        return False
    if board[x][y] != 1:
        return False
    return True    

def dfs(cur_x,cur_y):
    global people_num
    for dx,dy in move:
        next_x, next_y = cur_x + dx, cur_y + dy
        if can_people(next_x,next_y):
            people_num += 1
            board[next_x][next_y] = 2
            dfs(next_x,next_y)

for i in range(n):
    for j in range(n):
        if can_people(i,j):
            vilage_cnt += 1
            people_num = 1
            board[i][j] = 2
            dfs(i,j)
            answer.append(people_num)

print(vilage_cnt)
answer.sort()
for a in answer:
    print(a)