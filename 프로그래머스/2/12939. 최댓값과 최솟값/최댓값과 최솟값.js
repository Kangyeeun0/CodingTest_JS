function solution(s) {
    var answer = s.split(" ");
    const maxValue = Math.max(...answer);
    const minValue = Math.min(...answer);
    return String(minValue)+" "+ String(maxValue);
}