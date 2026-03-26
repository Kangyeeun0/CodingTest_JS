def solution(n, words):
    answer = []
    length=len(words)
    prior = words[0]
    number = 1
    wordList = []
    wordList.append(prior)
    
    for i in range(1, length) :
        if prior[-1] == words[i][0] and words[i] not in wordList :
            wordList.append(words[i])
            number+=1
            prior = words[i]
        elif prior[-1] != words[i][0] or words[i] in wordList :
            # number+=1
            break
            
    if number == len(words) :
        return [0,0]
    number += 1
    if number % n == 0 :
        return [n, number//n]
    else :
        return [number%n, number //n + 1]
    return answer