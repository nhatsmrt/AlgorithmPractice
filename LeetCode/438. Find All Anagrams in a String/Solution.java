class Multiset {
    private int[] data;
    private Set<Character> allowed;
    private int checker;

    public Multiset(String p) {
        allowed = new HashSet<>();
        data = new int[26];

        for (int i = 0; i < p.length(); i++) {
            char c = p.charAt(i);
            allowed.add(c);
            add(c);
        }
    }

    public void add(Character c) {
        if (allowed.contains(c)) {
            int ind = getInd(c);
            int prevCnt = data[ind];
            int newCnt = prevCnt + 1;

            data[ind] = newCnt;
            checker += newCnt * newCnt - prevCnt * prevCnt;
        }
    }

    public void remove(Character c) {
        if (allowed.contains(c)) {
            // size -= 1;
            int ind = getInd(c);
            int prevCnt = data[ind];
            int newCnt = prevCnt - 1;

            data[ind] = newCnt;
            checker += newCnt * newCnt - prevCnt * prevCnt;
        }
    }

    private int getInd(char c) {
        return (int) (c - 'a');
    }

    public boolean isEmpty() {
        return checker == 0;
    }
}


class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ret = new ArrayList<>();
        if (p.length() > s.length())
            return ret;

        Multiset current = new Multiset(p);
        for (int i = 0; i < p.length() - 1; i++)
            current.remove(s.charAt(i));

        for (int i = p.length() - 1; i < s.length(); i++) {
            current.remove(s.charAt(i));
            if (current.isEmpty())
                ret.add(i - p.length() + 1);
            current.add(s.charAt(i - p.length() + 1));
        }

        return ret;
    }
}
