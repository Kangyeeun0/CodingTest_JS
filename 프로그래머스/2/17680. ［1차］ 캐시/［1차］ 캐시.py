from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    # if len(cities) <= cacheSize :
    #     return 5 * len(cities)
    if cacheSize == 0 :
        return len(cities) * 5
    
    for i in range(len(cities)) :
        if cities[i].lower() in cache:
            cache.remove(cities[i].lower())
            answer+=1
            cache.append(cities[i].lower())
        else :
            if len(cache) < cacheSize :
                    answer+=5
                    
            else :
                answer+=5
                cache.popleft()
            cache.append(cities[i].lower())
                
        
            
    
    return answer