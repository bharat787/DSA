#include<bits/stdc++.h>
using namespace std;
# define tr(container, it) /
for(typeof(container.begin())it = container.begin(); it != container.end(); it++)


int main() {
    set< int > s;

    for(int i=0; i<=100; i++){
        s.insert(i);
    }

    s.insert(43); // This would do nothing as 43 already exists

    for(int i= 2; i<= 100; i+=2) {
        s.erase(i); // Erase even vals
    }

    int n = int(s.size());  // n will be 50

    // push_back() is not used for sets as the order does'nt matter

    /*
        Since set is not a linear container, it's impossible to take
        the element in a set by index. Therefore, the only way to transverse
        the elements of a set is to use iterators.
    */

    // For eg to calculate the sum of elements
    int r = 0;
    for (set< int >::iterator it = s.begin(); it != s.end(); it++){
        r += *it; 
    }

    if(s.find(42) != s.end()) {
    // 42 presents in set
    }
    else {
    // 42 not presents in set
}
    return 0;
}