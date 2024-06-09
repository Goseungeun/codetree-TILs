n = int(input())
d_ij = [(1,-1),(1,1),(-1,1),(-1,-1),(0,-1)]

r_s = n*2-1
answer  = [[32]*(r_s) for _ in range(r_s)]

i,j = 0,n-1
alpah = 65
d = 0

while True:
    answer[i][j] = alpah
    alpah += 1
    
    if i == n-1 and j == n-1:
        break
    if d == 0:
        i += d_ij[d][0]
        j += d_ij[d][1]
        if j == 0 or answer[i+1][j] != 32:
            d = 1
    elif d == 1:
        i += d_ij[d][0]
        j += d_ij[d][1]
        if i == r_s-1 or answer[i][j+1] != 32:
            d = 2
    elif d == 2:
        i += d_ij[d][0]
        j += d_ij[d][1]
        if j == r_s-1 or answer[i-1][j] != 32:
            d = 3
    elif d == 3:
        i += d_ij[d][0]
        j += d_ij[d][1]
        if i == 0 or answer[i-1][j-1] != 32:
            d = 4
    elif d == 4:
        i += d_ij[d][0]
        j += d_ij[d][1]
        d = 0
    
    if alpah > 90:
        alpah = 65


for a in answer:
    for an in a:
        print(chr(int(an)),end = " ")
    print()