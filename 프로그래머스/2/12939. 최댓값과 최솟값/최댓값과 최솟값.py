def solution(s):
    answer = ''
    a= s.split(" ")
    arr = []
    for s in a:
        arr.append(int(s))
    arr.sort()
    answer = str(arr[0]) + " " + str(arr[len(arr)-1])
    return answer