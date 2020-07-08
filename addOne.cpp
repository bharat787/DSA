#include<bits/stdc++.h>
using namespace std;
vector< int > print(vector < int > &v){

    // for(int i = 0; i < v.size(); i++){
    //     cout<<v[i]<<" ";
    // }
    // cout<<"\n";
    return v;
}

void addOne(vector < int > &v, int lsb){
    // int lsb = v.size() - 1;
    //int carry;

    
    v[lsb] += 1;
    if (v[lsb] <= 9){
        print(v);
    } else {
        
        v[lsb] = 0;
        addOne(v, lsb - 1);
    }
    

}



int main(){

    //cout<<23%10;
    vector < int > v;

    v.push_back(0);
    v.push_back(9);
    v.push_back(9);
    v.push_back(9);


    print(v);

    addOne(v, v.size()-1);




    return 0;
}