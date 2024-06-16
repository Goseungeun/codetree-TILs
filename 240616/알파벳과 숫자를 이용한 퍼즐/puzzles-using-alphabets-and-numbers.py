from itertools import product
n = int(input())
dic = {'B':[],'E':[],'S':[],'I':[],'G':[],'O':[],'M':[]}

for _ in range(n):
    alpha , num = input().split()
    dic[alpha].append(int(num))

def is_even(B,E,S,I,G,O,M):
    part1 = B + E + S + S + I + E
    part2 = G + O + E + S
    part3 = M + O + O
    result = part1 * part2 * part3

    if result % 2 == 0:
        return True
    else:
        return False

def count(dic):
    cnt = 0
    val = ['B','E','S','I','G','O','M']
    all_com = list(product(*[dic[v] for v in val]))
    
    for com in all_com:
        if is_even(*com):
            cnt+=1

    return cnt

print(count(dic))