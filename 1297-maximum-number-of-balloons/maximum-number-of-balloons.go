func maxNumberOfBalloons(text string) int {
	cnt := make(map[rune]int)

	for _, ch := range text {
		cnt[ch]++
	}

	cnt['l'] /= 2
	cnt['o'] /= 2

	ans := cnt['b']
	for _, ch := range []rune{'a', 'n', 'l', 'o'} {
		if cnt[ch] < ans {
			ans = cnt[ch]
		}
	}

	return ans
}