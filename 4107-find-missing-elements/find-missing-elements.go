import "slices"

func findMissingElements(nums []int) []int {
	n := len(nums)
	slices.Sort(nums)
	ans := []int{}

	for i := nums[0]; i < nums[n-1]; i++ {
		if !slices.Contains(nums, i) {
			ans = append(ans, i)
		}
	}

	return ans
}