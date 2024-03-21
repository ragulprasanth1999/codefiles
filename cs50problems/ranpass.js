function newpass(passwordlength, includeupper, includelower, includesymbol) {
    const lowercase = "abcdefghijklmnopqrstuvwxyz";
    const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const num = "12344567890";
    const symbol = "!@#$%^&*()_+";

    let charset = lowercase;
    if (includeupper) charset += uppercase;
    if (includelower) charset += num;
    if (includesymbol) charset += symbol;

    let password = "";
    for (let i = 0; i < passwordlength; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }

    return password;
}

const passwordlength = 12;
const includeupper = true;
const includelower = true;
const includesymbol = true;

let password = newpass(passwordlength, includeupper, includelower, includesymbol);
console.log("Generated password:", password);
