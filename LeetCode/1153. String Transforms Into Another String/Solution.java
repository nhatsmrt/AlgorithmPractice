class Solution {
    public boolean canConvert(String str1, String str2) {
        Map<Character, Character> transformMap = new HashMap<>();
        Set<Character> str2CharSet = new HashSet<>();
        for (int i = 0; i < str2.length(); i++) {
            if (transformMap.containsKey(str1.charAt(i)) &&
                transformMap.get(str1.charAt(i)) != str2.charAt(i))
                return false;
            transformMap.put(str1.charAt(i), str2.charAt(i));
            str2CharSet.add(str2.charAt(i));
        }

        if (str2CharSet.size() < 26)
            return true;

        Set<Character> visited = new HashSet<>();
        for (int i = 0; i < str1.length(); i++) {
            if (!dfs(str1.charAt(i), visited, new HashSet<>(), transformMap))
                return false;
        }
        return true;
    }

    private boolean dfs(char c, Set<Character> visited, Set<Character> ancestors, Map<Character, Character> transformMap) {
        if (visited.contains(c))
            return true;

        visited.add(c);
        ancestors.add(c);
        if (transformMap.containsKey(c)) {
            char to = transformMap.get(c);
            if (to == c)
                return true;

            if (ancestors.contains(to))
                return false;
            return dfs(to, visited, ancestors, transformMap);
        }

        return true;
    }
}
