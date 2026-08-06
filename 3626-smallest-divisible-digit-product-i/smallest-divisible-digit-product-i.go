func smallestNumber(n int, t int) int {
	for {
		x := n
		prod := 1

		for x > 0 {
			prod *= x % 10
			x /= 10
		}

		if prod%t == 0 {
			return n
		}

		n++
	}
}