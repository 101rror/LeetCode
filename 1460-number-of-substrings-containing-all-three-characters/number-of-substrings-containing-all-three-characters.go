func numberOfSubstrings(s string) int {
	idx := make([]int, 3)
	count := 0

	for i, c := range s {
		idx[c-'a'] = i + 1

		minVal := idx[0]
		if idx[1] < minVal {
			minVal = idx[1]
		}
		if idx[2] < minVal {
			minVal = idx[2]
		}

		count += minVal
	}

	return count
}