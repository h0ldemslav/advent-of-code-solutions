const { performance } = require("perf_hooks");
const { readInput } = require("../../utils");
const crypto = require('crypto')

const data = readInput("./2015/day 4/input.txt");

let startNumber = 0;
let hashFound = false;
let hash;

const start = performance.now();

while (!hashFound) {
    hash = crypto.createHash('md5').update(data + startNumber.toString()).digest("hex");
    if (hash.startsWith("000000")) {
        hashFound = true;
    } else {
        startNumber++;
    }
}

console.log("num", startNumber);
console.log("hash", hash);
console.log("time in s", (performance.now() - start) / 1000);
