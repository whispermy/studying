def solution(s):
    answer = []
    sub = []
    index = 0

    for i in range(0,len(s)):
        if s[i].isdecimal():
            if s[i+1] == ',':
                if index == 0:
                    sub.append(int(s[i]))
                else:
                    sub.append(int(s[index:i+1]))
                index = 0
            elif index == 0:
                index = i

        elif s[i] == '}':
            print('sub:', sub)
            answer.append(sub)
            sub = []
            index = 0
    
    return max(answer)


print(solution("{{20,111},{111}}"))