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

vector < string > solution(vector < int > &v){

    vector < string > vstr;
    for(int i = 0; i < v.size(); i++){
        vstr.push_back(to_string(v[i]));
    }

    sort(vstr.begin(), vstr.end(), myCompare); 

    print(vstr);

    return vstr;

}

int main(){

    vector < int > v;
    v.push_back(54);
    v.push_back(546);
    v.push_back(548);
    v.push_back(60);

    solution(v);
    return 0;
}