func minimumSwaps(nums []int) int {
	n := len(nums)
	zero, swap := 0, 0

	for _, num := range nums {
		if num == 0 {
			zero++
		}
	}

	for i := 0; i < n-zero; i++ {
		if nums[i] == 0 {
			swap++
		}
	}

	return swap
}