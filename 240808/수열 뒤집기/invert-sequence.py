N,K = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

num_list = [i + 1 for i in range(N)]

for _ in range(K):
    num_list = num_list[:A1-1] + num_list[A2-1:A1-2:-1] + num_list[A2:]
    num_list = num_list[:B1-1] + num_list[B2-1:B1-2:-1] + num_list[B2:]

print('\n'.join(list(map(str,num_list))))