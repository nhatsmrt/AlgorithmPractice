class SpecialMultiSet {
    private Map<Character, Integer> charMap;
    private Map<Character, Integer> requiredMap;
    private int totalLength;

    public SpecialMultiSet(String starter) {
        charMap = new HashMap<Character, Integer>();
        requiredMap = new HashMap<Character, Integer>();
        for (int i = 0; i < starter.length(); i++) {
            if (!requiredMap.containsKey(starter.charAt(i)))
                requiredMap.put(starter.charAt(i), 1);
            else
                requiredMap.put(starter.charAt(i), requiredMap.get(starter.charAt(i)) + 1);
        }
    }

    public void add(Character c) {
        if (!charMap.containsKey(c))
            charMap.put(c, 1);
        else
            charMap.put(c, charMap.get(c) + 1);

        if (charMap.get(c).equals(requiredMap.get(c)))
            totalLength += 1;
    }

    public void remove(Character c) {
        if (charMap.containsKey(c)) {
            if (charMap.get(c) == 1) {
                charMap.remove(c);
                if (requiredMap.get(c) == 1)
                    totalLength -= 1;
            }
            else {
                charMap.put(c, charMap.get(c) - 1);
                if (charMap.get(c) == requiredMap.get(c) - 1)
                    totalLength -= 1;
            }
        }
    }

    public int numItems() {
        return charMap.size();
    }

    public int getCount(Character c) {
        return charMap.get(c);
    }

    public int totalLength() {
        return this.totalLength;
    }

    public boolean requires(Character c) {
        return requiredMap.containsKey(c);
    }

    public int numCharRequired() {
        return requiredMap.size();
    }

    public boolean enough() {
        return totalLength == requiredMap.size();
    }

    public boolean safeToRemove(Character c) {
        return (!requiredMap.containsKey(c)) || (charMap.containsKey(c) && charMap.get(c) > requiredMap.get(c));
    }

    public void printRequirement() {
        for (Character c : requiredMap.keySet()) {
            System.out.println(c + "_" + requiredMap.get(c));
        }
    }

    public void printContent() {
        for (Character c : charMap.keySet()) {
            System.out.println(c + "_" + charMap.get(c));
        }
    }
}


class Solution {
    public String minWindow(String s, String t) {
        SpecialMultiSet chars = new SpecialMultiSet(t);

        int last = -1;
        while (last < s.length() && !chars.enough()) {
            last += 1;
            if (last < s.length() && chars.requires(s.charAt(last)))
                chars.add(s.charAt(last));
        }
        if (last == s.length() && !chars.enough())
            return "";
        int originalLast = last;

        int i = 0;
        int[] shortestLength = new int[s.length()];
        while (last < s.length()) {

            while (i <= last && (!chars.requires(s.charAt(i)) || chars.safeToRemove(s.charAt(i)))) {
                chars.remove(s.charAt(i));
                i += 1;
            }
            shortestLength[last] = last - i + 1;
            last += 1;
            if (last < s.length() && chars.requires(s.charAt(last)))
                chars.add(s.charAt(last));
        }


        int start = originalLast - shortestLength[originalLast] + 1;
        int end = originalLast;
        for (i = originalLast; i < shortestLength.length; i++) {
            if (shortestLength[i] < end - start + 1) {
                end = i;
                start = i - shortestLength[i] + 1;
            }
        }
        return s.substring(start, end + 1);
    }
}
