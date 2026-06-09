func maxTotalValue(nums []int, k int) int64 {
	mx, mn := math.MinInt, math.MaxInt

	for _, num := range nums {
		mx = max(mx, num)
		mn = min(mn, num)
	}

	return int64(mx-mn) * int64(k)
}