#include <iostream>
using namespace std;

class Test
{
    int length, width, area;

public:
    void input()
    {
        cout << "Enter length of rectangle: ";
        cin >> length;
        cout << "Enter width of rectangle: ";
        cin >> width;
    }
    void findArea()
    {
        area = length * width;
    }
    void display()
    {
        cout << "Area of rectangle is: " << area;
    }
};

int main()
{
    Test x;

    x.input();
    x.findArea();
    x.display();

    return 0;
}
