#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i = 1 ; i <= t ; i++)
    {
        int n;
        cin>>n;
        for(int j = 1 ; j <= n ; j++)
        {

            int act,max;
            cin>>act;
            if(max < act)
            {max = act;}
            if(j == n)
            {cout<<abs(max-144)<<endl;}
        }

    }
    return 0;
}