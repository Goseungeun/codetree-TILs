n,k = map(int,input().split())
points = list(map(int,input().split()))
result = 0
i = 1
obj_set = set(points)
while k > 0:
    prev_num_obj = len(obj_set)
    for p in points:
        obj_set.update([p-i,p+i])
    num_obj = len(obj_set) - prev_num_obj
    result += num_obj * i
    k -= num_obj
    i += 1
    
if k < 0:
    result += k*(i-1)

print(result)