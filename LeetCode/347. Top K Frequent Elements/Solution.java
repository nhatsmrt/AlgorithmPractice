class FrequencyComparator implements Comparator<Map.Entry<Integer, Integer>> {
        public int compare(Map.Entry<Integer, Integer> e1, Map.Entry<Integer, Integer> e2) {
            return -e1.getValue().compareTo(e2.getValue());
        }
}

class Solution {

    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<Integer, Integer>();
        List<Integer> mostFrequentList = new ArrayList<Integer>();
        int size = nums.length;

        for (int i = 0; i < size; i++) {
            if (frequencyMap.containsKey(nums[i])) {
                frequencyMap.put(nums[i], frequencyMap.get(nums[i]) + 1);
            }
            else
                frequencyMap.put(nums[i], 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> frequencyQueue =
            new PriorityQueue<Map.Entry<Integer, Integer>> (size, new FrequencyComparator());
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            frequencyQueue.add(entry);
        }

        for (int i = 0; i < k; i++) {
            mostFrequentList.add(frequencyQueue.poll().getKey());
        }

        return mostFrequentList;
    }
}
