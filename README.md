# DSA-Cpp-LeetCode 🧠

This repository contains my C++ solutions for LeetCode problems. I'm consistently solving DSA problems to improve my problem-solving skills and prepare for coding interviews.

## 💻 Languages Used
- C++

## 🚀 Goals
- Solve 100+ LeetCode problems by year-end.
- Focus on core topics like Arrays, Strings, Linked Lists, Trees, Graphs, DP.

## 📁 Folders
Organized by topic:
- Arrays
- Strings
- LinkedList
- Trees
- Graphs
- Dynamic Programming

## 🌱 Example
```cpp
// TwoSum.cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for(int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if(map.count(diff)) return {map[diff], i};
            map[nums[i]] = i;
        }
        return {};
    }
};
