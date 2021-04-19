# def move(alpa):
#     mvcount = 0
#     if ord(alpa) - ord("M") <= 0:
#         mvcount = ord("M") - ord(alpa)
#     else:
#         mvcount = ord("Z") - ord(alpa)

#     return mvcount



# def solution(name):
#     answer = 0
#     lmove = 0
#     rmove = 0
#     l = len(name)

#     for i in name:
#         answer += move(i)

    




#     return answer



def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]
    print(m)       

    answer = 0
    where = 0

    while True:    
        answer += m[where]
        print('a',m[where])
        m[where] = 0
        print(answer)

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
            print('left',m[where - left])
        while m[where + right] <= 0:
            right += 1
            print('right',m[where + right])

        answer += left if left < right else right
        print('answer',answer)
        where += -left if left < right else right
        print('where',where)

    return answer

m = [ min(ord(c) - 65, 91-ord(c)) for c in "name"]  
print("m",m)
print("answer:", solution("ABBBBBCZ"))
