def solution(n):
    s = str(n)
    ans = sorted(s,reverse=True)
    p = ''
    for i in ans:
        p += i
    return int(p)