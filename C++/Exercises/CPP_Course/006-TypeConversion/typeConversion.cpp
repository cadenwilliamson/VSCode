#include <iostream>

int Implicit() {
    int x = 3.14;
    std::cout << x << std::endl;

    return 0;
}

int Explicit() {
    double x = (int) 3.14;
    std::cout << x << std::endl;

    return 0;
}

int ImplicitExample() {
    char x = 100;

    std::cout << x << std::endl;

    return 0;
}

int ExplicitExample() {
    std::cout << (char) 65 << std::endl;

    return 0;
}

int UsefulExplicitExample() {
    int correct = 8;
    int questions = 10;

    double score = correct / (double)questions * 100;

    std::cout << score << "%" << std::endl;

    return 0;
}


int main() {
    Implicit();
    Explicit();
    ImplicitExample();
    ExplicitExample();
    UsefulExplicitExample();

    return 0;
}