#include <bits/stdc++.h>
#include <vector>
using namespace std;


int main (){
    vector < int > v;

    for (int i = 0; i < 10; i++){
        v.push_back(i);
    }

    /*
        push_back adds an element to the last. Instead of
        allocating memory for just one element vector always
        allocates more memory then it actually needs when adding
        elements using push_back
    */

    for (int i = 0; i < 10; i++){
        cout<<v[i];
    }

    // To get size 
    int count = v.size();

    // To know if vector is empty
    bool isNonEmpty = !v.empty()  ;  // (v.size() >= 0 ) is a bad method
    /*
        This is because not all containers report their size in
        O(1), and you definately should not require counting all
        elements in a double linked list just to ensure that it 
        contains atleast one.
    */

   // When you need to resize vector use resize()

   vector < int > v1(20);
   v.resize(25);
   // resize fills the newly allocated spaces with 0
   // If you use push_back after resize then new elements
   // are added after it rather than INTO it, 

    // Notice we use parantheses Instead of [] when dealing with vectors

    // To clear out the vector use .clear() member function. It completely
    // the container to contain zero elements.

    // A vector can be made to contain any data type
    vector < string > names(20, "Unknown");

    cout<<names[0];

    // To make a multi-dimensional one
    vector< vector < int > > Matrix;

    //  To make a multi-dimensional array of specific size
    int N, M;

    vector< vector < int > >  Matrix1(N, vector< int >(M, -1)); // Here we create a Matrix of N*M and fill it with -1

    /*
        When vector is passed as a parameter to a function
        a copy of the vector is actually created. It may take
        a lot of time and memory to create a new vector when 
        actually not needed.
    */

   // So you should never write
   void some_function(vector< int > v){
       //until you actually know what you're doing.
   }

   // Instead write
   void proper_function(const vector< int > v){
       // rest of the code.
   }

   // If you're going to change the contents of vector
   void canChangeFunction( vector< int > &v){
       // rest of the code here
   }

   // To insert after a particular index
   v.insert(1, 242) //  Insert value 242 after the first index

   // It shifts the rest of the elements to the right.
return 0;
}