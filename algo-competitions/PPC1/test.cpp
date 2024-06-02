#include <iostream>
#include <algorithm>
using namespace std;

void print(int a[], int n)
{
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << "\n";
}

int main()
{
    int a[5] = {1, 2, 3, 4, 5};
    sort(a, a + 5, [](int a, int b)
         { return a > b; });
    print(a, 5);
}