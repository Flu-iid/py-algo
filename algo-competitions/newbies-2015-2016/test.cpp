#include <iostream>
#include <string> 

using namespace std ;

int main()
{   
    int count,t,people,relation;
    cin>>t;
    
    for(;t != 0;t--)
    {   
        cin>>people>>relation;
        const int n = people + 1;
        int array[n];
        array[1]=1;
        for (int i = 0; i < relation ; i++)
        {
            int n1 , n2;
            cin>>n1>>n2;
            if(array[n1]==1)
            array[n2]==1;
            if(array[n2]==1)
            array[n1]==1;
        }
        for(int y = 0 ; y <= people ; y++)
        {if(array[y]== 1)
        count++;}
        cout<<count<<endl;
    }
    
    return 0;
}