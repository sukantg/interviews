// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

const isPallindrome = x => {
    if (x<0) return false;

    let reversed = 0, lastDigit = 0, y=x;
    
    while (y!==0) {
        lastDigit = (y%10);
        reversed = (reversed * 10) + lastDigit;
        // Update the number by removing the last digit with Bitwise OR
        y = (y/10) | 0; 
        // Alternate way: y = parseInt(y/10);
    }

    return x===reversed;
}

console.log(isPallindrome(272272));