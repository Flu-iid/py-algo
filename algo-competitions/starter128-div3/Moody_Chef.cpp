#include <iostream>
using namespace std;

int main()
{
    int t, n, l, r;
    cin >> t;
    for (; t > 0; t--)
    {
        int min = 0, max = 0, happiness = 0, tmp;
        cin >> n >> l >> r;
        for (int i = 0; i < n; i++)
        {
            cin >> tmp;
            if (l <= tmp and tmp <= r)
                happiness += 1;
            else
                happiness -= 1;

            if (happiness > max)
                max = happiness;
            if (happiness < min)
                min = happiness;
        }
        cout << max << " " << min << "\n";
    }
}