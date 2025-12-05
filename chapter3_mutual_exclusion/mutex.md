# Concurrent Access and Critical Sections    
# 并发访问与临界区  
  
When multiple threads concurrently read and write to a shared resource, that can lead to incorrect behavior, such as a data race.    
当多个线程同时读写一个共享资源时，可能会导致不正确的行为，比如数据竞争。  
  
This issue can be mitigated by identifying and protecting critical sections of code.    
可以通过识别并保护代码中的临界区来缓解这个问题。  
  
## Critical sections    
## 临界区  
  
A critical section is a part of a program that accesses a shared resource (for example, a data structure in memory).    
临界区是程序中访问共享资源（例如内存中的数据结构）的部分。  
  
The program may not function correctly if multiple threads access the critical section simultaneously.    
如果多个线程同时访问临界区，程序可能无法正常运行。  
  
Critical sections need protection to ensure only one thread or process can execute that code section at a time.    
临界区需要保护，以确保每次只有一个线程或进程能够执行该代码段。  
  
Barron and Olivia demonstrate a critical section with their shared shopping list, where incrementing a value is a three-step process: read, modify, and write back; those three steps form a critical section that needs to be executed by each thread as an uninterrupted action.    
Barron 和 Olivia 用他们的共享购物清单演示了临界区，其中递增一个值包含三个步骤：读取、修改和写回；这三步构成了一个临界区，需要由每个线程作为一个不可中断的动作来执行。  
  
## Mutex (mutual exclusion)    
## 互斥锁（互斥）  
  
A mutex, also known as a lock, is a mechanism to prevent simultaneous access to shared resources.    
互斥锁，也叫锁，是防止同时访问共享资源的一种机制。  
  
Only one thread can possess the mutex at a time, forcing threads to take turns accessing the shared resource.    
一次只有一个线程能够拥有互斥锁，强制线程轮流访问共享资源。  
  
The process involves acquiring the lock, executing the critical section, and then releasing the lock.    
这个过程包括获取锁、执行临界区代码，然后释放锁。  
  
## Atomic operations    
## 原子操作  
  
Acquiring a lock is an atomic operation, meaning it executes as a single, indivisible action.    
获取锁是一个原子操作，也就是说它是一次性、不可分割的动作。  
  
Atomic operations appear instantaneous to the rest of the system and are uninterruptible.    
对系统的其他部分来说，原子操作看起来是瞬时完成且不可中断的。  
  
## Thread blocking    
## 线程阻塞  
  
Threads attempting to acquire a lock that's already held by another thread will block (wait) until it becomes available.    
尝试获取已被其他线程持有的锁的线程会被阻塞（等待），直到锁可用为止。  
  
## Best Practices    
## 最佳实践  
  
It's crucial to keep the code protected by a mutex as short as possible to prevent threads from getting stuck waiting.    
必须尽量缩短受互斥锁保护的代码，以防止线程长时间等待。  
  
Operations that don't require the shared resource should be performed outside the critical section to improve efficiency.    
不需要访问共享资源的操作应在临界区外执行，以提高效率。  