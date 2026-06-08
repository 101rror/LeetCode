func pivotArray(nums []int, pivot int) []int {
	ans := make([]int, 0, len(nums))

	for _, x := range nums {
		if x < pivot {
			ans = append(ans, x)
		}
	}

	for _, x := range nums {
		if x == pivot {
			ans = append(ans, x)
		}
	}

	for _, x := range nums {
		if x > pivot {
			ans = append(ans, x)
		}
	}

	return ans
}