#include<bits/stdc++.h>
using namespace std;

string hashTable[21];
int hashTableSize = 21;

int hashFun(){
    // Make a function
}

void insert(string s){
    
    int index = hashFun(s); // get hash val

    // search for an unused slot and if the index
    // exceeds the hashTableSize then roll back
    int h = 1;
    while(hashTable[index] != ""){
        index = (index + h*h) % hashTableSize;
        h++;
    }
    hashTable[index] = s;
}

void search(string s){

    int index = hashFun(s);

    // Search for the unused slot and if the 
    // index will exceed the hashTableSize will 
    // roll back
    int h = 1;
    while(hashTable[index] != s and hashTable[index] != ""){
        index = (index + h*h) % hashTableSize;
        h++;
    }
    //check if the table has the element
    if(hashTable[index] == s){
        cout << s << " is found " << endl;
    } else 
        cout << s << " is not found " << endl;
        
}