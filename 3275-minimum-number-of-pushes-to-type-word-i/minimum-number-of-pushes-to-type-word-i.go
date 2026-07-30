func minimumPushes(word string) int {
	n := len(word)

	if n <= 8 {
		return n
	} else if n <= 16 {
		n -= 8
		return 8 + (n * 2)
	} else if n <= 24 {
		n -= 16
		return 24 + (n * 3)
	} else {
		n -= 24
		return 48 + (n * 4)
	}
}