## 개어려움
def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    def find(x) :
        if parent[x] != x :
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b) :
        a = find(a)
        b = find(b)
        
        if a<b :
            parent[b] = a
        else :
            parent[a] = b
    
    costs.sort(key=lambda x: x[2])
    
    answer = 0
    
    for a, b, cost in costs :
        if find(a) != find(b) :
            union(a,b)
            answer+= cost
        
        
        
    return answer