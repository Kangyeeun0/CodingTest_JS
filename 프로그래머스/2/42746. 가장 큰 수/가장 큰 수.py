def solution(numbers):
    answer = ''
    arr = []
    for n in numbers :
        arr.append(str(n))
        
    arr.sort(key = lambda x:x*3, reverse=True)
    
    if arr[0] == '0' :
        return '0'
        
        
    return "".join(arr)