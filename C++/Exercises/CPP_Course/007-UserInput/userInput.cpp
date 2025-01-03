#include <iostream>
#include <string>

// cout << (Insertion Operator)
    // Character Output
// cin >> (Extraction Operator)
    // Character Input


// int UserInputBAD() {
//     std::string name;

//     std::cout << "What's your name?: "
//     std::cin >> name;

//     std::cout << "Hello " << name << "!\n";

//     return 0;
// }

// int UserInputOK() {
//     std::string name;

//     std::cout << "What's your name?: ";
//     std::getline(std::cin >> std::ws, name);

//     std::cout << "Hello " << name << "!\n";

//     return 0;
// }

// int UserInputBETTER() {
//     std::string name = "Bob Bob";
//     int age = 24;


//     std::cout << "What's your age?: ";
//     std::cin >> age;

//     std::cout << "What's your name?: ";
//     std::getline(std::cin, name);

//     std::cout << "Hello " << name << "!\n";
//     std::cout << "You're " << age << " years old!\n";

//     return 0;
// }

int UserInputFULL() {
    std::string name;
    int age;

    std::cout << "What's your age?: ";
    std::cin >> age;

    std::cout << "What's your full name?: ";
    std::getline(std::cin >> std::ws, name);

    std::cout << "\nHello " << name << "!\n";
    std::cout << "You're " << age << " years old!\n";

    return 0;
}


int main() {
    // UserInputBAD();
    // UserInputOK();
    // UserInputBETTER();
    UserInputFULL();

    return 0;
}