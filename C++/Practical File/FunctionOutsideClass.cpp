#include <iostream>
using namespace std;
class rect
{
    int l, b;

public:
    int rectarea(int, int);
};
int main()
{
    cout << "Program to calculate area of rectange with member function outside class\n";
    cout << "------------------------------------------------------------------------\n";

    rect x;
    cout << "Area of Rectangle = " << x.rectarea(12, 10);
}
int rect::rectarea(int l, int b)
{
    return (l * b);
}
