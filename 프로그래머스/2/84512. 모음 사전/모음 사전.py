def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    found = False
    
    
    def dfs(w) :
        nonlocal answer, found
        answer+=1
        
        if w == word :
            found = True
            return answer
        elif len(w) == len(words) :
            return
        
        for i in range(len(words)) :
            dfs(w+words[i])
    
            if found :
                break
        return
            
            
    for i in range(len(words)) :
        dfs(words[i])
        if found :
            break
        
            
    
    
    return answer