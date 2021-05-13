from itertools import combinations

def solution(numbers):
    answer = []
    lt = [sum(i) for i in combinations(numbers,2)]
    lt.sort()
    
    for i in lt:
        if i not in answer:
            answer.append(i)
        
    return answer