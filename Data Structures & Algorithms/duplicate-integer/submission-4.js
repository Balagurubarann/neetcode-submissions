class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        const count = {};

        for (let num of nums) {
            
            if (!count[num]) {
                count[num] = 1
            } else {
                return true;
            }
        } 

        return false;
    }
}
