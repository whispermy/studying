array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
answer = []

for i in commands:
    start = i[0]-1
    end = i[1]
    val = i[2]-1
    
    sublist = array[start:end]
    sublist.sort()
    ans = sublist[val]
    answer.append(ans)

