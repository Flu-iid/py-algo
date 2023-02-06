#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <direct.h>

using namespace std ;

void save(string );
int main()
{
    string str;
    int n,s = (n-1), temp;
    cout<<"pls enter how many line do you want : ";
    cin>>n;
    cout<<endl;
    int nums[n+1]={0};
    s = n-1;
    nums[s]=1;
    for(int i = 0 ; i < n ; i++)
    {
        cout<<endl;
       /*for(int j =0 ; j < s ; j++)
        {
            str+="  ";
        }*/
        for(int j = 0 ; j <= i ; j++)
        {
            temp = nums[s+j]+nums[s+j+1];
            str+="  "+to_string(temp);
            nums[s+j] = temp;
        }
        str+="\n";
        s--;
    } 
    save(str);  
    return 0;
}
void save (string str)
{
    const char *add = "C:\\Users\\Almasiran\\Desktop\\dice\\khayam\\";
    _mkdir(add);
    ofstream file;
    file.open(add + to_string(1)+".txt",ios_base::out);
    file<<str;
    file.close();
    cout<<"DOWN"<<endl;