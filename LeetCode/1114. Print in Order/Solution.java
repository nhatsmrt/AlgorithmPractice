class Foo {
    private int count;

    public Foo() {
        count = 0;
    }

    public void first(Runnable printFirst) throws InterruptedException {

        // printFirst.run() outputs "first". Do not change or remove this line.
        synchronized (this) {
            printFirst.run();
            count += 1;
            this.notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {

        // printSecond.run() outputs "second". Do not change or remove this line.

        synchronized (this) {
            while (count != 1)
                this.wait();
            printSecond.run();
            count += 1;
            this.notifyAll();
        }

    }

    public void third(Runnable printThird) throws InterruptedException {

        // printThird.run() outputs "third". Do not change or remove this line.

        synchronized (this) {
            while (count != 2)
                this.wait();
            printThird.run();
        }

    }
}
