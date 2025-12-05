# Limitations of Locks and Mutexes    
# 锁与互斥锁的局限性  
  
A lock or mutex restricts multiple threads from accessing a shared resource simultaneously; however, it doesn't provide a way for threads to signal each other or synchronize actions efficiently.    
锁或互斥锁可以防止多个线程同时访问共享资源，但它们无法让线程之间高效地互相通知或同步操作。  
  
---  
  
## Condition Variables    
## 条件变量  
  
Condition variables serve as a queue for threads waiting for a specific condition to occur.    
条件变量为等待特定条件发生的线程提供了一个队列。  
  
They work in conjunction with mutexes to implement a higher-level construct called a monitor.    
条件变量与互斥锁配合使用，实现更高级的同步结构——监视器。  
  
---  
  
## Monitors    
## 监视器  
  
Monitors protect critical sections of code with mutual exclusion and provide mechanisms for threads to wait and be notified.    
监视器利用互斥保护关键代码段，并为线程提供等待和被通知的机制。  
  
Barron and Olivia describe the concept of monitors using a room analogy:    
Barron 和 Olivia 用房间类比解释监视器的概念：  
  
- The monitor is like a room containing protected procedures and shared data    
  监视器像一个房间，里面有受保护的过程和共享数据  
- The mutex acts as a lock on the door    
  互斥锁就像门锁  
- Condition variables are like waiting rooms outside the monitor    
  条件变量像房间外的等候区  
  
---  
  
## Condition Variable Operations    
## 条件变量的操作  
  
There are three main operations associated with condition variables:    
条件变量有三个主要操作：  
  
- **Wait**: Releases the mutex lock and puts the thread to sleep in a queue    
  等待：释放互斥锁，并让线程在队列中休眠  
- **Signal (notify/wake)**: Wakes up a single thread from the waiting queue    
  通知（唤醒）：唤醒等待队列中的一个线程  
- **Broadcast (notifyAll/wakeAll)**: Wakes up all threads in the waiting queue    
  广播（全部唤醒）：唤醒所有等待队列中的线程  
  
---  
  
## Practical Application    
## 实际应用  
  
One common use case for condition variables is implementing a shared queue or buffer, which typically involves:    
条件变量的常见应用之一是实现共享队列或缓冲区，通常包括：  
  
- A mutex to ensure exclusive access to the queue    
  一个互斥锁，确保对队列的独占访问  
- Two condition variables:    
  两个条件变量：    
  - One for signaling when the buffer is not full (for adding items)    
    一个用于缓冲区未满时（可添加元素）发信号  
  - Another for signaling when the buffer is not empty (for removing items)    
    另一个用于缓冲区非空时（可移除元素）发信号  
  
---  
  
## Summary    
## 总结  
  
Condition variables enable efficient thread synchronization by allowing threads to wait for specific conditions and signal each other when those conditions are met.    
条件变量通过让线程等待特定条件并在条件满足时互相通知，实现了高效的线程同步。  
  
This mechanism improves upon simple mutex-based solutions by reducing “busy-waiting” and enabling more sophisticated coordination between threads.    
这种机制比仅用互斥锁的方案更优，通过减少“忙等待”并实现更复杂的线程协作。  