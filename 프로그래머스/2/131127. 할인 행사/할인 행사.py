from collections import Counter

def solution(want, number, discount):
    answer = 0
    n = len(discount)
    
    want_dict = { want[i] : number[i] for i in range(len(want)) }
    
    for i in range(len(discount)-9) :
        window = discount [i:i+10]
        window_count = Counter(window)
        
        ok = True
        for item, cnt in want_dict.items() :
            if window_count.get(item, 0) < cnt :
                ok = False
                break
                
        if ok :
            answer+=1
                
    
    
    return answer