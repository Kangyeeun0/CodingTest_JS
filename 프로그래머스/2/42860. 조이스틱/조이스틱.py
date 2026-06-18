def solution(name):
    answer = 0
    n = len(name)
    
    #세로 이동
    for c in name:
        answer += min(ord(c)-ord("A"), ord('Z')- ord(c)+1)
        
    # 가로 이동
    move = n-1
    
    for i in range(n) :
        next_idx = i+1
        
        while next_idx < n and name[next_idx] == "A" :
            next_idx += 1
        
        move = min(move, i*2+(n-next_idx), (n-next_idx) * 2 + i)
                
    
    
    return answer + move