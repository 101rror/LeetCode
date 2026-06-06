func leftRightDifference(nums []int) []int {
	total := 0
	for _, x := range nums {
		total += x
	}

	left := 0
	ans := make([]int, len(nums))

	for i, x := range nums {
		total -= x

		if left > total {
			ans[i] = left - total
		} else {
			ans[i] = total - left
		}

		left += x
	}

	return ans
}