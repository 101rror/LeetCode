func numberOfSpecialChars(word string) int {
	ans := 0

	for ch := 'a'; ch <= 'z'; ch++ {
		last := strings.LastIndexByte(word, byte(ch))
		first := strings.IndexByte(word, byte(ch-'a'+'A'))

		if last != -1 && first != -1 && last < first {
			ans++
		}
	}

	return ans
}