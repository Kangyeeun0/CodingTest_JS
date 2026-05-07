def solution(s, skip, index):
    answer = ''
    # a => 97, z => 122
    skip_arr = [ord(skip[i]) for i in range(len(skip))]
    skip_arr.sort()
    # print(skip_arr)
   
    for i in range(len(s)) :
        text = ord(s[i])
        j = 0
        while j < index :
            text += 1
            if text > 122 :
                text = 97
            if not text in skip_arr :
                j+=1
            
        
        if text > 122 :
            text = text - 122 + 97 - 1
        answer+=chr(text)
        
    return answer