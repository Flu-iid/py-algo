#include <iostream>
#include <math.h>
using namespace std;

long max_element(long a[], long n)
{
    long max_a = 0;
    for (long i = 0; i < n; i++)
        if (a[i] > max_a)
            max_a = a[i];

    return max_a;
}

int main()
{
    long test;
    cin >> test;
    for (long t = 0; t < test; t++)
    {
        long n;
        cin >> n;
        long array[n];
        for (long d = 0; d < n; d++)
            cin >> array[d];
        long count = 0;
        long max_a = max_element(array, n);
        for (long i = 0; i < n; i++)
        {
            long e1 = array[i];
            for (long j = 0; j < n; j++)
            {

                long e2 = array[j];
                if (pow(e1, j + 1) > max_a)
                    break;
                if (e1 == 1)
                {
                    count += n;
                    break;
                }
                if (pow(e1, j + 1) <= e2)
                    count++;
            }
        }
        cout << count << endl;
    }
}