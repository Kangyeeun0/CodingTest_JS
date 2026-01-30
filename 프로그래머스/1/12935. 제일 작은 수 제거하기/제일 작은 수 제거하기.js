function solution(arr) {
    var answer = [];
    const min=Math.min(...arr);
    console.log(min);
    return arr.filter(x=>x!==min);
}