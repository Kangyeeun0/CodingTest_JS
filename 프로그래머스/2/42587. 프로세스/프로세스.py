def solution(priorities, location):
    answer = 0
    q = []
    arr_prior=[]
    
    for i in range(len(priorities)) :
        arr_prior.append([i, priorities[i]])

    while len(q)<len(priorities) :
        target = arr_prior[0]
        if target[1] < max(x[1] for x in arr_prior) :
            arr_prior.pop(0)
            arr_prior.append(target)
        else :
            arr_prior.pop(0)
            q.append(target)
    
    for j in range(len(q)) :
        if q[j][0] == location :
            return j+1

    return answer