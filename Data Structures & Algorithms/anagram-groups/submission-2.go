func isAnagram(si, sj string) bool {
    if len(si) != len(sj) {
        return false
    }
    mi := make(map[byte]int)
    mj := make(map[byte]int)
    for i := 0; i < len(si); i+=1 {
        mi[si[i]] += 1
        mj[sj[i]] += 1
    }
    for i := 0; i < len(si); i+=1 {
        ok := mi[si[i]] == mj[si[i]]
        if !ok {
            return false
        }
    }
    return true
}

func groupAnagrams(strs []string) [][]string {
    res := make([][]string, 0)
    proc := make(map[int]bool)
    for i := 0; i < len(strs); i+=1 {
        grp := []string{strs[i]}
        for j := i+1; j < len(strs); j+=1 {
            _, was_proc := proc[j]
            if was_proc || !isAnagram(strs[i], strs[j]) {
                continue
            }
            grp = append(grp, strs[j])
            proc[j] = true
        }
        _, was_proc := proc[i]
        if !was_proc || len(grp) >1 {
            res = append(res, grp)
        }
    }
    return res
}
