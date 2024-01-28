// @param Number[] - nums
// @param Number - target
// @return Number[] 
var currentsum;

var twoSum = function(nums,target){
    for (var i = nums.length-1; i>=0; i--){
        for (var j = 0; j<i ; j++){
            currentsum = nums[i]+nums[j];
            if (currentsum === target) console.log('Elements ' + i + ' and ' + j + ' add up to ' + target) ;
        }
    }

}

twoSum([3,4,5,6,7],10);

// execute node 1-twosum.js