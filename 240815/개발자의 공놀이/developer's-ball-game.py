n = int(input())
programers = list(map(int,input().split()))
programers.sort(reverse = True)

next_pro = [0] * n
in_degree = [0] * n
ball = 0

next_pro[0] = in_degree[1] = 1
next_pro[n-1] , in_degree[n-2] = n-2, 1

for i in range(1,n-1):
    nxt = i+1 if programers[i] - programers[i+1] <= programers[i-1] - programers[i] else i-1
    next_pro[i] = nxt
    in_degree[nxt] += 1

for j in range(n):
    if (in_degree[j] == 0 or (next_pro[next_pro[j]] == j and in_degree[j] == 1 and in_degree[next_pro[j]] == 1 and j < next_pro[j])):
        ball += 1

print(ball)