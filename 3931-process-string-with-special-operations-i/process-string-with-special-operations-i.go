func processStr(s string) string {
	ans := ""

	for _, ch := range s {
		switch ch {
		case '*':
			if len(ans) > 0 {
				ans = ans[:len(ans)-1]
			}
		case '#':
			ans += ans

		case '%':
			r := []rune(ans)
			for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
				r[i], r[j] = r[j], r[i]
			}
			ans = string(r)

		default:
			ans += string(ch)
		}
	}

	return ans
}