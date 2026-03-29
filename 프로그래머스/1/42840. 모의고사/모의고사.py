def solution(answers):
    answer =[]
    people = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = []
    
    for i in range(3):
        count = 0
        for j in range(len(answers)) :
            if people[i][j%len(people[i])] == answers[j] :
                count +=1
        scores.append(count)
    max_score = max(scores)
    for k in range(len(scores)) :
        if max_score==scores[k] :
            answer.append(k+1)
    

    return answer