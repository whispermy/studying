def solution(lottos, win_nums):
    cnt = 0
    fault = 0
    rank = 0
    
    for i in range(0,6):
        cnt = 0
        if lottos[i] == 0:
            fault += 1
        else:
            while cnt < 6:
                if lottos[i] == win_nums[cnt]:
                    rank += 1
                    break
                cnt += 1
    
    first = 7-rank-fault
    end = 7-rank
    if end > 6:
        end = 6
    if first < 1:
        first = 1
    if first > 6:
        first = 6
        
    return [first, end]