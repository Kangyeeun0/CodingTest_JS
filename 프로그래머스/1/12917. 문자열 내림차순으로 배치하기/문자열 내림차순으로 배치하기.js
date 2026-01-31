function solution(s) {
    var answer = [...s];
    answer.sort((a,b)=> {
        if(a>b) return -1;
        else if(a<=b) return 1;
    })
    return answer.join("");
}