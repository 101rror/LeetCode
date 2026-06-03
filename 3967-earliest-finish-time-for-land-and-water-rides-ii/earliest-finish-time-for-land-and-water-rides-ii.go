func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	const INF = int(1e18)

	ans, minLand, minWater := INF, INF, INF

	for i := 0; i < len(landStartTime); i++ {
		minLand = min(minLand, landStartTime[i]+landDuration[i])
	}

	for i := 0; i < len(waterStartTime); i++ {
		ans = min(ans, max(minLand, waterStartTime[i])+waterDuration[i])
	}

	for i := 0; i < len(waterStartTime); i++ {
		minWater = min(minWater, waterStartTime[i]+waterDuration[i])
	}

	for i := 0; i < len(landStartTime); i++ {
		ans = min(ans, max(minWater, landStartTime[i])+landDuration[i])
	}

	return ans
}