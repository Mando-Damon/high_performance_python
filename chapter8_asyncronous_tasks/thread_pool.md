# Challenges with Creating Many Threads    
# 创建大量线程的挑战  
  
Barron and Olivia introduce the concept of running asynchronous tasks in parallel using a cooking analogy where they each represent independent threads (or processes) chopping different vegetables representing parallel tasks.    
Barron 和 Olivia 用烹饪类比解释并行异步任务：他们各自像独立线程（或进程）一样切不同的蔬菜，代表并行任务。  
  
---  
  
## Thread Creation Overhead    
## 线程创建的开销  
  
- As more tasks (vegetables) are added, they can spawn a new thread for each one    
  随着任务（蔬菜）增多，可以为每个任务创建一个新线程  
- Creating a new thread for each task can lead to inefficiencies because thread creation incurs overhead in terms of processor time and memory usage    
  为每个任务单独创建线程会导致效率低下，因为线程创建会消耗处理器时间和内存  
  
---  
  
## Thread Pools    
## 线程池  
  
Thread pools can be a more efficient alternative to creating individual threads for each task.    
线程池是比为每个任务创建新线程更高效的选择。  
  
- Thread pools maintain a small collection of worker threads that can be reused to execute multiple tasks    
  线程池维护少量可复用的工作线程，用于执行多个任务  
- Submitting tasks to a thread pool is analogous to adding items to a to-do list for worker threads    
  将任务提交到线程池就像把任务添加到工作线程的待办清单  
  
---  
  
## Benefits of Thread Pools    
## 线程池的优势  
  
- Reusing threads from a pool overcomes the overhead of creating new threads for each task    
  重用线程池中的线程，避免每次任务都新建线程的开销  
- Thread pools are especially advantageous when the task execution time is less than thread creation time    
  当任务执行时间短于线程创建时间时，线程池优势明显  
- Using preexisting threads in a pool can make programs more responsive by eliminating the delay of thread creation    
  使用线程池中的预先存在线程可消除线程创建延迟，提高程序响应速度  