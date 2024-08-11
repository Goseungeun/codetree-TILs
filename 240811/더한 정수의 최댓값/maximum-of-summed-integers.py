n = int(input())
nums = list(map(int,input().split()))

def left_redpoint(n):
    result = (sum(nums) - nums[0]) * 2
    min_sub = nums[1] * 2

    for i in range(2,n):
        ssub = nums[i]
        for j in range(1,i+1):
            ssub+=nums[j]
        if min_sub <= ssub:
            break
        else:
            min_sub = ssub
    result -= min_sub
    return result

def right_redpoint(n):
    result = (sum(nums) - nums[-1]) * 2
    min_sub = nums[-2] * 2

    for i in range(n-3,0,-1):
        ssub = nums[i]
        for j in range(n-2,i-1,-1):
            ssub+=nums[j]
        if min_sub <= ssub:
            break
        else:
            min_sub = ssub
    result -= min_sub
    return result

if (nums[0]+nums[1] < nums[-1]+nums[-2]):
    result = left_redpoint(n)
elif(nums[0]+nums[1] > nums[-1]+nums[-2]):
    result = right_redpoint(n)
elif (nums[0]+nums[1] == nums[-1]+nums[-2]):
    if (nums[0] <= nums[-1]):
        result = left_redpoint(n)
    else:
        result = right_redpoint(n)

print(result)