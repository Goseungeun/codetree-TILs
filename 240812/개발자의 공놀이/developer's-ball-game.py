n = int(input())
programers = list(map(int,input().split()))
programers.sort(reverse = True)

ball = 1

for i in range(1,n-1):
    left_dist = programers[i-1] - programers[i]
    right_dist = programers[i] - programers[i+1]

    if left_dist < right_dist:
        ball += 1

print(ball)