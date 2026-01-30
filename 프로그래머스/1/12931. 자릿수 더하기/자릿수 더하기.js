function solution(n)
{
    var answer = 0;
    const arr =n.toString().split("");
   answer= arr.reduce((acc,cur)=>acc+Number(cur),0);

    return answer;
}