func digitFrequencyScore(n int) int {
	ans := 0

	for n > 0 {
		ans += n % 10
		n /= 10
	}

	return ans
}