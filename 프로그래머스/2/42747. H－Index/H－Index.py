def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    # print(citations)
    answer = 0
    
    for i in range(n) :
        if citations[i] > i :
            answer+=1
        
    
    
    
    return answer