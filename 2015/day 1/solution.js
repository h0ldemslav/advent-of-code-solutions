const { readInput } = require("../../utils");

const data = readInput("./2015/day 1/input.txt");
const FLOOR_UP = "(";
const FLOOR_DOWN = ")";
const BASEMENT = -1;
let floorNumber = 0;
let charPosition = null;

for (let i = 0; i < data.length; i++) {
    if (data[i] === FLOOR_UP) {
        floorNumber += 1;
    } else if (data[i] === FLOOR_DOWN) {
        floorNumber -= 1;

        if (floorNumber === BASEMENT && !charPosition) {
            charPosition = i + 1;
        }
    }
}

console.log(floorNumber);
console.log(charPosition);
