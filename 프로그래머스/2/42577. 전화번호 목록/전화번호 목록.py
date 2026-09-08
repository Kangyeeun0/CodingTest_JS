from collections import deque
def solution(phone_book):
    answer = True
    books = deque(sorted(phone_book))
                  
    # print(phone_book)
    
    while books :
        target = books.popleft()
        
        for i in range(len(books)) :
            if target == books[i][0:len(target)] :
                return False
            else :
                break
        
        
    
            
    return answer