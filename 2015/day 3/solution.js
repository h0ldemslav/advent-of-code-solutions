const { readInput } = require("../../utils");

const data = readInput("./2015/day 3/input.txt");
let housesCount = 1;

// let x = 0;
// let y = 0;
// let x1 = 0, y1 = 0;

const coord1 = { x: 0, y: 0, };
const coord2 = { x: 0, y: 0, };
const visited = new Set();
visited.add(`${0}${0}`);

for (let i = 0; i < data.length; i++) {
    const coord = i % 2 === 0 ? coord1 : coord2;

    switch (data[i]) {
        case ">":
            coord.x++;
            break;
        case "<":
            coord.x--;
            break;
        case "^":
            coord.y++;
            break;
        case "v":
            coord.y--;
            break;
        default:
            throw new Error("Invalid symbol");
    }

    const xy = `${coord.x}${coord.y}`;

    if (!visited.has(xy)) {
        housesCount++;
        visited.add(xy);
    }
}

console.log(housesCount);
