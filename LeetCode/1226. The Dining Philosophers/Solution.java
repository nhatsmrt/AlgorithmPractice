class DiningPhilosophers {
    private Object[] forkLocks;

    public DiningPhilosophers() {
        forkLocks = new Object[5];
        for (int i = 0; i < 5; i++)
            forkLocks[i] = new Object();
    }

    // call the run() method of any runnable to execute its code
    // By convention, the ith philosopher has ith fork and (i + 1) % 5 fork
    public void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {
        int right = (philosopher + 1) % 5;
        int left = philosopher;

        Object firstLock = forkLocks[Math.min(left, right)];
        Object secondLock = forkLocks[Math.max(left, right)];

        synchronized(firstLock) {
            synchronized(secondLock) {
                pickLeftFork.run();
                pickRightFork.run();
                eat.run();
                putRightFork.run();
                putLeftFork.run();
            }
        }
    }
}
