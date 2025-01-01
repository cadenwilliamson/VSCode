#include <iostream>

namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}


int main() {
    using std::cout;
    using std::endl;

    int x = 0;
    
    cout << "Local X Value: " << x << endl;
    cout << "First X Value: " << first::x << endl;
    cout << "Second X Value: " << second::x << endl;


    return 0;
}