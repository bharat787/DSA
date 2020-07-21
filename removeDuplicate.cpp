#include<bits/stdc++.h>
using namespace std;

int solution(vector < int > &A){

    int i = 0;
    int n = A.size();

    while(i < A.size() -1 ){
        int j = i+1;
        if(A[i] == A[j] && j<A.size())
        {
            //++j;
            n -= (j-i);
            A.erase(A.begin()+i+1, A.begin()+j+1);

        }
        ++i;

    }
    return n;
}

int main(){

    return 0;
}