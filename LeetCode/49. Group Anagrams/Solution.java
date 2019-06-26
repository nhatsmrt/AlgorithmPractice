class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        for (String str : strs) {
            String code = getCode(str);
            if (!map.containsKey(code))
                map.put(code, new ArrayList<String>());
            map.get(code).add(str);
        }
        List<List<String>> ret = new ArrayList<List<String>>();
        for (String code : map.keySet()) {
            ret.add(map.get(code));
        }
        return ret;
    }

    private String getCode(String str) {
        int[] chars = new int[26];
        for (int i = 0; i < str.length(); i++) {
            chars[(int) (str.charAt(i) - 'a')] += 1;
        }
        String ret = "";
        for (int i = 0; i < 26; i++) {
            ret += "" + chars[i];
        }
        return ret;
    }

    private void print(String str) {
        System.out.println(str);
    }
}
