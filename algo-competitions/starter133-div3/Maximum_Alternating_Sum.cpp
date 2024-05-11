#include <iostream>
#include <algorithm>

using namespace std;

int answer(int n, int a[])
{
    sort(a, a + n);
    bool is_j = true;
    int i = 0;
    int j = n - 1;
    int result = 0;
    while (j >= i)
    {
        if (is_j)
        {
            result += a[j];
            j--;
        }
        else
        {
            result -= a[i];
            i++;
        }
        is_j = !is_j;
    }
    return result;
}

int main()
{
    int test;
    cin >> test;
    for (int t = 0; t < test; t++)
    {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];

        cout << answer(n, a) << "\n";
    }
}