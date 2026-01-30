function solution(phone_number) {
    var n=phone_number.length;
    var answer = phone_number.slice(n-4,n);
    var str='';
    for(let i=0;i<n-4;i++){
        str+="*"
    }
    return str+answer; 
}