numbers = [3, 30, 34, 5, 9]

answer = ''
substring = []
subnumber = ''

for i in range (len(numbers)):
    subnumber = str(numbers[i])
    substring.append(subnumber)
    
substring.sort(reverse=True)
print(substring)

for i in range (len(substring)):
    answer = answer + substring[i]
    
print(answer)