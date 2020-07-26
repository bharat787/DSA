#include<bits/stdc++.h>
using namespace std;

long long int rev(int num){

    bool isNeg = false;
    if(num < 0){
        isNeg = true;
        num = -num;
    }
    auto rev = 0;
    auto prev = 0;
    auto dig = 0;
    while (num != 0){
        dig = num%10;
        rev = rev * 10 + dig;

        // overflow check
        if((rev - dig ) / 10 != prev){
            cout<<"OV"<<endl;
            return 0; // overflowed number
        } 

        prev = rev;
        //cout<< rev;
        num /= 10;

    }

    if(isNeg == true){
        rev = -rev;
    }
    return rev;
}

int main(){

    auto num = rev(1534236469);
    cout << num;
    return 0;
}