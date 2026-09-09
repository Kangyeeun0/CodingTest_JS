def solution(sizes):
    answer = 0
    one = []
    two = []
    
    for size in sizes :
        size.sort()
        one.append(size[0])
        two.append(size[1])
        
    
    return max(one)*max(two)