from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize <1 :
        return 5*len(cities)
    
    for i in range(len(cities)) :
        city = cities[i].upper()
        if city in cache :
                cache.remove(city)
                cache.append(city)
                answer+=1
        else :
            if len(cache) < cacheSize :
                cache.append(city)
                answer+=5
            
            else :
                cache.popleft()
                cache.append(city)
                answer+=5
                    

    return answer