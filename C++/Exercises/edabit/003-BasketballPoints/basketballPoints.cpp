#include <iostream>

int square(int a) {
    std::cout << a * a << std::endl;
    return 0;
}

int main() {
    square(8);
    square(12);
    square(534);
    square(39);
    return 0;
}