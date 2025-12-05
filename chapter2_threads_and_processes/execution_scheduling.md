# Operating System Scheduling in Concurrent Computing（并发计算中的操作系统调度）  
  
Computers manage multiple processes and threads competing for limited processor resources.    
计算机需要管理多个进程和线程，它们竞争有限的处理器资源。  
  
The operating system's scheduler controls when different threads and processes execute on the CPU.    
操作系统的调度器控制不同线程和进程在CPU上的执行时机。  
  
## The Role of the Scheduler（调度器的作用）  
  
### Process management（进程管理）  
  
- The scheduler enables multiple programs to run concurrently on a single processor    
  调度器使多个程序能在单个处理器上并发运行  
- New processes are loaded into memory and placed in the "ready queue" when created    
  新进程被加载到内存并放入“就绪队列”  
- The scheduler cycles through ready processes, allocating CPU time for each process to execute    
  调度器轮流分配CPU时间给就绪进程执行  
  
### Multiprocessor handling（多处理器管理）  
  
- For systems with multiple processors, the OS schedules processes across all available processors to maximize resource utilization    
  对于多处理器系统，操作系统会在所有可用处理器上调度进程，以最大化资源利用率  
  
### Process execution states（进程执行状态）  
  
- Processes may run until completion, get blocked waiting for I/O events, or be swapped out after using their allocated timeshare    
  进程可能运行直到完成，因等待I/O事件而阻塞，或在用完分配的时间片后被切换出去  
  
### Context Switch（上下文切换）  
  
- Save the state of a currently running process and load the state of another process    
  保存当前运行进程的状态并加载另一个进程的状态  
- Allows multiple processes to share CPU time    
  使多个进程能够共享CPU时间  
- Context switches are not instantaneous and incur overhead    
  上下文切换不是瞬时的，会产生一定开销  
- Schedulers must balance switch frequency with performance impact    
  调度器需要在切换频率与性能影响之间做平衡  
  
## Scheduling Algorithms（调度算法）  
  
- Different operating systems use different scheduling algorithms based on their specific purposes and system requirements    
  不同操作系统根据自身目的和系统需求采用不同的调度算法  
- Some scheduling algorithms aim to maximize throughput, while others focus on minimizing latency for improved responsiveness    
  有些调度算法旨在最大化吞吐量，另一些则专注于最小化延迟以提升响应性  
- Preemptive scheduling: Can interrupt low-priority processes for high-priority ones    
  抢占式调度：可以中断低优先级进程以执行高优先级进程  
- Non-preemptive scheduling: Allows processes to run for their full allotted time once started    
  非抢占式调度：进程一旦开始可运行完整的分配时间  
  
## Key Takeaways（要点总结）  
  
- Scheduling details are typically handled by the OS "under the hood"    
  调度细节通常由操作系统在底层自动完成  
- Programmers should not assume a specific execution order or equal time allocation for threads or processes    
  程序员不应假定线程或进程有特定的执行顺序或均等的时间分配  
- Programs should be written to function correctly regardless of scheduling decisions    
  程序应确保无论调度如何都能正确运行  