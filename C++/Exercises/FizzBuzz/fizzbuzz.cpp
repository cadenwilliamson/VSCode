#include <iostream>

// Initializes function FizzBuzz
int FizzBuzz() {
    using std::cout;
    using std::endl;
    
    // Create 'for' loop to iterate through 100 numbers.
    for(int num = 1; num <= 100; ++num) {
        
        // If number is divisable by 3 and 5:
        if (num % 3 == 0 && num % 5 == 0) {
            cout << "Fizzbuzz: " << num << endl;
        }
        
        // If number is divisable by 3:
        else if (num % 3 == 0) {
            cout << "Fizz: " << num << endl;
        }
        
        // If number is divisable by 5:
        else if (num % 5 == 0) {
            cout << "Buzz: " << num << endl;
        }
        
        // If nothing else:
        else {
            cout << num << endl;
        }
    }

    return 0;
}

// Main function that runs FizzBuzz function.
int main() {
    FizzBuzz();

    return 0;
}