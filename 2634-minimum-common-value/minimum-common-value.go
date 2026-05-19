func getCommon(nums1 []int, nums2 []int) int {
	n1, n2 := len(nums1), len(nums2)
	i, j := 0, 0

	for i < n1 && j < n2 {
		if nums1[i] == nums2[j] {
			return nums1[i]
		} else if nums1[i] < nums2[j] {
			i++
		} else {
			j++
		}
	}

	return -1
}