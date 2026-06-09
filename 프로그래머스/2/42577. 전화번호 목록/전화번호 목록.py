def solution(phone_book):
    answer = True
    phone_book.sort()
    # print(phone_book)
    
    for i in range(len(phone_book)-1) :
        phone = phone_book[i]
    
        if phone == phone_book[i+1][0:len(phone)] :
            return False
            
    return answer