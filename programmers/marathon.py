participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

participant.sort()
completion.sort()
k = 0

# for i in completion:
#     if i != participant[k]:
#         print("end:",i)
#     else:
#         print('i:',i,'k:',participant[k])
#         k += 1
#         if k == len(completion):
#             print("end~~~",participant[k])

# for i in completion:
#     if i == participant[k]:
#         print('delete', participant[k])
#         # del participant[k]
#         k += 1
#     else:
#         print(participant[k])

# print(participant[k])\



def solution(participant, completion):
    participant.sort()
    completion.sort()
    k = 0
    
    for i in completion:
        if i == participant[k]:
            # del participant[k]
            k += 1
        else:
            return participant[k]
    return participant[k]