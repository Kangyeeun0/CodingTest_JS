def solution(people, limit):
    people.sort()
    
    print(people)
    
    left = 0
    right = len(people) - 1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 같이 탐
        right -= 1    # 무거운 사람은 항상 탐
        answer += 1
    
    return answer