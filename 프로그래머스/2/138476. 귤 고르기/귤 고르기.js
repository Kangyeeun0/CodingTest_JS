function solution(k, tangerine) {
   
    var counts = tangerine.reduce((pv,cv)=>{
            pv[cv] = (pv[cv] || 0) + 1;
            return pv;
        }, {});
        
    const arrCount = Object.values(counts).sort((a,b) => b-a);
    
    let sum=0;
    let answer=0;
    
    for(let cnt of arrCount) {
        sum+=cnt;
        answer++;
        if(sum>=k) break;
    }
        
    
   
    return answer;
}