const { readInput } = require("../../utils");

const data = readInput("./2015/day 2/input.txt");
const list = data.split("\r\n");
let total = 0;
let totalRibbon = 0;

for (let i = 0; i < list.length; i++) {
    let [l, w, h] = list[i].split("x");
    l = Number(l);
    w = Number(w);
    h = Number(h);

    const surfaceArea = 2 * l * w + 2 * w * h + 2 * h * l;
    const smallestSideArea = Math.min(l * w, w * h, h * l);
    total += surfaceArea + smallestSideArea;

    const [minDim1, minDim2] = [l, w, h].sort((a, b) => a - b);
    totalRibbon += minDim1 + minDim1 + minDim2 + minDim2 + l * w * h;
}

console.log(total);
console.log(totalRibbon);
