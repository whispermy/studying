def solution(s):
    answer = list(map(str, s.split(' ')))
    ans = ''
    for i in range(0,len(answer)):
        for j in range(0,len(answer[i])):
            if j == 0:
                ans += answer[i][j].upper()
            elif j % 2 == 1:
                ans += answer[i][j].lower()
            else:
                ans += answer[i][j].upper()
        ans += ' '
    return ans[:len(ans)-1]