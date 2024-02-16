const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Who are you?", (name) => {
  console.log(`Hey there ${name}!`);
  readline.close();
});

// const a = prompt();
// const b = prompt();
// const c = prompt();

// console.log(a && b && c && a + b + c === 180 ? "Yes" : "No");
