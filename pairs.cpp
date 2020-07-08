#include <bits/stdc++.h>
using namespace std;

int main() {
    pair <int, char> pair1; // The pairs can be of any datatype

    pair1.first = 100;
    pair1.second = 'G';

    cout << pair1.first << " " ; 
    cout << pair1.second << endl ; 

    // A complex way to make pairs

    pair<string, pair< int, int > > P;
    string s = P.first;
    int x = P.second.first;
    int y = P.second.second; 
  
    return 0;

}