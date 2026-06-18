def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) -1
    
    while left <= right :
        tube = people[right]
        right -=1
        
        if tube+people[left] <= limit :
            tube += people[left]
            left+=1
            
        answer+=1
            
    
    
    return answer





