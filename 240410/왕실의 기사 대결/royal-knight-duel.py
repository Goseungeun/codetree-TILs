l,n,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(l)] 
knight = []
knight_damage = [0] * n

for _ in range(n):
    r,c,h,w,k = map(int,input().split())
    knight.append([r-1,c-1,h,w,k])

dir = [(-1,0),(0,1),(1,0),(0,-1)]   #이동 방향 (상,우,하,좌)

def make_knight_board(knight):
    knight_board = [[-1] * l for _ in range(l)]
    for knight_num in range(len(knight)):
        r,c,h,w,k = knight[knight_num]
        if k>0:
            for i in range(r,r+h):
                for j in range(c,c+w):
                    knight_board[i][j] = knight_num
    return knight_board

def move(knight_num,d):
    # print(knight_num)
    n_cr,n_cc,h,w = knight[knight_num][0],knight[knight_num][1],knight[knight_num][2],knight[knight_num][3]
    n_nr = n_cr + dir[d][0]
    n_nc = n_cc + dir[d][1]
    
    for i in range(n_nr,n_nr+h):
        for j in range(n_nc,n_nc+w):
            if 0<=i<l and 0<=j<l:
                if board[i][j] == 2:
                    return False
                elif knight_board[i][j] != -1 and knight_board[i][j] != knight_num:
                    if not(move(knight_board[i][j],d)):
                        return False
            else:
                return False
    knight[knight_num][0] = n_nr
    knight[knight_num][1] = n_nc
    return True

def damage(knight,move_knight_num):
    for knight_num in range(len(knight)):
        if knight_num == move_knight_num:
            continue
        r,c,h,w,k = knight[knight_num]
        if k > 0 :
            ddd = 0
            for i in range(r,r+h):
                for j in range(c,c+w):
                    if board[i][j] == 1:
                        k -= 1
                        ddd += 1
        knight[knight_num][4] = k
        knight_damage[knight_num] = ddd

knight_board = make_knight_board(knight)
# print("initial :", knight_board)

for _ in range(q):
    k_n,d = map(int,input().split())
    if move(k_n-1,d):
        damage(knight,k_n-1)
        # print('knight_status : ',knight)
        knight_board = make_knight_board(knight)
result = 0
for knight_num in range(n):
    if knight[knight_num][4] > 0:
        result += knight_damage[knight_num]

print(result)

# print(knight)
# print("final : ",knight_board)