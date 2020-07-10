#include<bits/stdc++.h>
#include<string>
using namespace std;

int myCompare(string X, string Y) 
{ 
    // first append Y at the end of X 
    string XY = X.append(Y); 
  
    // then append X at the end of Y 
    string YX = Y.append(X); 
  
    // Now see which of the two formed numbers is greater 
    return XY.compare(YX) > 0 ? 1: 0; 
}  

void print(vector < string > &vstr){
    
    for(int i = 0; i < vstr.size(); i++){
        cout<<vstr[i];
    }
}

void solution(vector < int > &v){

    vector < string > vstr;
    int flag = 0;
    int k = 0;
    while(k < v.size()){
        if(v[k++] != 0){
            flag = 1;
        }
    }
    cout<<"flag"<<flag;
    if (flag == 0){
        cout<< "0";
    } else {
    for(int i = 0; i < v.size(); i++){
        vstr.push_back(to_string(v[i]));
    }

    sort(vstr.begin(), vstr.end(), myCompare); 

    print(vstr);

    
    }
}

int main(){

    vector < int > v;
    v.push_back(0);
    v.push_back(0);
    v.push_back(1);
    v.push_back(0);

    solution(v);
    return 0;
}