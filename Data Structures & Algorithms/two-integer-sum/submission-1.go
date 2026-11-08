func twoSum(nums []int, target int) []int {
    res := make([]int, 0)
    m := make(map[int]int)
    for i, n := range nums {
        diff := target - nums[i]
        si, ok := m[diff]
        if ok {
            res = append(res, si, i)
        } else {
            m[n] = i
        }
    }
    return res
}
