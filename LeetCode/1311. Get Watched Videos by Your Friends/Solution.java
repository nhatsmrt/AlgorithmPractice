class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        // Time Complexity: O(V + E + Q log Q)
        // Space Complexity: O(V + E + Q)

        List<Integer> curLevel = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();

        curLevel.add(id);
        visited.add(id);

        for (int i = 0; i < level; i++) {
            List<Integer> newLevel = new ArrayList<>();

            for (int per : curLevel) {
                for (int friend : friends[per]) {
                    if (!visited.contains(friend)) {
                        visited.add(friend);
                        newLevel.add(friend);
                    }
                }
            }

            curLevel = newLevel;
        }

        List<String> ret = new ArrayList<>();
        Map<String, Integer> freq = new HashMap<>();

        for (int per : curLevel) {
            for (String vid : watchedVideos.get(per)) {
                if (!freq.containsKey(vid)) {
                    ret.add(vid);
                }

                freq.put(vid, freq.getOrDefault(vid, 0) + 1);
            }
        }

        Collections.sort(ret, new Comparator<String>() {
            @Override
            public int compare(String vid1, String vid2) {
                if (freq.get(vid1) != freq.get(vid2)) {
                    return freq.get(vid1) - freq.get(vid2);
                }

                return vid1.compareTo(vid2);
            }
        });

        return ret;
    }
}
