def solution(nums):
    answer = 0
    N = len(nums)
    n = N // 2
    dic = dict()
    
    for num in nums :
        dic[num] = dic.get(num, 0) + 1
    
    if n <= len(dic) :
        return n
    else :
        return len(dic)
        
    return answer