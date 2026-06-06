class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dic = new HashMap<>();
        for (int i: nums) {
            dic.put(i, dic.getOrDefault(i,0) + 1);
        }

        // System.out.println(dic);

        for (int x : dic.values()) {
            // System.out.println(x);
            if (x > 1) return true;
        }

        return false;
        
    }
}