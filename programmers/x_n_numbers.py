def solution(x, n):
    answer = []
    answer.append(x)
    a = x
    for i in range(0,n-1):
        a += x
        answer.append(a)
        
    return answer