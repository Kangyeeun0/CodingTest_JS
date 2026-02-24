def solution(word):
    answer = 0
    arr =[]
    
    
    for a in ['A', 'E', 'I', 'O', 'U'] :
        arr.append(a)
        for b in ['A', 'E', 'I', 'O', 'U'] :
            arr.append(a+b)
            for c in ['A', 'E', 'I', 'O', 'U'] :
                arr.append(a+b+c)
                for d in ['A', 'E', 'I', 'O', 'U'] :
                    arr.append(a+b+c+d)
                    for e in ['A', 'E', 'I', 'O', 'U'] :
                        arr.append(a+b+c+d+e)
                        
                        
    
    
    return arr.index(word) + 1