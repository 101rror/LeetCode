func checkGoodInteger(n int) bool {
	digitSum := 0
	squreSum := 0

	for n > 0 {
		r := n % 10
		digitSum += r
		squreSum += r * r
		n /= 10
	}

	return squreSum-digitSum >= 50
}