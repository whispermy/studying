def solution(n):
    answer = []
    s = str(n)
    l = len(s)
    for i in range(0,l):
        answer.append(int(s[l-i-1]))
    return answer