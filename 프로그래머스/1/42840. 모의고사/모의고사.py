def solution(answers):
    answer = [0,0,0]
    one = [1, 2, 3, 4, 5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if answers[i] == one[i%len(one)] :
            answer[0] += 1
        if answers[i] == two[i%len(two)] :
            answer[1] += 1
        if answers[i] == three[i%len(three)] :
            answer[2] += 1
            
    max_answer = max(answer)
    result = []
    for j in range(len(answer)) :
        if max_answer == answer[j] :
            result.append(j+1)
    return result