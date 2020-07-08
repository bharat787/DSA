#include<bits/stdc++.h>
using namespace std;


void swap(int *a, int *b)
{
	int temp; 
	temp = *a;
	*a = *b;
	*b = temp;
}

int partition(vector < int > &v, int low, int high){
    int pivot, index, i;
    index = low;
    pivot = high;

    for(i = low; i < high; i++){
        if(v[i] < v[pivot]){
            swap(v[i], v[index++]);
        }
    }

    swap(v[pivot], v[index]);

    return index;
}

int randomPivotPartition(vector < int > &v, int low, int high){
    int pvt, n, temp;
    n = rand();

    pvt = low + n%(high-low+1);

    swap(v[high], v[pvt]);

    return partition(v, low, high);
}

 void quickSort(vector < int > &v, int low, int high){
     int pindex;
     if(low < high){
        pindex = randomPivotPartition(v, low, high);

        quickSort(v, low, pindex-1);
        quickSort(v, pindex, high);
     }
 }

void print(vector < int > &v){
    for(int i = 0; i < v.size(); i++){
        cout<<v[i]<<" ";
    }
    cout<<"\n";
}

int main(){

     vector < int > v;

    v.push_back(1);
    v.push_back(14);
    v.push_back(75);
    v.push_back(4);
    v.push_back(17);

    print(v);
    
    quickSort(v, 0, v.size()-1);

    print(v);

    return 0;
}