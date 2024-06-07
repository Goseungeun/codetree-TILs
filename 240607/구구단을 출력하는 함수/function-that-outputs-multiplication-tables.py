nums = list(map(int,input().split()))
nums.sort()

for i in range(nums[0],nums[2]+1):
    if i == nums[1]:
        continue
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j))