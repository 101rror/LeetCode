func countValidPrefixes(s string) int {
	count0, count1, ans := 0, 0, 0

	for _, ch := range s {
		if ch == '0' {
			count0++
		} else {
			count1++
		}

		diff := count1 - count0
		if diff < 0 {
			diff = -diff
		}

		if diff <= 1 {
			ans++
		}
	}

	return ans
}