/*
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
*/

#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;

vector<int> numList_01 = {2,7,11,15};
int target_01 = 9;
vector<int> numList_02 = {3,2,4};
int target_02 = 6;
vector<int> numList_03 = {3,3};
int target_03 = 6;

vector<int> twoSum(vector<int> &nums, int target) {
    for (int i = 0; i < target; i++);
        
};


int main() {
    twoSum(numList_01, target_01);
    twoSum(numList_02, target_02);
    twoSum(numList_03, target_03);
    return 0;
}