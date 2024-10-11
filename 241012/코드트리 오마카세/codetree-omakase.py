from collections import defaultdict

l,q = map(int,input().split())
queue = [] # 명령어 저장 list
s4p = defaultdict(list) #특정 사람의 초밥 정보 {name : [mst,s_pos]}
enter_t = {} #사람 별 입장 시간
exit_t = {} #사람 별 퇴장 시간
position = {} #사람 별 위치
names = set()

def add_eating_time(s_pos,p_pos):
    if s_pos <= p_pos:
        return p_pos - s_pos
    else:
        return p_pos + l - s_pos
for _ in range(q):
    query = list(input().split())
    if query[0] == '300':
        code, time = map(int,query)
        queue.append([code,time])
    else:
        code,time,x = map(int,query[:3])
        queue.append([code,time,x,query[3]])
    
    if code == 100:
        s4p[query[3]].append([time,x])
    elif code == 200:
        enter_t[query[3]] = exit_t[query[3]] = time
        position[query[3]] = x
        names.add(query[3])

for name in names:
    for s_time,s_pos in s4p[name]:
        if s_time < enter_t[name]:
            s_pos = (s_pos + (enter_t[name]-s_time)) % l
            eating_time = enter_t[name]
        else:
            eating_time = s_time
        
        add_time = add_eating_time(s_pos,position[name])
        eating_time += add_time

        exit_t[name] = max(exit_t[name],eating_time)
        queue.append([150,eating_time])

for name in names:
    queue.append([250,exit_t[name]])

queue.sort(key = lambda x:(x[1],x[0]))
p_num = 0
s_num = 0

for q in queue:
    if q[0] == 100:
        s_num += 1
    elif q[0] == 150:
        s_num -=1
    elif q[0] == 200:
        p_num += 1
    elif q[0] == 250:
        p_num -= 1
    elif q[0] == 300:
        print(p_num, s_num)