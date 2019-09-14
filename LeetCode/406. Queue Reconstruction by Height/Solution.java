class Solution {
    public int[][] reconstructQueue(int[][] people) {
        if (people.length == 0)
            return new int[0][0];
        Arrays.sort(people, new Comparator<int[]>() {
            public int compare(int[] height1, int[] height2) {
                if (height1[0] != height2[0])
                    return Integer.compare(height1[0], height2[0]);
                else
                    return -Integer.compare(height1[1], height2[1]);
            }
        });

        int[][] ret = new int[people.length][people[0].length];
        TreeSet<Integer> indicesRemained = new TreeSet<Integer>();
        for (int i = 0; i < people.length; i++)
            indicesRemained.add(i);

        for (int i = 0; i < people.length; i++) {

            Iterator<Integer> it = indicesRemained.iterator();
            for (int j = 0; j < people[i][1]; j++)
                it.next();

            int ind = it.next();
            it.remove();

            ret[ind] = people[i];
        }
        return ret;
    }
}
