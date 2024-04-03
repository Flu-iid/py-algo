#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (; t > 0; t--)
    {
        int x;
        cin >> x;
        int b = x;
        int mxor = x ^ b;
        int mand = x & b;
        for (; (mxor % x) or (mand % x) or mxor <= 0 or mand <= 0;)
        {
            b += x;
            mxor = x ^ b;
            mand = x & b;
        }
        cout << x << " " << b << "\n";
    }
}