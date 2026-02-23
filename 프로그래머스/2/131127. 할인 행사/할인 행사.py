def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9) :
        window = discount[i:i+10]
        
        ok = True
        for j in range(len(want)) :
            if window.count(want[j]) != number[j] :
                ok = False
                break
        if ok :
            answer+=1
    
    
    return answer