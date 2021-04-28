def solution(arr):
    answer = []
    arr.remove(min(arr))
    
    if arr == []:
        return [-1]
    else:
        return arr