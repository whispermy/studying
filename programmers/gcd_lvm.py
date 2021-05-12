def solution(n, m):
    answer = []
    lvm = n*m
    while m:
        n,m = m,n%m
    answer.append(n)
    answer.append(lvm/n)
    return answer