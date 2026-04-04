def solution(word):
    answer = 0
    m=['A', 'E', 'I', 'O', 'U']
    words = []
    
    def generate(current) :
        if current :
            words.append(current)
            
        if len(current) < 5:
            for vowel in m :
                generate(current+vowel)
    
    generate("")
    # print(words)
    
    return words.index(word) + 1
        
        
        
    
    
    return answer