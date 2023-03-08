function superDigit(n, k) {
    const sum = n
        .split('')
        .reduce((acc, digit) => acc + Number(digit), 0) * k;
    console.log(sum);
    let superDigit = sum;
    while (superDigit >= 10) {
        superDigit = superDigit
            .toString()
            .split('')
            .reduce((acc, digit) => acc + Number(digit), 0);
    }
    
    return superDigit;
}

console.log(superDigit('1', 3))