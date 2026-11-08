class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for elem in strs:
            n = len(elem)
            encoded += f"{n}#{elem}"

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        print(s)
        while i < len(s):
            j = s.find("#", i)
            if j == -1:
                break
            length = int(s[i:j])
            tok = s[j + 1 : j + 1 + length]
            print(i, j, length, tok)
            result.append(tok)
            i = j + 1 + length
        return result
