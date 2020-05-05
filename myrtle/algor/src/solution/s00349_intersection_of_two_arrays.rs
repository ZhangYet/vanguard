pub struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
	if nums1.len() == 0 || nums2.len() == 0 {
	    return Vec::new();
	}
	let mut nums1_map = HashMap::with_capacity(nums1.len());
	for i in &nums1 {
	    nums1_map.insert(i, true);
	}
        let mut nums2_map = HashMap::with_capacity(nums2.len());
	for i in &nums2 {
	    nums2_map.insert(i, true);
	}
	let mut res:Vec<i32> = Vec::new();
	for (key, value) in &nums1_map {
	    match nums2_map.get(key) {
		None =>{
		    continue;
		}
		Some(sub_index) => {
		    res.push(**key);
		}
	    }
	}
	return res;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_intersection() {
	let nums1: Vec<i32> = vec![1, 2, 2, 1];
	let nums2: Vec<i32> = vec![2, 2];
	assert_eq!(vec![2], Solution::intersection(nums1, nums2));
    }
}
