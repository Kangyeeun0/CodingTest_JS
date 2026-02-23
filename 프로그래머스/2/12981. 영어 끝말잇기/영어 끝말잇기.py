def solution(n, words):
    answer = []
    arr = [words[0]]
    num = 1
    r = 1 
    
    for i in range (1, len(words)) :
        if words[i] not in arr and words[i][0] == words[i-1][len(words[i-1])-1] :
            arr.append(words[i])
            # print(arr)
        elif (words[i] in arr or words[i][0] != words[i-1][len(words[i-1])-1]):
            num = (i%n) + 1
            r = i // n + 1
            answer.append(num)
            answer.append(r)
            return answer
        
    return [0,0]
        
        
   