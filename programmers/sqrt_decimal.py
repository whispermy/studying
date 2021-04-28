import math

def solution(n):
    answer = math.sqrt(n)
    if answer%1 == 0:
        return (answer+1)**2
    
    return -1