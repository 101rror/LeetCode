func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	n := len(landStartTime)
	m := len(waterStartTime)

	ans := int(^uint(0) >> 1)

	for i := 0; i < n; i++ {
		landEnd := landStartTime[i] + landDuration[i]

		for j := 0; j < m; j++ {
			startWater := max(landEnd, waterStartTime[j])
			finish := startWater + waterDuration[j]
			if finish < ans {
				ans = finish
			}
		}
	}

	for j := 0; j < m; j++ {
		waterEnd := waterStartTime[j] + waterDuration[j]

		for i := 0; i < n; i++ {
			startLand := max(waterEnd, landStartTime[i])
			finish := startLand + landDuration[i]
			if finish < ans {
				ans = finish
			}
		}
	}

	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}