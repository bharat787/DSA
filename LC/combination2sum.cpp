#include<bits/stdc++.h>
using namespace std;

int Backtracking(vector < vector < int > >& ans, vector < int >& temp, int index, vector < int >& nums, int target){

    if(target == 0){
        if(find(ans.begin(), ans.end(), temp) != ans.end()){
        ans.push_back(temp); 
        cout<<"found";
        } else { cout << "not ";}
        for(int j = 0; j < temp.size(); j++){
                cout<< temp[j];
            }
            cout<< endl;
        return 0;
    }
    else if(target < 0){
        return 0;
    }
    else{
        for(int i = index; i < nums.size(); i++){
            temp.push_back(nums[i]);
            Backtracking(ans, temp, i+1, nums, target-nums[i]);
            // for(int j = 0; j < temp.size(); j++){
            //     cout<< temp[j];
            // }
            // cout<< endl;
            temp.pop_back();
        }
    }
    return 1;
}

int main(){

    vector < int > candidates;
    int target = 8;
    candidates.push_back(1);
    candidates.push_back(1);
    candidates.push_back(2);
    candidates.push_back(5);
    candidates.push_back(6);
    candidates.push_back(7);
    candidates.push_back(10);

    vector < vector < int > > ans;
    vector < int > temp;
    Backtracking(ans, temp, 0, candidates, target);
    // for(int i = 0; i < ans.size(); i++){
    //     cout<<ans[i];
    // }
    return 0;
}