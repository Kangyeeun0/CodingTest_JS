def solution(nums):
    answer = 0
    cnt = len(nums) / 2
    dic = {}
    
    for num in nums :
        dic[num] = dic.get(num, 0) + 1
        
    if cnt <= len(dic) :
        return cnt
    else :
        return len(dic)
        
    
    
    return answer