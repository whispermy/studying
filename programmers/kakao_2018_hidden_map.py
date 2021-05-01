def solution(n, arr1, arr2):
    answer = []
    
    for n in range (0,n):
        answer.append(str(bin(arr1[n] | arr2[n])))
    
    ans = []
    for i in answer:
        ans.append(i[2:])
        
    for i in range (0,len(ans)):
        while len(ans[i]) < n+1:
            ans[i] = '0'+ans[i]
    
    table = str.maketrans('01',' #')    

    for k in range(0,len(ans)):
        ans[k] = ans[k].translate(table)

    return ans