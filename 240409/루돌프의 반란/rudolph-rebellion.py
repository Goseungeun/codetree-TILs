import sys
input = sys.stdin.readline
n,m,p,c,d = map(int,input().split())
board = [[0] * (n+1) for _ in range(n+1)] #게임판 

ru_r,ru_c = map(int,input().split())
board[ru_r][ru_c] = 31  #board 에 루돌프 위치 표시

santas_status = [[0,0] for _ in range(p+1)] #산타의 상태 표시(탈락,기절한 턴)
santas = [[0] for _ in range(p+1)] #각 산타의 위치 좌표 저장
santa_score = [0] * (p+1)

for _ in range(p):
    p_n,s_r,s_c = map(int,input().split())
    santas[p_n] = [s_r,s_c]   #산타 번호, 위치 입력
    board[s_r][s_c] = p_n #board에 산타 위치 표시

def find_closest_santa(ru_r,ru_c,santas):
    temp = []
    for s_n in range(1,p+1):
        s_r,s_c = santas[s_n]
        if santas_status[s_n][0] == 0:
            dist = ((ru_r - s_r)**2) + ((ru_c - s_c)**2)
            temp.append([dist,s_r,s_c,s_n])
    temp.sort(key = lambda x:(x[0],-x[1],-x[2]))

    return temp[0][3]

def interaction(santa_num,direction):
    s_cr,s_cc = santas[santa_num]
    s_nr,s_nc = s_cr+direction[0], s_cc + direction[1]

    if 1 <= s_nr <=n and 1 <= s_nc <= n:
        if board[s_nr][s_nc] != 0 :
            interaction(board[s_nr][s_nc],direction)
        board[s_nr][s_nc] = santa_num
        santas[santa_num] = [s_nr,s_nc]
        return
    else:
        santas_status[santa_num][0] = -1
        return

def crush(Ru,direction,santa_num,now_turn):
    santas_status[santa_num][1] = now_turn+2
    s_cr,s_cc = santas[santa_num]
    if Ru:
        santa_score[santa_num] += c
        s_nr,s_nc = s_cr+(c*direction[0]), s_cc + (c*direction[1])
    else:
        santa_score[santa_num] += d
        direction[0],direction[1] = -direction[0],-direction[1]
        s_nr,s_nc = s_cr+(d*direction[0]), s_cc + (d*direction[1])

    if 1<= s_nr <=n and 1 <= s_nc <= n:
        if board[s_nr][s_nc] != 0 :
            interaction(board[s_nr][s_nc],direction)
        board[s_nr][s_nc] = santa_num
        santas[santa_num] = [s_nr,s_nc]     
    else:
        santas_status[santa_num][0] = -1

    return 
    
def move_ru(ru_r,ru_c,closest_santa,now_turn):
    board[ru_r][ru_c] = 0
    r_d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]    #상하좌우 대각선
    s_r,s_c = santas[closest_santa]
    current_dist = ((ru_r - s_r)**2) + ((ru_c - s_c)**2)
    
    for dr,dc in r_d:
        n_r = ru_r + dr
        n_c = ru_c + dc
        if 1<= n_r <=n and 1<= n_c <=n:
            dist = ((n_r - s_r)**2) + ((n_c - s_c)**2)
            if current_dist > dist:
                current_dist = dist
                next_r,next_c = n_r,n_c
                direction = [dr,dc]
    ru_r,ru_c = next_r,next_c
    
    if board[next_r][next_c] != 0:
        crush(True,direction,board[next_r][next_c],now_turn)
    board[next_r][next_c] = 31
    ru_r,ru_c = next_r,next_c
    return ru_r,ru_c

def move_santa(santa_num,ru_r,ru_c,now_turn):
    s_cr,s_cc = santas[santa_num]
    board[s_cr][s_cc] = 0
    flag = 0
    s_d = [(-1,0),(0,1),(1,0),(0,-1)]
    current_dist = ((ru_r - s_cr)**2) + ((ru_c - s_cc)**2)
    
    for dr,dc in s_d:
        s_nr = s_cr + dr
        s_nc = s_cc + dc
        if 1<= s_nr <=n and 1<= s_nc <=n and (board[s_nr][s_nc] == 0 or board[s_nr][s_nc] == 31):
            dist = ((ru_r - s_nr)**2) + ((ru_c - s_nc)**2)
            if current_dist > dist:
                flag = 1
                current_dist = dist
                next_r,next_c = s_nr,s_nc
                direction = [dr,dc]
    if flag == 1:
        santas[santa_num] = next_r,next_c
        if board[next_r][next_c] == 31:
            crush(False,direction,santa_num,now_turn)
        else:
            board[next_r][next_c] = santa_num
    else:
        board[s_cr][s_cc] = santa_num

for now_turn in range(m):
    if sum([ii[0] for ii in santas_status]) == -p:
        break   #모든 산타가 죽으면 게임 종료
    closest_santa_num = find_closest_santa(ru_r,ru_c,santas)
    ru_r,ru_c = move_ru(ru_r,ru_c,closest_santa_num,now_turn)
    # 1번 산타부터 순서대로 움직이기
    for s_n in range(1,p+1):
        if santas_status[s_n][1] <= now_turn and santas_status[s_n][0] == 0:
            move_santa(s_n,ru_r,ru_c,now_turn)
    
    for s_n in range(1,p+1):
        if santas_status[s_n][0] ==0:
            santa_score[s_n] += 1
    # print(now_turn)
    # # print(board)
    # print("status:",santas_status)
    # # print("score: ",santa_score)
print(' '.join(map(str,santa_score[1:])))