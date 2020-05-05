pub struct Solution {}

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        // 处理空列表的情况
        // 如果不是这样写而是判断 tail < 1
        // 会有问题：
        // usize 类型是大于等于0的，一旦 usize 0 - 1 就溢出，然后 rust 就 panic 了
        if s.len() == 0 {
            return;
        }
        let mut head = 0;
        let mut tail = s.len() - 1;
        while head < tail {
            let tmp = s[head];
            s[head] = s[tail];
            s[tail] = tmp;
            head += 1;
            tail -= 1;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_string() {
        let mut test_string = vec!['a', 'e', 'i', 'o', 'u'];
        Solution::reverse_string(&mut test_string);
        assert_eq!(vec!['u', 'o', 'i', 'e', 'a'], test_string);
        let mut test_string2 = vec![];
        Solution::reverse_string(&mut test_string2);
    }
}
