#include <stdio.h>

long long sum(long long n, int multiplier){
    // sum 1 to n, not including n it self
    long long max = (n-1)/multiplier;
    return (max*(max+1)/2)*multiplier;
}

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long long n; 
        scanf("%lld",&n);
        printf("%lld\n", sum(n, 3) + sum(n, 5) - sum(n, 15));
    }
    return 0;
}