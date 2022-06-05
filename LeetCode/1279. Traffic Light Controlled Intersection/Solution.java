class TrafficLight {
    private List<List<Integer>> cars;
    private int cur_greened_direction = 0;

    private Object participateLock = new Object();
    private Object greenLock = new Object();

    public TrafficLight() {
        cars = new ArrayList<>();
        cars.add(new ArrayList<Integer>());
        cars.add(new ArrayList<Integer>());
    }

    public void carArrived(
        int carId,           // ID of the car
        int roadId,          // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        int direction,       // Direction of the car
        Runnable turnGreen,  // Use turnGreen.run() to turn light to green on current road
        Runnable crossCar    // Use crossCar.run() to make car cross the intersection
    ) {
        // NOTE: the test case is wrong - it only accepts a single ordering...
        try {

            int direction_id = (direction - 1) / 2;
            int other_direction = (direction_id + 1) % 2;

            synchronized(participateLock) {

                // guarded suspension pattern:
                while (cars.get(other_direction).size() > 0) {
                    participateLock.wait();
                }

                // added to traverse list:
                cars.get(direction_id).add(carId);
            }

            synchronized(greenLock) {
                if (cur_greened_direction != direction_id) {
                    cur_greened_direction = direction_id;
                    turnGreen.run();
                }
            }

            // safe to go!
            crossCar.run();

            // release!
            synchronized(participateLock) {
                cars.get(direction_id).remove(cars.get(direction_id).indexOf(carId));
                participateLock.notifyAll();
            }
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
}
