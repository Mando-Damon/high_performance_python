# Thread Lifecycle and States（线程生命周期与状态）  
  
A new process begins with a single "main thread" that can spawn additional child threads    
一个新进程以单个“主线程”开始，主线程可以创建其他子线程  
  
Child threads execute independently within the same process and can spawn their own children    
子线程在同一进程内独立执行，也可以创建自己的子线程  
  
Threads notify their parent upon completion, with the main thread usually finishing last    
线程完成时会通知其父线程，主线程通常最后结束  
  
## Thread States（线程状态）  
  
Threads transition through four main states during their lifecycle:    
在线程生命周期中，线程会经历四个主要状态：  
  
### NEW（新建）  
  
- The NEW thread has been created but is not yet running    
  新建线程已创建但尚未运行  
- It doesn't consume CPU resources at this stage    
  此阶段不会占用CPU资源  
- The thread is assigned a function to execute    
  线程被分配一个要执行的函数  
  
### RUNNABLE（可运行）  
  
- The operating system can schedule the RUNNABLE thread to execute on a processor    
  操作系统可以调度可运行线程在处理器上执行  
- It may be swapped with other threads through context switches    
  可通过上下文切换与其他线程交换运行  
  
### BLOCKED（阻塞）  
  
- The thread enters the BLOCKED state when waiting for an event or resource    
  线程在等待事件或资源时进入阻塞状态  
- It doesn't use CPU resources while blocked    
  阻塞时不占用CPU资源  
- The thread returns to the RUNNABLE state when the required condition is met    
  条件满足后线程回到可运行状态  
  
### TERMINATED（终止）  
  
- The thread enters the TERMINATED state upon completing execution or being abnormally aborted    
  线程执行完毕或异常终止后进入终止状态  
- It notifies its parent thread before termination    
  终止前会通知父线程  
  
## Key Concepts（关键概念）  
  
- Threads can create child threads to perform parallel tasks    
  线程可以创建子线程以执行并行任务  
- The join() method allows a parent thread to wait for a child thread to complete    
  join()方法允许父线程等待子线程完成  
- Different programming languages may use varying terminology for thread states    
  不同编程语言可能用不同术语描述线程状态  
- Efficient thread management is crucial for concurrent and parallel computing    
  高效的线程管理对并发和并行计算至关重要  