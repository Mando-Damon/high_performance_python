# Semaphores    
# 信号量  
  
Semaphores are a synchronization mechanism used to control access to shared resources.    
信号量是一种用于控制对共享资源访问的同步机制。  
  
Unlike locks or mutexes, semaphores can allow multiple threads to access a resource simultaneously.    
与锁或互斥锁不同，信号量可以允许多个线程同时访问资源。  
  
Semaphores include a counter to track how many times they've been acquired or released.    
信号量包含一个计数器，用于跟踪其被获取或释放的次数。  
  
---  
  
## Semaphore Functionality    
## 信号量的工作原理  
  
- Threads can acquire a semaphore when its count is positive, decrementing the counter    
  当信号量计数为正时，线程可以获取信号量，并将计数减一  
- If the counter reaches zero, threads attempting to acquire the semaphore are blocked and queued    
  如果计数器为零，尝试获取信号量的线程会被阻塞并排队  
- Threads release the semaphore when done, incrementing the counter and potentially signaling waiting threads    
  线程使用完资源后释放信号量，计数加一，并可能唤醒等待的线程  
  
---  
  
## Types of Semaphores    
## 信号量的类型  
  
### Counting Semaphore    
### 计数信号量  
  
- Counting semaphores can have values of 0, 1, 2, 3, etc., representing the number of available resources    
  计数信号量的取值可以为 0、1、2、3 等，表示可用资源的数量  
- They can be used to manage access to a limited pool of resources, such as database connections or items in a queue    
  常用于管理有限资源池的访问，如数据库连接或队列中的项目  
  
**Example:**    
Barron, Olivia, and Steve demonstrate a counting semaphore using a two-port phone charger:    
Barron、Olivia 和 Steve 用双口充电器演示计数信号量：  
  
- The number of available ports represents a semaphore with an initial value of two    
  可用插口数量即为初始值为 2 的信号量  
- As devices are plugged in, the semaphore value is decremented; when unplugged, the semaphore count is incremented    
  插入设备时信号量减一，拔出设备时信号量加一  
- When all ports are in use (semaphore = 0), additional threads must wait    
  当所有插口被占用（信号量为 0）时，其他线程必须等待  
  
### Binary Semaphore    
### 二值信号量  
  
- Binary semaphores are restricted to one of two values: 0 (locked) or 1 (unlocked)    
  二值信号量只能取 0（锁定）或 1（解锁）  
- They are similar to mutexes, but any thread can release a semaphore, not just the one that acquired it    
  类似于互斥锁，但任何线程都可以释放信号量，而不仅仅是持有者  
  
---  
  
## Key Advantages of Semaphores    
## 信号量的主要优点  
  
- Flexibility in allowing multiple threads to access resources simultaneously    
  灵活地允许多个线程同时访问资源  
- Ability to function as a signaling mechanism between threads    
  可以作为线程间的信号传递机制  
- Versatility in managing various types of resource pools and synchronization scenarios    
  可用于管理多种资源池和不同的同步场景  