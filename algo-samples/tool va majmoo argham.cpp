#include <iostream>
#include <math.h>

using namespace std;

int dig_sum(int n)
{
    if (n == 0)
        return 0;
    else
        return n % 10 + dig_sum(int(n / 10));
}

int main()
{
    int m, s, n, max = -1, min = -1;
    cin >> m >> s;
    n = pow(10, m - 1);
    while (n < pow(10, m))
    {
        if (dig_sum(n) == s)
        {
            if (min == -1 && max++ - 1)
            {
                min = n;
                max = n;
            }
            else
                max = n;
        }
        n++;
    }
    cout << min << " " << max << endl;
    return 0;
}