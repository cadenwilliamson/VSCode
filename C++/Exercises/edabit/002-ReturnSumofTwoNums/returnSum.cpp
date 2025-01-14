#include <iostream>

int addition(int a, int b) {
    int sum = a + b;

    std::cout << a << " + " << b << " = " << sum << "\n";

    return 0;
}

int main() {
    addition(3, 2);
    addition(-3, -6);
    addition(7, 3);

    return 0;
}