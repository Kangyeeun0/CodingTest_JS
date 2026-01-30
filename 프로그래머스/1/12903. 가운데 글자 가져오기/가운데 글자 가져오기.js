function solution(s) {
    var answer = '';
    
    if(s.length%2) return s[Math.floor(s.length/2)];
    if(s.length%2===0) return s.slice(s.length/2-1,s.length/2+1);
    return answer;
}