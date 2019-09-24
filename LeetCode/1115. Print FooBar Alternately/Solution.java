class FooBar {
    private int n;
    private boolean foo;

    public FooBar(int n) {
        this.n = n;
        foo = true;
    }

    public void foo(Runnable printFoo) throws InterruptedException {

        for (int i = 0; i < n; i++) {

        	// printFoo.run() outputs "foo". Do not change or remove this line.
            synchronized (this) {
                while (!foo)
                    this.wait();

                printFoo.run();
                foo = false;
                this.notifyAll();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {

            // printBar.run() outputs "bar". Do not change or remove this line.
            synchronized (this) {
                while (foo)
                    this.wait();


                printBar.run();
                foo = true;
                this.notifyAll();
            }
        }
    }
}
