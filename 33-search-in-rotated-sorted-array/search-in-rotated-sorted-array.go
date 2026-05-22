func search(nums []int, target int) int {
	n := len(nums)

	for i := 0; i < n; i++ {
		if nums[i] == target {
			return i
		}
	}

	return -1
}