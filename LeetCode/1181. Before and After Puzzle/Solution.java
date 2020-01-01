class Solution {
    public List<String> beforeAndAfterPuzzles(String[] phrases) {
        Set<String> ret = new TreeSet<>();
        List<List<String>> processedData = new ArrayList<>();
        Map<String, List<Integer>> startsWith = new HashMap<>();
        Map<String, List<Integer>> endsWith = new HashMap<>();

        for (String phrase : phrases) {
            String[] words = phrase.split(" ");

            if (!startsWith.containsKey(words[0]))
                startsWith.put(words[0], new ArrayList<>());
            if (!endsWith.containsKey(words[words.length - 1]))
                endsWith.put(words[words.length - 1], new ArrayList<>());

            startsWith.get(words[0]).add(processedData.size());
            endsWith.get(words[words.length - 1]).add(processedData.size());

            processedData.add(Arrays.asList(words));
        }

        for (String end : endsWith.keySet()) {
            if (startsWith.containsKey(end)) {
                for (Integer i : endsWith.get(end)) {
                    for (Integer j : startsWith.get(end)) {
                        if (!i.equals(j)) {
                            StringBuilder str = new StringBuilder();
                            for (int k = 0; k < processedData.get(i).size() - 1; k++) {
                                str.append(processedData.get(i).get(k));
                                str.append(' ');
                            }

                            str.append(end);

                            for (int k = 1; k < processedData.get(j).size(); k++) {
                                str.append(' ');
                                str.append(processedData.get(j).get(k));
                            }

                            ret.add(str.toString());
                        }
                    }
                }
            }
        }

        return new ArrayList<>(ret);
    }
}
