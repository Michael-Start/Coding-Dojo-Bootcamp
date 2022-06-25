function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for ( var i = 2; i < n; i++){
        fibArr[i] = fibArr[i - 1] + fibArr[i - 2];
        fibArr.push(i);
        if(i == n-1){
            fibArr.pop()
        }
    }
    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
