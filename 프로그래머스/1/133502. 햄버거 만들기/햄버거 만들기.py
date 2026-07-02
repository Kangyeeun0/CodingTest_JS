def solution(ingredient):
    answer = 0
    # 1 -> 빵, 2 -> 야채, 3 -> 고기
    # 1,2,3,1 순을 무조건 쌓여야 함
    stack = []
    
    for i in range(len(ingredient)) :
        ingre = ingredient[i]
        stack.append(ingre)

        if stack[-4:] == [1, 2, 3, 1] :
            for i in range(4) :
                stack.pop()
            answer+=1
        
    return answer