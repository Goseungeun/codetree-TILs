n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()

def com(lotto,c):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return

    for i in range(c,len(num_list)):
        com(lotto+[num_list[i]],i+1)

com([],0)