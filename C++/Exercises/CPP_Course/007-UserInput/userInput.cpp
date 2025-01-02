#include <iostream>
#include <string>

// cout << (Insertion Operator)
    // Character Output
// cin >> (Extraction Operator)
    // Character Input

int UserInput() {
    std::string name;
    int age;

    std::cout << "What's your age?: ";
    std::cin >> age;

    std::cout << "What's your full name?: ";
    std::getline(std::cin >> std::ws, name);
    //TODO EXPLAIN WHY `getline` IS USED HERE


    std::cout << "Hello " << name << "!" << std::endl;
    std::cout << "You're " << age << " years old!";

    return 0;
}

int main() {
    UserInput();

    return 0;
}