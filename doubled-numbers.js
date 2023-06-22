// 与えられたリストの要素を2倍にして新しいリストを作成するプログラム
var numbers = [1, 2, 3, 4, 5];
var doubledNumbers = [];

for (var i = 0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i] * 2);
}

console.log(doubledNumbers);