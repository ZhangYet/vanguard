pub struct Solution {}

impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
	if n == 1 {
	    return true;
	}
	if n % 2 == 1 {
	    return false;
	}
	return  Self::is_power_of_two(n / 2);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_power_of_two() {
	assert_eq!(true, Solution::is_power_of_two(1));
	assert_eq!(false, Solution::is_power_of_two(3));
    }
}
