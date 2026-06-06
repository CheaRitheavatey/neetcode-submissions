class Solution:


    def encode(self, strs: List[str]) -> str:

        new_words = []
        if not strs:
            return "∅"

        for s in strs:
            encoded = ""
            for ch in s:
                encoded += str(ord(ch)) + " "
            new_words.append(encoded.rstrip())  # remove trailing space per word

        return "\n".join(new_words)
    
 


    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "∅":
            return []

        array = []
        words = s.split("\n")

        for i in words:
            # IMPORTANT: this preserves [""] correctly
            if i == "":
                array.append("")
                continue

            word = ""
            for char in i.split(" "):
                if char == "":
                    continue
                word += chr(int(char))

            array.append(word)

        return array
