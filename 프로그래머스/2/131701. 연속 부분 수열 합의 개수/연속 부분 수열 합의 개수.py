def solution(elements):
    answer = 0
    n = len(elements)
    twoElements = elements * 2
    arr = []
    
    # print(twoElements)
    
    for i in range(n) :
        total = 0
        for j in range(i, n+i) :
            total += twoElements[j] 
            arr.append(total)
        
    setArr = set(arr)
    # print(setArr)
    return len(setArr)