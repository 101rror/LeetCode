func limitOccurrences(nums []int, k int) []int {
	count := 0

	for _, num := range nums {
		if count < k || num != nums[count-k] {
			nums[count] = num
			count++
		}
	}

	return nums[:count]
}