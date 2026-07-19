func rearrangeString(s string, x byte, y byte) string {
	n := len(s)
	var left, mid, right []byte

	for i := 0; i < n; i++ {
		if s[i] == y {
			left = append(left, s[i])
		} else if s[i] == x {
			right = append(right, s[i])
		} else {
			mid = append(mid, s[i])
		}
	}

	return string(append(append(left, mid...), right...))
}