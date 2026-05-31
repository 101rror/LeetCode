func asteroidsDestroyed(mass int, asteroids []int) bool {
	sort.Ints(asteroids)

	m := int64(mass)

	for _, x := range asteroids {
		if m < int64(x) {
			return false
		}
		m += int64(x)
	}
	return true
}