n = int(input())
programers = list(map(int,input().split()))
programers.sort(reverse = True)

ball = 1
flag = True

for i in range(1,n-1):
    left_dist = programers[i-1] - programers[i]
    right_dist = programers[i] - programers[i+1]

    if left_dist < right_dist and flag:
        ball += 1
        flag = False
    elif left_dist >= right_dist:
        flag = True

print(ball)