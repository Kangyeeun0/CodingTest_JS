def solution(word):
    answer = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    words= []
    
    def generate(w) :
        if len(w) > 5  :
            return 
        if w:
            words.append(w)
            
        for v in vowel :
            generate(w+v)
        
    generate("") 

    return words.index(word) + 1