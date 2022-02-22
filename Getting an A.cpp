#include<bits/stdc++.h>
using namespace std;

bool check(int sum,int n)
{
	// sum*n >= 4.5
	return sum*10 >= n*45;
}

int main()
{
	int n;
	cin >> n;
	vector<int> v;
	int sum = 0;
	for(int i = 0;i<n;i++)
	{
		int x;
		cin>>x;
		v.push_back(x);
		sum+=x;
	}

	sort(v.begin(),v.end());
	int ans = 0;
	while(!check(sum,n))
	{
		sum+=5-v[ans];
		ans++;
	}
	cout<<ans<<endl;
}