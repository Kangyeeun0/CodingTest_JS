def solution(s):
    answer = True
    pNum=0
    yNum=0
    
    for i in s :
        if(i=='p' or i=='P') :
            pNum+=1
        elif(i=='y' or i=='Y') :
            yNum+=1
        
    print(pNum, yNum)
    
    if(pNum==yNum) :
        return True
    else :
        return False
        

    return True