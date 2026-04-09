from collections import deque
def solution(begin, target, words):
    answer = 0
    N = len(words)
    visited = [False] * N
    
    def canDiff(word1, word2) :
        n= 0
        for i in range(len(word1)) :
            if word1[i] != word2[i] :
                n+=1
        if n == 1 :
            return True
        else :
            return False
    
    q = deque()
    q.append((begin, 0))
    
    while q :
        word, cnt = q.popleft()
        
        if word == target :
            return cnt
        
        for i in range(len(words)) :
            if canDiff(words[i], word) and not visited[i] :
                q.append((words[i],cnt+1))
                visited[i] = True
    
    
    return 0