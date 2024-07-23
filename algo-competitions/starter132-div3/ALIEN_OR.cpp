#include <iostream>
#include <math.h>
using namespace std;

long bin_to_decimal(string n)
{
    int length = n.length();
    long result = 0;
    for (int i = 0; i < length; i++)
        result += (n[i] - '0') * pow(2, length - i - 1);
    return result;
}

bool answer(int n, int k, long check[])
{
    long goal[k];
    long num = 1;
    for (int i = 0; i < k; i++)
    {
        goal[i] = num;
        num <<= 1;
    }
    long cnt = 0;
    for (int g = 0; g < k; g++)
    {
        bool once = true;
        for (int c = 0; c < n; c++)
            if (goal[g] == check[c] and once)
            {
                cnt++;
                once = false;
            }
    }
    return (cnt == k) ? true : false;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n, k;
        cin >> n >> k;
        long a[n];
        string str_tmp;
        for (int j = 0; j < n; j++)
        {
            cin >> str_tmp;
            a[j] = bin_to_decimal(str_tmp);
        }
        cout << (answer(n, k, a) ? "YES\n" : "NO\n");
    }
}