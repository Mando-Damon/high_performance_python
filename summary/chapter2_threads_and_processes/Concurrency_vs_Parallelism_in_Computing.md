# Concurrency versus Parallelism in Computing（计算中的并发与并行）  
  
Concurrency refers to the ability of a program to be broken into independent parts that can be executed out of order without affecting the final result.    
并发是指程序能够被划分为若干独立部分，这些部分可以无序执行且不影响最终结果。  
  
It focuses on how a program is structured and composed of independently executing processes.    
它关注的是程序的结构，以及如何由独立执行的进程组成。  
  
Concurrent execution does not necessarily mean parallel execution.    
并发执行不一定意味着并行执行。  
  
Barron and Olivia use a salad-making analogy to explain concurrency and parallelism.    
Barron和Olivia用制作沙拉的类比来解释并发和并行。  
  
They are two tasks (chopping tomatoes and slicing cucumbers) representing concurrent processes.    
他们的两个任务（切番茄和切黄瓜）代表了并发进程。  
  
Their single knife represents a single-core processor, where tasks must take turns executing.    
一把刀代表单核处理器，任务必须轮流执行。  
  
## Concurrent Execution（并发执行）  
  
Concurrent processes overlap in time but may not execute simultaneously on a single processor    
并发进程在时间上有重叠，但在单处理器上可能并不会同时执行  
  
Rapid task-switching can create an illusion of simultaneous execution, but it's not true parallelism    
快速任务切换可能造成同时执行的假象，但这并不是真正的并行  
  
## Parallel Execution（并行执行）  
  
Parallel execution requires parallel hardware, such as multiple processors or cores    
并行执行需要并行硬件，比如多处理器或多核心  
  
Olivia introduces a second knife and cutting board (processor) to demonstrate true parallel execution    
Olivia引入了第二把刀和切菜板（处理器）来展示真正的并行执行  
  
Parallel execution allows multiple tasks to be performed simultaneously, potentially speeding up the overall process    
并行执行可以让多个任务同时进行，有可能加快整体进程  
  
## Forms of Parallel Hardware（并行硬件的形式）  
  
- Multicore processors in desktop computers and mobile devices    
  台式机和移动设备中的多核处理器  
- Graphics processing units (GPUs) with numerous specialized cores    
  拥有大量专用核心的图形处理器（GPU）  
- Computer clusters that distribute processing across multiple systems    
  计算机集群，将处理分布在多个系统之间  
  
## Key Distinctions（关键区别）  
  
- Concurrency is about program structure and dealing with multiple things at once    
  并发关注的是程序结构和同时处理多件事情  
- Parallelism involves simultaneous execution and doing multiple things at once    
  并行涉及同时执行、真正做多件事情  
- Concurrency enables potential parallel execution but doesn't guarantee it    
  并发为并行执行提供可能，但并不保证并行  
- Use Cases（使用场景）  
  - Concurrent programming is beneficial for I/O-dependent tasks like graphical user interfaces    
    并发编程适用于依赖I/O的任务，如图形用户界面  
  - Parallel processing is particularly useful for computation-intensive tasks, such as matrix multiplication    
    并行处理特别适用于计算密集型任务，比如矩阵乘法  
  
## Practical Applications（实际应用）  
  
- Device drivers for I/O devices (mouse, keyboard, and hard drive) execute concurrently but may not benefit significantly from parallelism    
  I/O设备（鼠标、键盘、硬盘）的驱动程序可以并发执行，但不一定能显著受益于并行  
- Graphical user interfaces use concurrency to maintain responsiveness during time-consuming operations    
  图形用户界面通过并发来在耗时操作期间保持响应  
- Large mathematical operations can be divided into subparts for efficient parallel processing    
  大型数学运算可以被分解为子部分，以实现高效的并行处理  