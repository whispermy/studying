def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    string = ''
    for i in answer:
        string += i
    return string