#include <iostream>


int Addition() {
    // Addition (+)
    int studentsADD = 20;
    studentsADD = studentsADD + 1;
    studentsADD += 1;
    studentsADD++;

    std::cout << "Addition: " << studentsADD << std::endl;
    return 0;
}

int Subtraction() {
    // Subtraction (-)
    int studentsSUB = 20;
    studentsSUB = studentsSUB - 1;
    studentsSUB -= 1;
    studentsSUB--;

    std::cout << "Subtraction: " << studentsSUB << std::endl;

    return 0;
}

int Multiplication() {
    // Multiplication (*)
    int studentsMULT = 20;
    studentsMULT = studentsMULT * 2;
    studentsMULT*=2;
    // studentsMULT**; (This does not work for Multiplication)

    std::cout << "Multiplication: " << studentsMULT << std::endl;

    return 0;
}

int Division() {
    // Division (/)
    int studentsDIV = 20;
    studentsDIV = studentsDIV / 2;
    studentsDIV/=2;
    // studentsDIV//; (This does not work for Division)

    std::cout << "Division: " << studentsDIV << std::endl;

    return 0;
}

int Modulus() {
    // Modulus (%) - Good to find if number is even or odd.
    // Gives remainder of any division.
    int students = 20;
    int remainder = students % 3;
    
    std::cout << "Students: " << students << std::endl;
    std::cout << "Modulus: " << remainder << std::endl;

    return 0;
}

int LongEquation() {
    // Long Equation Example
    int longEquation = 6 - 5 + 4 * 3 / 2;
    int separateStepsEq = 6 - ((5 + 4) * 3) / 2;

    std::cout << "Long Equation: " << longEquation << std::endl;
    std::cout << "Separate Steps: " << separateStepsEq << std::endl;

    return 0;
}

int main() {
    Addition();
    Subtraction();
    Multiplication();
    Division();
    Modulus();
    LongEquation();

    return 0;
}