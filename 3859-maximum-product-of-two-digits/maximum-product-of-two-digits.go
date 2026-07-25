func maxProduct(n int) int {
	max1, max2 := 0, 0

	for n > 0 {
		rem := n % 10
		if rem > max1 {
			max2 = max1
			max1 = rem
		} else if rem > max2 {
			max2 = rem
		}
		n /= 10
	}

	return max1 * max2
}