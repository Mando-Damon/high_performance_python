#!/usr/bin/env python3
""" Three philosophers, thinking and eating sushi """
import threading
import time

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
print_lock = threading.Lock()
sushi_count = 5000


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    sushi_eaten = 0
    while True:
        got_first = first_chopstick.acquire(timeout=0.001)
        if not got_first:
            continue
        got_second = second_chopstick.acquire(timeout=0.001)
        if not got_second:
            first_chopstick.release()
            continue
        if sushi_count > 0:
            sushi_count -= 1
            sushi_eaten += 1
            # print(name, 'took a piece! Sushi remaining:', sushi_count)
            second_chopstick.release()
            first_chopstick.release()
        else:
            second_chopstick.release()
            first_chopstick.release()
            break
        time.sleep(0.001)
    with print_lock:
        print(name, 'took', sushi_eaten, 'pieces')


if __name__ == '__main__':
    # still has starving philosophers, but at least some make progress (reducing threads, add timeout)
    threads = 10
    for thread in range(threads):
        threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Olivia', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_b)).start()
