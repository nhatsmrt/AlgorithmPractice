#include <pthread.h>
#include <semaphore.h>

class H2O {
public:
    H2O() {
        pthread_barrier_init(&barrier_all, NULL, 3);
        sem_init(&semaphore_h, 0, 2);
        sem_init(&semaphore_o, 0, 1);
    }

    void hydrogen(function<void()> releaseHydrogen) {

        // releaseHydrogen() outputs "H". Do not change or remove this line.
        sem_wait(&semaphore_h);
        pthread_barrier_wait(&barrier_all);
        releaseHydrogen();
        sem_post(&semaphore_h);
    }

    void oxygen(function<void()> releaseOxygen) {

        // releaseOxygen() outputs "O". Do not change or remove this line.
        sem_wait(&semaphore_o);
        pthread_barrier_wait(&barrier_all);
        releaseOxygen();
        sem_post(&semaphore_o);
    }

private:
    pthread_barrier_t barrier_all;
    sem_t semaphore_h;
    sem_t semaphore_o;
};
