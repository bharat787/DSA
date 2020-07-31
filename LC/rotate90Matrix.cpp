class Solution {
public:
    void replace(vector<vector<int>>& matrix,int a ,int n){
        if(a>=n ) return;
        
        for(int k=0;k<n-a;k++){
            int t=matrix[a][a+k];
            matrix[a][a+k]=matrix[n-k][a];
            matrix[n-k][a]=matrix[n][n-k];
            matrix[n][n-k]=matrix[a+k][n];
            matrix[a+k][n]=t;
        }
        replace(matrix,a+1,n-1);
        return;
    }
    void rotate(vector<vector<int>>& matrix) {
        int n=matrix[0].size();
        replace(matrix,0,n-1);
        return;
        
    }
};