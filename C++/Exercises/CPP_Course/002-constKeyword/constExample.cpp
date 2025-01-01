#include <iostream>

int main () {
    
    // Circumference Example
    const double PI = 3.14159;
    const double RADIUS = 10;
    double circumference = 2 * PI * RADIUS;

    std::cout << "Circumference: " << circumference << " cm" << std::endl;
    
    // Physics Calculation
    const int LIGHT_SPEED = 299792458; // meters/second
    const int WIDTH = 1920;
    const int HEIGHT = 1080;

    std::cout << "Light Speed: " << LIGHT_SPEED << " m/s" << std::endl;
    std::cout << "Screen Resolution: " << WIDTH << "x" << HEIGHT << std::endl;

    return 0;
}