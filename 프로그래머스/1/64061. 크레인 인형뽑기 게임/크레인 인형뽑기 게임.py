from collections import deque
def solution(board, moves):
    answer = 0
    stack = []
    arr = deque([deque([]) for i in range(len(board))])

    
    for i in range(len(board)-1, -1, -1) :
        
        for j in range(len(board[0])) :
            if board[i][j] !=0 :
                arr[j].append(board[i][j])

    for move in moves :
        if arr[move-1] :
            # prot(arr[move])
            value = arr[move-1].pop()
            stack.append(value)

        if len(stack) > 1 :
            if stack[-1] == stack[-2] :
                answer+=2
                stack.pop()
                stack.pop()
    # print(stack)
        
    return answer