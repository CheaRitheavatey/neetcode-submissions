class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_str = defaultdict(list)
        
        for i in strs:
            arr_word = [0] * 26 
            for char in i:
                arr_word[ord(char) - ord('a')] += 1

            set_str[tuple(arr_word)].append(i)
            
        return list(set_str.values())
