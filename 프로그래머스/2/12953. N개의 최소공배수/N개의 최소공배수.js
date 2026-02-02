function solution(arr) {
    var answer = 0;
    
    function gcd(a,b) {
        while(b!== 0) {
            let r = a%b;
            a=b;
            b=r;
        }
        return a;
    }
    
    function lcm(a,b){
        var target = (a*b) / gcd(a,b);
        return target;
    }
    
    var first = arr[0];
    for(var i=1;i<arr.length;i++){
        answer=lcm(first, arr[i]);
        first=answer;
}
   

    return answer;
}