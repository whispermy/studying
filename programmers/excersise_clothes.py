# def solution(n, lost, reserve):
#     answer = 0
#     lostindex = 0
#     reserveindex = 0
#     list1 = []
    
#     for i in range (1,n+1):
#         list1.append(i)

#     print(list1)
        
#     for i in list1:
#         print(i,lostindex,reserveindex,answer)
#         if reserve[reserveindex] == list1[i]:
#             if reserve[reserveindex] == lost[lostindex]:
#                 answer += 2
#                 i += 1
#                 lostindex += 1
#                 reserveindex += 1
#                 if len(lost) <= lostindex:
#                     lostindex -= 1
#                 if len(reserve) <= reserveindex:
#                     reserveindex -= 1
#             else:
#                 reserveindex += 1
#                 if len(reserve) <= reserveindex:
#                     reserveindex -= 1
#                 answer += 1
                
#         elif lost[lostindex] == list1[i]:
#             if lost[lostindex] == reserve[reserveindex]:
#                 answer += 2
#                 i += 1
#                 lostindex += 1
#                 reserveindex += 1
#                 if len(lost) <= lostindex:
#                     lostindex -= 1
#                 if len(reserve) <= reserveindex:
#                     reserveindex -= 1
#             else:
#                 lostindex += 1
#                 if len(lost) <= lostindex:
#                     lostindex -= 1
#                 answer += 1
                
#         else:
#             answer += 1
            
            
#     return answer



# print("answer:",solution(5, [2,4] , [3]))

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    for i in range(1,n+1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    for i in range(1,n+1):
        if i in lost:
            if (i-1) in reserve:
                reserve.remove(i-1)
                lost.remove(i)
            elif (i+1) in reserve:
                reserve.remove(i+1)
                lost.remove(i)

    return n-len(lost)

print("answer:", solution(6,[1,3,5],[2,4,6]))
