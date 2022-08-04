let y = [6,8,1,9,2,7,3,4,5]
console.log(y.sort())

const  quicksort=(array) =>{
let pivot = array[4];
let left =[];
let right = [];
for (let i = 0; i < array.length; i++){
    array[i] < pivot ? left.push([i]) : right.push([i]);
}
return quicksort(left).concat(pivot, quicksort(right));
};

console.log(quicksort(y))