#include <bits/stdc++.h>
using namespace std;
long long L,R;
int ans;
int main()
{
	scanf("%lld%lld",&L,&R);
	if (R-L>=10) printf("%d\n",0);
	else
	{
		ans=1;
		for (long long i=L+1;i<=R;i++)
			ans=(1LL*ans*(i%10))%10;
		printf("%d\n",ans);
	}
	return 0;
}