class NFA {
    private StringBuilder states;
    private Map<Integer, Set<Integer>> adjMap;

    public NFA(String re) {
        states = new StringBuilder();
        states.append('(');


        for (int i = 0; i < re.length(); i++) {
            if (re.charAt(i) != '*')
                states.append(re.charAt(i));
            else if (i == 0 || re.charAt(i - 1) != '*')
                states.append('*');
        }
        states.append(')');
        states.append('$');
        buildEpsGraph();

    }

    private void buildEpsGraph() {
        adjMap = new HashMap<Integer, Set<Integer>>();
        for (int i = 0; i < states.length(); i++)
            adjMap.put(i, new HashSet<Integer>());

        for (int i = 0; i < states.length(); i++) {
            if (states.charAt(i) == '(' || states.charAt(i) == ')')
                adjMap.get(i).add(i + 1);
            if (states.charAt(i) == '*') {
                adjMap.get(i).add(i);

                if (i < states.length() - 1)
                    adjMap.get(i).add(i + 1);
            }
        }
    }

    public boolean match(String text) {
        Set<Integer> candidates = new HashSet<Integer>();
        candidates.add(0);
        candidates = epsDFS(candidates);

        for (int i = 0; i < text.length(); i++) {
            Set<Integer> match = new HashSet<Integer>();
            for (Integer state : candidates) {
                if (
                    states.charAt(state) == text.charAt(i) ||
                    states.charAt(state) == '?'
                )
                    match.add(state + 1);
                else if (states.charAt(state) == '*') {
                    match.add(state);
                }

            }
            match = epsDFS(match);
            candidates = match;
        }

        return candidates.contains(states.length() - 1);
    }

    private Set<Integer> epsDFS(Set<Integer> states) {
        Set<Integer> ret = new HashSet<Integer>();
        Stack<Integer> traverse = new Stack<Integer>();
        for (Integer state : states) {
            traverse.push(state);
            ret.add(state);
        }

        while (!traverse.isEmpty()) {
            Integer state = traverse.pop();
            for (Integer next : adjMap.get(state)) {
                if (!ret.contains(next)) {
                    traverse.push(next);
                    ret.add(next);
                }
            }
        }

        return ret;
    }
}


class Solution {
    public boolean isMatch(String s, String p) {
        NFA nfa = new NFA(p);
        return nfa.match(s);
    }
}
