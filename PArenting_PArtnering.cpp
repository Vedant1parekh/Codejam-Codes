#include <bits/stdc++.h>
using namespace std;
int main()
{
    int te,i,n,c,j,flag;
    cin>>te;
    for(int m=1;m<=te;m++)
    {
        string st;
        cin>>n;
        vector<pair<int,pair<int,int> > >v;
        int s[n],e[n];
        for(i=0;i<n;i++)
        {
            cin>>s[i]>>e[i];
            v.push_back({s[i],{e[i],i}});
            st+='C';
   }
    sort(v.begin(),v.end());
    c=0,j=0,flag=0;
    for(i=0;i<v.size();i++)
    {
        if(v[i].first>=c)
        {
            st[v[i].second.second]='C';
            c=v[i].second.first;
        }
    else if(v[i].first>=j)
    {
        st[v[i].second.second]='J';
        j=v[i].second.first;
    }
   else
   {
      flag=1;
      break;
   }
}
if(flag==1)
{
     cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
     continue;
}
     cout<<"Case #"<<m<<": "<<st<<endl;

}
}
