#include<bits/stdc++.h>
using namespace std;

int main(){
    vector< vector < int > > matrix;
    int k = 0;
    for(int i = 0; i < 5; i++){
        vector < int > v;
        for (int j = 0; j < 5; j++){
            v.push_back(k++);
        }
        matrix.push_back(v);
    }

    for(int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            cout<<matrix[i][j]<<" ";
        }
    }

    matrix[2][2] = 100;
    cout<<matrix[2][2];
    int N = 5; 
    int M = 5;
    vector< vector < int > >  Matrix1(N, vector< int >(M, -1));

    for(int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            cout<<Matrix1[i][j]<<" ";
        }
    }

    
}