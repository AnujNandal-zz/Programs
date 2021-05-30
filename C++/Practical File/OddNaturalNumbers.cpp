#include <iostream>
using namespace std;
int main()
{
    int n = 1, c = 0;
    cout << "First 10 Odd Natural Numbers\n";
    cout << "----------------------------\n";
    while (c < 10)
    {
        do
        {
            cout << n << "\n";
            n += 2;
            c += 1;
        } while (n < 19);
    }

    return 0;
}