def solution(nums):
    answer = 0
    dic = dict()
    
    for n in nums :
        dic[n] = dic.get(n, 0) + 1
    
    for item in dic.items() :
        answer+=1
        
    if answer > len(nums)//2 :
        return len(nums)//2
    else :
        return answer
    return answer