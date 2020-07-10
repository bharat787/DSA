#include<bits/stdc++.h>
using namespace std;

void print(vector < vector < int > > matrix, int n){

    for(int i = 0; i < 2*n-1; i++){
        for(int j = 0; j < 2*n-1; j++){
            cout<<matrix[i][j];
        }
        cout<<"\n";
    }
}

vector < vector < int > > solution(int n){
    int maxm = 2*n-1;
    vector < vector < int > > matrix(maxm, vector < int >(maxm, -1));
    
    int top, bottom, right, left;
    top = 0;
    bottom = maxm;
    left = 0;
    right = maxm;

    while (top <= bottom && left<=right){
        int num = n-top;
        //cout<<"num"<<num<<"\n";

        if(top != bottom){
            for(int i = left; i < right; i++){
                matrix[top][i] = num;
            }
        }
        top++;
        //cout<<"T"<<top<<"B"<<bottom<<"L"<<left<<"R"<<right<<"\n";
        //print(matrix, 3);

        if(right != left){
            for(int i = top; i < bottom; i++){
                matrix[i][right-1] = num;
            }
        }
        right--;
        //cout<<"T"<<top<<"B"<<bottom<<"L"<<left<<"R"<<right<<"\n";
        //print(matrix, 3);



        if(top != bottom){
            for(int i = right; i > left; i--){
                matrix[bottom-1][i] = num;
            }
        }
        bottom--;
        //cout<<"T"<<top<<"B"<<bottom<<"L"<<left<<"R"<<right<<"\n";


        if(right != left){
            for(int i = bottom; i >= top; i--){
                matrix[i][left] = num;
            }
        }
        left++;
        //cout<<"T"<<top<<"B"<<bottom<<"L"<<left<<"R"<<right<<"\n";


        
    }

    

    return matrix;
}


int main(){

    print(solution(3), 3);
    return 0;
}