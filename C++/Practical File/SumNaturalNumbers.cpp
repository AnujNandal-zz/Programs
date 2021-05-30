#include <iostream>
using namespace std;
int main()
{
    int n = 1;
    int sum = 0;

    cout << "The Sum of First 10 Natural Numbers\n";
    cout << "-----------------------------------\n";

    while (n < 11)
    {
        sum = sum + n;
        n += 1;
    }

    cout << "\nThe sum of first 10 natural numbers is: " << sum;

    return 0;
}
