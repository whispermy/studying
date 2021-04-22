# def solution(n, computers):
#     answer = 0
#     for l in (0,n):
                
                
# #     return answer
# answer = 0
# index = []
# n = 8

# for i in range (0,n):
#     index.append(i)
    
# for i in range (0,n):
#     for j in range (0,n):
#         if computers[i][j] == 1:
#             if index[i] == i:
#                 index[i] = 0 
#             if index[j] == j:
#                 index[j] = 0
    
#     for k in range (0,n):
#         if index[k] != 0:
#             i = index[k]
#             answer += 1
#             break

from collections import deque

def solution(n, computers):
    answer = 0
    index = [False]*(n+1)
    # queue = deque([1])
    queue = []
        
    for i in range (1,n+1):
        if index[i] == False:
            queue = deque([i])
            index[i] =  True
            
            while queue:
                v = queue.popleft()

                c = computers[v-1]
                for k in range (0,len(c)):
                    if c[k] == 1:
                        if not index[k+1]:
                            queue.append(k+1)
                            index[k+1] = True
              
            answer += 1
            
    
    return answer

print(solution(3,[[1,1,0],[1,1,1],[0,1,1]]))