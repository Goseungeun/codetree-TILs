#include <iostream>
#include <string> 
#include <climits> 

using namespace std; 

string str1, str2;
int n; 

void Swap(int idx, string& str1){
    if(idx-1>=0){
        str1[idx-1] = str1[idx-1]=='0'?'1': '0';
    }
    str1[idx] = str1[idx]=='0'?'1':'0';
    if(idx+1<n)
        str1[idx+1] = str1[idx+1] == '0' ? '1' : '0'; 
}

int GetCnt(string str1){

    int cnt = 0;
    for(int i=1; i<n; i++){
        if(str1[i-1]==str2[i-1])
            continue;
        cnt++;
        Swap(i, str1); 
    }    
    if(str1[n-1]!=str2[n-1])
        return INT_MAX;
    return cnt; 
}

int main() {
    cin>>n;
    cin>>str1>>str2;

    string tmp1 = str1; 
    int ans1 = GetCnt(tmp1);

    string tmp2 = str1; 
    Swap(0, tmp2); 
    int ans2 = GetCnt(tmp2); 
    if(ans2!=INT_MAX)
        ans2++; 
    int ans = min(ans1, ans2);
    if(ans==INT_MAX)
        ans=-1;
    cout<<ans; 
    
    return 0;
}