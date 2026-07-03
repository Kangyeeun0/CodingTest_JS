def solution(numbers, hand):
    answer = ''
    now_left = (3,0)
    now_right = (3,2)
    
    position = {
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    9: (2,2),
    0: (3,1)
}
    
    for number in numbers : 
        if number in [1,4,7] :
            answer+='L'
            now_left = position[number]
            
        elif number in [3,6,9] :
            answer += 'R'
            now_right = position[number]
            
        elif number in [2,5,8,0] :
            po = position[number]
            left_po = abs(now_left[0]-po[0]) + abs(now_left[1]-po[1])
            right_po = abs(now_right[0]-po[0]) + abs(now_right[1]-po[1])
            
            if left_po < right_po :
                answer+='L'
                now_left = po
            elif left_po > right_po :
                answer+= 'R'
                now_right = po
            else :
                if hand == 'right' :
                    answer+='R'
                    now_right = po
                else :
                    answer +='L'
                    now_left = po
               

            
            
        
    return answer