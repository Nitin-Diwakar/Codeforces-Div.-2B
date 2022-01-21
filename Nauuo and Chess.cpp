#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long LL;
const int MAXN = 1e3 + 10;
const int MOD = 1e9 + 7;
int n, m, k, t;
int x, y;
 
int A[MAXN][MAXN];
 
int main()
{
    cin >> n;
    if (n == 1)
    {
        cout << 1 << endl;
        cout << 1 << ' ' << 1 << endl;
        return 0;
    }
    for (int i = 2;i <= n;i++)
        if ((i-1)*2 >= n-1)
        {
            x = y = i;
            break;
        }
    for (int i = 1;i <= x;i++)
        A[1][i] = i;
    for (int i = x, v = n;i >= 1 && v > x;i--,v--)
        A[x][i] = v;
 
    cout << x << endl;
    for (int i = 1;i <= x;i++)
        for (int j = 1;j <= y;j++)
            if (A[i][j] <= n && A[i][j] >= 1)
                cout << i << ' ' << j << endl;
 
    return 0;
}