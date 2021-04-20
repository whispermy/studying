# def solution(n, computers):
#     answer = 0
#     for l in (0,n):
                
                
#     return answer
answer = 0
index = []
n = 8

for i in range (0,n):
    index.append(i)
    
for i in range (0,n):
    for j in range (0,n):
        if computers[i][j] == 1:
            if index[i] == i:
                index[i] = 0 
            if index[j] == j:
                index[j] = 0
    
    for k in range (0,n):
        if index[k] != 0:
            i = index[k]
            answer += 1
            break