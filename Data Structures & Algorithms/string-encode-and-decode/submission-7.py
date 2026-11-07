class Solution:

    def encode(self, strs: List[str]) -> str:
        # ['hello', 'world'] => 5#hello5#world
        string = ""
        for i in strs:
            string+= f"{len(i)}#{i}"
        return string

    def decode(self, s: str) -> List[str]:
        # 5#hello5#world => ['hello', 'world']
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            result.append(word)
            i += length
        return result


