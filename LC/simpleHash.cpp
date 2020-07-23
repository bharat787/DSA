#include<bits/stdc++.h>
using namespace std;

// Simple example to use hash table to count frequency of letters in string

int Frequency[26];

int hashFunc(char c){
    return (c - 'a');
}

void countFre(string s){

    for(int i = 0; i < s.length(); ++i){
        int index = hashFunc(s[i]);
        Frequency[index]++;
    }

    for(int i = 0; i< 26; ++i)
        cout<<(char)(i + 'a') << ' ' << Frequency[i]  << endl;
}

int main(){

    string s = "ababcd";
    countFre(s);
    return 0;
}