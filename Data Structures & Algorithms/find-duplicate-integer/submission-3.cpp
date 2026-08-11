class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        while(true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if(slow==fast) break;
        }
        int start = 0;
        while (true) {
            start = nums[start];
            slow = nums[slow];
            if (start == slow) return start;
        }
    }
};
