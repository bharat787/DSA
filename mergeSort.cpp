#include<bits/stdc++.h>
using namespace std;

void merge(vector < int > &v, int start, int mid, int end){
    vector < int > temp(end - start + 1);

    int i = start, j = mid + 1, k = 0;

    while(i <= mid && j <= end){
        if(v[i] <= v[j]){
            temp[k++] = v[i++];
            
        } else {
            temp[k++] = v[j++];
            
        }
    }

    while(i <= mid){
        temp[k++] = v[i++];
    }

    while(j <= end){
        temp[k++] = v[j++];
    }

    for(i = start; i <= end; i++){
        v[i] = temp[i - start];
    }
}

void mergeSort(vector < int > &v, int start, int end){

    if(start < end) {
        int mid = (start + end) / 2;
        mergeSort(v, start, mid);
        mergeSort(v, mid+1, end);
        merge(v, start, mid, end);
    }
}

void print(vector < int > &v){
    for(int i = 0; i < v.size(); i++){
        cout<<v[i]<<" ";
    }
    cout<<"\n";
}

int main() {

    vector < int > v;

    v.push_back(1);
    v.push_back(14);
    v.push_back(75);
    v.push_back(4);
    v.push_back(17);

    print(v);
    
    mergeSort(v, 0, v.size()-1);

    print(v);

    cout<<v.size();

    return 0;
}