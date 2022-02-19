#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long a,b;
    long long ans;//Take care, integer overflow can emerge everywhere!
    while(~scanf("%lld%lld",&a,&b))
    {
        ans=1;
        for(long long i=a+1;i<=b;i++)
        {
            ans=(ans*(i%10))%10;
            if(!ans) break;
        }
        printf("%lld\n",ans);
    }
    return 0;
}
 
/*Hence we can multiply the integers one by one, 
only preserving the last digit (take it modulo 10 whenever possible), and stop when it becomes 0. 
It's obvious that at most 10 multiplications are needed before stopping, 
and it's not hard to prove a tighter upper bound of 5.*/