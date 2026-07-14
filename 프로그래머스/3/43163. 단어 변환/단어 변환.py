# 너비우선탐색인 거 같음
def solution(begin, target, words):
    answer = len(words)
    isSame = [False] * len(words)
    
    if target not in words :
        return 0
    
    def cntDiff(word1, word2) :
        cnt = 0
        for i in range(len(word1)) :
            if word1[i] != word2[i] :
                cnt+=1
        if cnt == 1:
            return True
        else :
            return False
        
    def bfs(word, count) :
        nonlocal answer
        
        
        if word == target :
            answer = min(answer, count)
            return answer
        
        for i in range(len(words)) :
            if not isSame[i] and cntDiff(word, words[i]) :
                isSame[i] = True
                bfs(words[i], count+1)
                isSame[i] = False
                
            
        
        
    for i in range(len(words)) :
        if cntDiff(begin, words[i]) :
            isSame[i] = True
            bfs(words[i], 1)
            isSame[i] = False
    
    return answer