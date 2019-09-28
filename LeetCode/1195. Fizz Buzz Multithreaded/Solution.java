class FizzBuzz {
    private int n;
    private int count;
    private int max3;
    private int max5;
    private int max15;
    private int max;

    public FizzBuzz(int n) {
        this.n = n;
        count = 1;

        max15 = (n / 15) * 15;
        max3 = (n / 3) * 3;
        max5 = (n / 5) * 5;

        if (max3 % 5 == 0)
            max3 -= 3;

        if (max5 % 3 == 0)
            max5 -= 5;

        max = n;
        while (max == max3 || max == max5 || max == max15)
            max -= 1;

    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        synchronized (this) {
            if (max3 > 0) {
                while (count % 3 != 0 || count % 5 == 0) {
                    this.notifyAll();
                    this.wait();
                }

                printFizz.run();
                count += 1;
                if (count < max3)
                    fizz(printFizz);
                this.notifyAll();
            }
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        synchronized (this) {
            if (max5 > 0) {
                while (count % 3 == 0 || count % 5 != 0) {
                    this.notifyAll();
                    this.wait();
                }

                printBuzz.run();
                count += 1;
                if (count < max5)
                    buzz(printBuzz);
                this.notifyAll();
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        synchronized (this) {
            if (max15 > 0) {
                while (count % 15 != 0) {
                    this.notifyAll();
                    this.wait();
                }


                printFizzBuzz.run();
                count += 1;
                if (count < max15)
                    fizzbuzz(printFizzBuzz);
                this.notifyAll();
            }
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        synchronized (this) {
            while (count % 3 == 0 || count % 5 == 0) {
                this.notifyAll();
                this.wait();
            }


            printNumber.accept(count);
            count += 1;
            if (count <= max)
                number(printNumber);
            this.notifyAll();

        }
    }

}
