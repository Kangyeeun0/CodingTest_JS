function solution(n)
{
    let ans= 0;
    var cp = n;
   
    while(true){
        if(cp%2===0){
            cp=cp/2;
        } else {
            cp--;
            ans++;
        }
    
        if(cp===0){
            break;
        }
    }

    return ans;
}