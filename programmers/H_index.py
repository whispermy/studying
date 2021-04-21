# citations = [0,1,1]

# answer = 0
# citations.sort()

# print(citations)

# size = len(citations)
# answer = size // 2
# print(answer, size)
# count = 0

# while(True):
#     for i in range (len(citations)):
#         if citations[i] > answer:
#             count += 1

#     if count > answer:
#         answer += 1
#         count = 0
#     else:
#         print(answer)
#         print(citations[size-1])
#         if citations[size-1] == answer:
#             print(answer-1)
#             break
#         else:
#             print(answer)
#             break
        
#         break
#         # return answer-1


def solution(citations):
    answer = 0
    citations.sort()
    
    size = len(citations)
    answer = size // 2
    count = 0
    while(True):
        for i in range (len(citations)):
            if citations[i] > answer:
                count += 1

        if count > answer:
            answer += 1
            count = 0
        else:
            if citations[size-1] == 0:
                return 0
            else:
                return answer





                