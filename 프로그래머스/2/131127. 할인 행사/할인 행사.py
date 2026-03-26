def solution(want, number, discount):
    answer = 0
    n= len(want)
    d = {}
    for i in range(n) :
        d[want[i]] = number[i]
    
    for j in range(len(discount)-10+1) :
        d2 = {}
        for k in range(j, j+10) :
            if discount[k] in want :
                d2[discount[k]] = d2.get(discount[k], 0) + 1
    
        if d == d2 :
            answer+=1         
    
    return answer