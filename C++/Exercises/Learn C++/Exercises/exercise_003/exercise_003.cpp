#include <iostream>
#include <iomanip>
using namespace std;

int items = 50;
double costPerItem = 9.99;
float totalCost = items * costPerItem;
char USD = '$';

int main() {
    cout << fixed << setprecision(2);
    cout << "Number of items: " << items << endl;
    cout << "Cost Per Item: " << costPerItem << endl;
    cout << "Total Cost: " << USD << totalCost << endl;
    return 0;
}