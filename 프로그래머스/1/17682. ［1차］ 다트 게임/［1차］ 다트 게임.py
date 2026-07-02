def solution(dartResult):
    answer = 0
    arr = []
    num = ""
    
    for result in dartResult :
        if result in ['*', '#'] :
            if result == '*' :
                if arr :
                    arr[-1] = arr[-1] * 2
                if len(arr) > 1 :
                    arr[-2] = arr[-2] * 2
            elif result == '#' :
                arr[-1] = -arr[-1]
            
        elif result in ['S', 'D', 'T'] :
            num = int(num)
            if result == 'S' :
                arr.append(num)
            elif result == 'D' :
                arr.append(num**2)
            elif result == 'T' :
                arr.append(num**3)
            num = ""
        else :
            num += result
    
    # print(arr)
        
    return sum(arr)