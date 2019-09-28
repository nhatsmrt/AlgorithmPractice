class ZeroEvenOdd {
    private int n;
    private int cur;
    private boolean printZero;

    public ZeroEvenOdd(int n) {
        this.n = n;
        printZero = true;
        cur = 1;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        synchronized (this) {
            while (!printZero) {
                this.notifyAll();
                this.wait();
            }


            printNumber.accept(0);
            printZero = false;
            if (cur < n)
                zero(printNumber);
            this.notifyAll();
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        synchronized(this) {
            if (n > 1) {
                while(printZero || cur % 2 != 0) {
                    this.notifyAll();
                    this.wait();
                }

                printNumber.accept(cur);
                printZero = true;
                cur += 1;
                if (cur < n / 2 * 2)
                    even(printNumber);
                this.notifyAll();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        synchronized(this) {
            while (printZero || cur % 2 != 1) {
                this.notifyAll();
                this.wait();
            }

            printNumber.accept(cur);
            printZero = true;
            cur += 1;
            if (cur < (n - 1) / 2 * 2 + 1)
                odd(printNumber);
            this.notifyAll();
        }
    }
}
