def solution(triangle):
    answer = 0
    
    for i in range(len(triangle)-2,-1, -1) :
        tri = triangle[i]
        for j in range(len(tri)) :
            tri[j]=max(tri[j]+triangle[i+1][j], tri[j]+triangle[i+1][j+1])
            
    # print(triangle)
    
    return triangle[0][0]