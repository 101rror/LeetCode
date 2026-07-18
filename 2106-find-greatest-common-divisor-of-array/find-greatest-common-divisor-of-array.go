func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func findGCD(nums []int) int {
	mx, mn := nums[0], nums[0]

	for _, num := range nums {
		mn = min(mn, num)
		mx = max(mx, num)
	}

	return gcd(mx, mn)
}