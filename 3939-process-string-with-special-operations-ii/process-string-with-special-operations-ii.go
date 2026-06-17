func processStr(s string, k int64) byte {
	var ans int64

	for i := 0; i < len(s); i++ {
		switch s[i] {
		case '*':
			if ans > 0 {
				ans--
			}
		case '#':
			ans *= 2
		case '%':
			continue
		default:
			ans++
		}
	}

	if k+1 > ans {
		return '.'
	}

	for i := len(s) - 1; i >= 0; i-- {
		switch s[i] {
		case '*':
			ans++
		case '#':
			half := ans / 2
			if k >= half {
				k -= half
			}
			ans = half
		case '%':
			k = ans - k - 1
		default:
			if k+1 == ans {
				return s[i]
			}
			ans--
		}
	}

	return '.'
}