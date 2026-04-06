from collections import deque
def solution(begin, target, words):
    answer = 0   
    
    if target not in words :
        return 0

    # 한 글자만 다른지 체크하는 함수 :
    def can_convert(word1, word2) :
        diff_count = 0
        for i in range(len(word1)) :
            if word1[i] != word2[i] :
                diff_count+=1
        if diff_count == 1:
            return 1
        else :
            return 0
    
    #BFS
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue :
     
        current_word, count = queue.popleft()
        
        if current_word == target :
            return count
        
        for word in words :
            if word not in visited and can_convert(current_word, word) :
                visited.add(word)
                queue.append((word, count+1))
                
    return 0
    
