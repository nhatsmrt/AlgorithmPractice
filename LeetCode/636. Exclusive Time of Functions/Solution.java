class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] ret = new int[n];

        Stack<Integer> stack = new Stack<Integer>();
        int prevTime = -1;
        boolean isLastStart = true;

        for (String log : logs) {
            String[] infos = getInfo(log);
            int id = new Integer(infos[0]);
            if (stack.isEmpty()) {
                prevTime = new Integer(infos[infos.length - 1]);
                stack.push(id);
                isLastStart = true;
            }
            else {
                int curTime = new Integer(infos[infos.length - 1]);
                ret[stack.peek()] += curTime - prevTime;

                if (infos[1].equals("start")) {
                    if (!isLastStart)
                        ret[stack.peek()] -= 1;

                    isLastStart = true;
                    stack.push(id);
                }
                else {
                    if (isLastStart)
                        ret[stack.peek()] += 1;

                    isLastStart = false;
                    stack.pop();
                }

                prevTime = curTime;
            }
        }

        return ret;
    }

    private String[] getInfo(String info) {
        return info.split(":");
    }
}
