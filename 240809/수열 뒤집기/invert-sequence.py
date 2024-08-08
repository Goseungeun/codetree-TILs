N,K = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

num_list = [i + 1 for i in range(N)]

def reversed_list(num_list,start,end):
    while start < end:
        num_list[start],num_list[end] = num_list[end],num_list[start]

        start += 1
        end -= 1

for _ in range(K%12):
    reversed_list(num_list,A1-1,A2-1)
    reversed_list(num_list,B1-1,B2-1)

print('\n'.join(list(map(str,num_list))))