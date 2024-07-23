#include <iostream>
using namespace std;

void bubble_sort(int n, int a[])
{
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n; i++)
        {
            if (i == n - 1)
                continue;
            if (a[i] > a[i + 1])
            {
                int tmp;
                tmp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = tmp;
            }
        }
    }
}

int main()
{
    int t, n;
    cin >> t;
    for (; t > 0; t--)
    {
        int tmp, count = 0;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        bubble_sort(n, a);

        int hesabi[n];
        for (int i = 0; i < n; i++)
            hesabi[i] = i;

        for (int i = 0; i < n; i++)
        {
            if (hesabi[i] != a[i])
                count += abs(hesabi[i] - a[i]);
        }

        cout << count << "\n";
    }
}
