import sys

def swap(idx, str1):
    str1 = list(str1)  # 문자열을 리스트로 변환 (문자열은 불변이기 때문에 수정 가능하도록 변환)
    if idx - 1 >= 0:
        str1[idx - 1] = '1' if str1[idx - 1] == '0' else '0'
    str1[idx] = '1' if str1[idx] == '0' else '0'
    if idx + 1 < n:
        str1[idx + 1] = '1' if str1[idx + 1] == '0' else '0'
    return ''.join(str1)  # 리스트를 다시 문자열로 변환하여 반환

def get_cnt(str1):
    cnt = 0
    for i in range(1, n):
        if str1[i - 1] == str2[i - 1]:
            continue
        cnt += 1
        str1 = swap(i, str1)
    
    if str1[n - 1] != str2[n - 1]:
        return float('inf')
    
    return cnt

# 입력 받기
n = int(input())
str1 = input().strip()
str2 = input().strip()

# 첫 번째 시도
tmp1 = str1
ans1 = get_cnt(tmp1)

# 두 번째 시도 (첫 번째 스위치 스왑)
tmp2 = swap(0, str1)
ans2 = get_cnt(tmp2)
if ans2 != float('inf'):
    ans2 += 1

# 결과 계산
ans = min(ans1, ans2)
if ans == float('inf'):
    ans = -1

# 결과 출력
print(ans)