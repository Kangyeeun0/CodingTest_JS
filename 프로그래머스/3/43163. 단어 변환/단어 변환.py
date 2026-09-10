from collections import deque
def diffCount(word1,word2) :
    cnt = 0
    for i in range(len(word1)) :
        if word1[i] != word2[i] :
            cnt +=1
        if cnt > 1 :
            return False
    
    if cnt == 1:
        return True
    else :
        return False    

def solution(begin, target, words):
    answer = 0
    q = deque()
    visited = [False] * len(words)
    
    if target not in words :
        return 0
    
    q.append((begin, 0))
    
    while q :
        word, cnt = q.popleft()
        
        if word == target :
            return cnt
        
        for i in range(len(words)) :
            if not visited[i] :
                if diffCount(word, words[i]) :
                    q.append((words[i], cnt+1))
            
        
    
    
    
    
    return answer