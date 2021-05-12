from itertools import combinations

def primenumber(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return sieve


def solution(nums):
    answer = primenumber(3000)
    comb = [i for i in combinations(nums,3)]
    ans = 0
    
    for i in comb:
        if answer[sum(i)] == True:
            ans += 1

    return ans
    