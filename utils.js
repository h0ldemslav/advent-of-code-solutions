const fs = require("node:fs");

/**
 * Wrapper for Node.js `readFileSync`.
 *
 * @param {string} path
 * @param {string} [encoding="utf-8"]
 * @param {boolean} [trim=true]
 * @returns
 */
function readInput(path, encoding = "utf-8", trim = true) {
    try {
        const data = fs.readFileSync(path, encoding);
        return trim ? data.trim() : data;
    } catch (err) {
        console.error(err);
    }
}

exports.readInput = readInput;
