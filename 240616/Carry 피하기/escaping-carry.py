n = int(input())
max_num = 0
num_list = [int(input()) for _ in range(n)]

def is_notcarry(num1, num2):
    while (num1 > 0 or num2 > 0):
        a = num1 % 10
        b = num2 % 10

        if a+b >= 10:
            return False
        
        num1 = num1 // 10
        num2 = num2 // 10

    return True

def backtraking(count,depth,sum_num):
    global ans
    ans = max(ans,count)

    if depth == n:
        return
    
    for i in range(depth,n):
        if is_notcarry(sum_num,num_list[i]):
            backtraking(count + 1, i+1, sum_num+num_list[i])
        
ans = 0
backtraking(0,0,0)

print(ans)