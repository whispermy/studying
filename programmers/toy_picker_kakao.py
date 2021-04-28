def solution(board, moves):
    answer = 0
    stack = []
    
    for i in moves:
        for j in range (0,len(board)):
            if board[j][i-1] != 0:
                if stack != [] and board[j][i-1] == stack[len(stack)-1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[j][i-1])
                    
                board[j][i-1] = 0   
                break

    return answer*2