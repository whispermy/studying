def solution(clothes):
    answer = 0
    keys = clothes[1][1]
    number = 0
    line = []
    mul = 1
        
    while clothes:
        for i in clothes:
            if i[1] == keys:
                number += 1
                clothes.remove(i)

        line.append(number)
        number = 0
        
    for j in line:
        answer += j
        mul *= j
        
    return answer+mul


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))