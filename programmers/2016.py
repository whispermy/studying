def solution(a, b):
    answer = ''
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    days = 0
    
    for i in range(1,a):
        days += month[i]
    
    days += b
    
    return day[days%7]

print(solution(1,1))