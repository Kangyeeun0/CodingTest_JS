import math
def solution(r1, r2):
    answer = 0
    #x^2 +y^2 = r^2
    
    for x in range(1, r2+1) :
        y2 = int(math.sqrt(r2*r2 - x*x))
        #print(y2)#
        
        if x < r1:
            y1 = math.ceil(math.sqrt(r1 * r1 - x * x))

            answer += y2 - y1 + 1
        else :

            answer+=(y2+1)
            
    answer*=4
    
    
    return answer