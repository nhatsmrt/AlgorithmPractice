class Solution {

    class TaskComparator implements Comparator<Character> {
        Map<Character, Integer> taskCount;

        public TaskComparator(Map<Character, Integer> taskCount) {
            this.taskCount = taskCount;
        }

        public int compare(Character task1, Character task2) {
            return -Integer.compare(taskCount.get(task1), taskCount.get(task2));
        }
    }

    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> taskCount = new HashMap<Character, Integer>();
        Queue<Character> taskQueue = new LinkedList<Character>();

        for (char task : tasks) {
            if (!taskCount.containsKey(task))
                taskCount.put(task, 0);
            taskCount.put(task, taskCount.get(task) + 1);
        }

        PriorityQueue<Character> taskPriority = new PriorityQueue<Character>(
            new TaskComparator(taskCount)
        );

        for (Character task : taskCount.keySet())
            taskPriority.add(task);

        int ret = 0;
        while (!taskCount.isEmpty()) {
            if (taskQueue.size() == n + 1) {
                Character task = taskQueue.remove();
                if (taskCount.containsKey(task))
                    taskPriority.add(task);
            }

            int maxCount = 0;
            char nextTask = 'i';

            if (!taskPriority.isEmpty())
                nextTask = taskPriority.poll();

            taskQueue.add(nextTask);
            if (nextTask != 'i') {
                if (taskCount.get(nextTask) == 1)
                    taskCount.remove(nextTask);
                else
                    taskCount.put(nextTask, taskCount.get(nextTask) - 1);
            }
            ret += 1;
        }

        return ret;
    }
}
