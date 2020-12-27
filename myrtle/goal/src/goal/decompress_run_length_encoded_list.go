package goal

// https://leetcode.com/problems/decompress-run-length-encoded-list/
type offsetElem struct {
	start int
	end   int
	value int
}

func decompressRLElist(nums []int) []int {
	elemNum := len(nums) / 2
	offset, total := 0, 0
	offsetList := make([]*offsetElem, elemNum)
	for i := 0; i < elemNum; i++ {
		length := nums[2*i]
		end := offset + length
		offsetList[i] = &offsetElem{
			start: offset,
			end:   end,
			value: nums[2*i+1],
		}
		offset = end
		total += length
	}
	ret := make([]int, total)
	for _, o := range offsetList {
		for i := o.start; i < o.end; i++ {
			ret[i] = o.value
		}
	}
	return ret
}
