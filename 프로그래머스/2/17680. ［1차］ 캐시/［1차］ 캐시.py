from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    
    if cacheSize == 0 :
        return 5*len(cities)
    

    for j in range(0, len(cities)) :
        city = cities[j].upper()
        if city in queue :
            queue.remove(city)
            answer+=1
            queue.append(city)

        else :
            if len(queue)>=cacheSize :
                queue.popleft()
            queue.append(city)
            answer+=5
                
    return answer