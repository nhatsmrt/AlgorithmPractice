class Solution {
    HashMap<String, List<List<Integer>>> combinationMap = new HashMap<String, List<List<Integer>>>();
    public List<List<Integer>> cloneList(List<List<Integer>> list) {
        List<List<Integer>> newList = new ArrayList<List<Integer>>();
            for (List<Integer> sublist : list) {
                List<Integer> newSublist = new ArrayList<Integer>();
                for (Integer num : sublist)
                    newSublist.add(num.intValue());
                newList.add(newSublist);
            }
        return newList;
    }
    public List<List<Integer>> combine(int n, int k) {
        String key = Integer.toString(n) + "_" + Integer.toString(k);
        List<List<Integer>> ret = new ArrayList<List<Integer>>();

        if (combinationMap.containsKey(key))
            return combinationMap.get(key);

        else if (k == 0 || n == 0) {
            List<Integer> combination = new ArrayList<Integer>();
            ret.add(combination);
            combinationMap.put(key, ret);
            return ret;

        }

        else if (k == 1) {
            List<Integer> combination;
            for (int i = 1; i <= n; i++) {
                combination = new ArrayList<Integer>();
                combination.add(i);
                ret.add(combination);
            }
            combinationMap.put(key, ret);
            return ret;
        }

        else if (k == n) {
            List<Integer> combination = new ArrayList<Integer>();
            for (int i = 1; i <= n; i++) {
                combination.add(i);
            }
            ret.add(combination);
            combinationMap.put(key, ret);
            return ret;
        }

        else if (n == 1) {
            List<Integer> combination = new ArrayList<Integer>();
            combination.add(1);
            ret.add(combination);

            combinationMap.put(key, ret);
            return ret;
        }

        else {
            List<List<Integer>> combinationList1 = cloneList(combine(n - 1, k - 1));
            List<List<Integer>> combinationList2 = cloneList(combine(n - 1, k));


            for (List<Integer> combination : combinationList1)
                combination.add(n);

            ret.addAll(combinationList1);
            ret.addAll(combinationList2);

            combinationMap.put(key, ret);
            return ret;
        }
    }
}
