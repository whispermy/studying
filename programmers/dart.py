def cal(st):
    i = int(st[0])
    if st[1] == 'S':
        return i
    if st[1] == 'D':
        return i*i
    if st[1] == 'T':
        return i*i*i
    
    
def solution(dartResult):
    answer = 0
    first = 0
    second = 0
    third = 0
    
    for i in range (0,len(dartResult)):
        if dartResult[i] == '2':
            if dartResult[i-1] == '*':
                first = cal(dartResult[:i-2]) * 2
                answer = i
            elif dartResult[i-1] == '#':
                first = cal(dartResult[:i-2]) * -1
                answer = i
            else:
                first = cal(dartResult[:i-2])
                answer = i
                
        if dartResult[i] == '3':
            if dartResult[i-1] == '*':
                second = cal(dartResult[answer:i-2]) * 2
                first *= 2
                answer = i
            elif dartResult[i-1] == '#':
                second = cal(dartResult[answer:i-2]) * -1
                answer = i
            else:
                second = cal(dartResult[answer:i-2])
                answer = i
            
            if dartResult[i+1] == '*':
                third = cal(dartResult[i:i+1]) * 2
                second *= 2

            elif dartResult[i-1] == '#':
                third = cal(dartResult[i:i+1]) * -1
            else:
                third = cal(dartResult[i:i+1])
                
                
    return first+second+third




print("hello")
print('solution: ' + solution('1S2D*3T'))

