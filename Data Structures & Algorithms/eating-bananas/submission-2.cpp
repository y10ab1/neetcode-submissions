class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        int ans = r;
        while (l <= r){
            int k = (l + r) / 2;
            if (valid(piles, k, h) == true){
                ans = k;
                r = k - 1;
            } else {
                l = k + 1;
            }
            
        }
        return ans;
    }

    bool valid(vector<int> piles, int k, int h){
        int cnt = 0;
        for (int p : piles){
            cnt += ceil(static_cast<float> (p) / k);
            if (cnt > h){
                return false;
            }
        }
        return true;
    }
};
