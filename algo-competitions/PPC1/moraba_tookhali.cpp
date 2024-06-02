#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    if (b >= a)
        cout << "Wrong order!";
    else if ((a - b) % 2)
        cout << "Wrong difference!";
    else
    {
        int edge = (a - b) / 2;
        for (int row = 0; row < a; row++)
        {
            for (int j = 0; j < edge; j++)
                cout << "* ";
            for (int j = 0; j < b; j++)
            {
                if (row < edge or row >= edge + b)
                    cout << "* ";
                else
                    cout << "  ";
            }
            for (int j = 0; j < edge; j++)
                cout << "* ";
            cout << "\n";
        }
    }
}