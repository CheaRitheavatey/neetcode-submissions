class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hash1 = new HashMap<>();
        HashMap<Character, Integer> hash2 = new HashMap<>();

        if (s.length() != t.length()) return false;
        Arrays.sort(s.toCharArray());
        Arrays.sort(t.toCharArray());



        for (char c: s.toCharArray()) {
            hash1.put(c, hash1.getOrDefault(c,0) + 1);
        }

        for (char c: t.toCharArray()) {
            hash2.put(c, hash2.getOrDefault(c,0) + 1);
        }

        // System.out.println(hash1);
        // System.out.println(hash2);

        if (hash1.equals(hash2)) return true;

        return false;
    }
}
