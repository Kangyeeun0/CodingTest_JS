def solution(s):
    answer = 0
    min_length = len(s)
    mid = len(s) // 2
    
    for unit in range(1, mid + 1) :
        compressed = ""
        prev = s[0:unit]
        cnt = 1
        
        for i in range(unit, len(s), unit) :
            curr = s[i:i+unit]
            if prev == curr :
                cnt += 1
            else :
                if cnt > 1 :
                    compressed += str(cnt) + prev
                else :
                    compressed += prev
                prev = curr 
                cnt = 1
        
        if cnt > 1 :
            compressed += str(cnt) + prev
        else :
            compressed += curr
        # print(compressed,curr)
        min_length = min(min_length, len(compressed))
                
    return min_length