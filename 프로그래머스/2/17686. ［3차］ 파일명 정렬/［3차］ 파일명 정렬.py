def solution(files):
    arr = []
    answer = []
    
    def split_filename(filename) :
        head = ""
        number = ""
        tail = ""
        
        i = 0
        while i < len(filename) and not filename[i].isdigit() :
            head += filename[i]
            i+=1
        
        while i < len(filename) and filename[i].isdigit() :
            number += filename[i]
            i+=1
        
        tail = filename[i:]
        
        return head, number, tail
        
    for file in files :
        head, number, tail = split_filename(file)
        arr.append([head, number, tail])
    
    arr.sort(key = lambda x:(x[0].upper(),int(x[1])))
    
    for a in arr :
        answer.append(a[0]+a[1]+a[2])
    return answer