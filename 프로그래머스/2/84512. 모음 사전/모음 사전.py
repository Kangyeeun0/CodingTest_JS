## 다시 풀어보기
def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def generate(w) :
        nonlocal answer
        
        if w == word :
            return True
        
        if w != "" :
            answer+=1
        
        if len(w) <5 :
            for i in range(len(vowels)) :
                if generate(w+vowels[i]) :
                    return True
        return False
                
        
        
    generate("")
    
    return answer + 1