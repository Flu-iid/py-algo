function isQInteger([a, b, r]) {
  const invalidNumbers =
    a < 0 || a > 100 || b < 1 || b > 100 || r < 0 || r > 100;
  if (invalidNumbers) throw new Error("Invalid numbers!");
  const q = (a - r) / b;
  if (Number.isInteger(q)) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}

function analyzeInput(...inputArrays) {
  inputArrays.forEach((arr) => isQInteger(arr));
}
