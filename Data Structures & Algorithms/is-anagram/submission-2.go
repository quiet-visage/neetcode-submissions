
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    m1 := make(map[rune]int)
    m2 := make(map[rune]int)
    for _, v := range(s) {
        m1[v] += 1
    }
    for _, v := range(t) {
        m2[v] += 1
    }
    for _, v := range(t) {
        ok := m1[v] == m2[v]
        if !ok {
            return false
        }
    }
    return true
}
