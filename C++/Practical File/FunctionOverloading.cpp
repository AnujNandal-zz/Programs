#include <iostream>
using namespace std;

int CalcArea(int);
int CalcArea(int, int);
int CalcArea(float, float, float);
int main()
{
    cout << "Program to show the concept of Function Overloading\n";
    cout << "---------------------------------------------------\n";

    cout << CalcArea(12) << "\n";
    cout << CalcArea(20, 15) << "\n";
    cout << CalcArea(8, 10, 11) << "\n";

    return 0;
}
int CalcArea(int s)
{
    return (s * s);
}
int CalcArea(int l, int b)
{
    return (l * b);
}
int CalcArea(float a, float b, float h)
{
    return ((a + b) / 2 * h);
}
