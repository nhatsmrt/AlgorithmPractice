class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        List<Pair> distList = new ArrayList<Pair>();
        for (int i = 0; i < workers.length; i++) {
            for (int j = 0; j < bikes.length; j++)
                distList.add(new Pair(i, j, manhatDist(workers[i], bikes[j])));
        }
        PriorityQueue<Pair> distances = new PriorityQueue<Pair>(distList);

        int[] ret = new int[workers.length];
        Set<Integer> assignedWorker = new HashSet<Integer>();
        Set<Integer> assignedBike = new HashSet<Integer>();

        while (!distances.isEmpty()) {
            while (
                !distances.isEmpty() &&
                (assignedWorker.contains(distances.peek().worker) ||
                assignedBike.contains(distances.peek().bike))
            )
                distances.poll();

            if (!distances.isEmpty()) {
                Pair dist = distances.poll();
                ret[dist.worker] = dist.bike;
                assignedWorker.add(dist.worker);
                assignedBike.add(dist.bike);
            }
        }

        return ret;
    }

    private class Pair implements Comparable<Pair> {
        int worker;
        int bike;
        int distance;

        public Pair(int worker, int bike, int distance) {
            this.worker = worker;
            this.bike = bike;
            this.distance = distance;
        }

        public int compareTo(Pair other) {
            if (distance != other.distance)
                return Integer.compare(distance, other.distance);
            if (worker != other.worker)
                return Integer.compare(worker, other.worker);
            return Integer.compare(bike, other.bike);
        }
    }

    private int manhatDist(int[] worker, int[] bike) {
        return Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
    }
}
