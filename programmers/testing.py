def solution(answers):
    answer = []
    student1 = [1,2,3,4,5,1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    std1count = 0
    std2count = 0
    std3count = 0
    std1index = 0
    std2index = 0
    std3index = 0
    std1size = 10
    std2size = 8
    std3size = 10
    for i in answers:
        if i == student1[std1index]:
            std1count += 1
        if i == student2[std1index]:
            std2count += 1
        if i == student3[std1index]:
            std3count += 1
        
        std1index += 1
        std2index += 1
        std3index += 1
    
        if std1index == std1size:
            std1index = 0
        if std2index == std2size:
            std2index = 0
        if std3index == std3size:
            std3index = 0
            
    print(std1count, std2count, std3count)
    if std1count > std2count:
        if std1count > std3count:
            answer.append(1)
            return answer
        elif std1count == std3count:
            answer.append(1)
            answer.append(3)
            return answer
        else:
            answer.append(3)
            return answer
    elif std1count == std2count:
        if std1count > std3count:
            answer.append(1)
            answer.append(2)
            return answer
        elif std1count == std3count:
            answer.append(1)
            answer.append(2)
            answer.append(3)
            return answer
        else:
            answer.append(3)
            return answer
    else:
        if std2count > std3count:
            answer.append(2)
            return answer
        elif std2count == std3count:
            answer.append(2)
            answer.append(3)
            return answer
        else:
            answer.append(3)
            return answer

lists = [5,5,5,1,4,1]

print(solution(lists))