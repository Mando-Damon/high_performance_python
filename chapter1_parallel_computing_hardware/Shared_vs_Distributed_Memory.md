# Shared vs. Distributed Memory（共享内存 vs. 分布式内存）  
  
Memory organization and access are crucial factors in parallel computing performance.    
内存组织和访问是并行计算性能的关键因素。  
  
Even with numerous processors, inefficient memory access can negate potential gains because computer memory typically operates slower than processors, creating potential bottlenecks.    
即使有大量处理器，低效的内存访问也会抵消潜在收益，因为计算机内存通常比处理器慢，从而形成潜在的瓶颈。  
  
Shared memory and distributed memory are the two main memory architectures that support different use cases for parallel computing.    
共享内存和分布式内存是并行计算支持不同应用场景的两种主要内存架构。  
  
---  
  
## Shared Memory Architecture（共享内存架构）  
  
All processors access a global memory address space, and changes made by one processor to that memory are visible to all others.    
所有处理器都能访问全局内存地址空间，一个处理器对内存的修改对其他处理器都是可见的。  
  
### Types of shared memory systems（共享内存系统的类型）  
  
1. Uniform memory access (UMA)（一致内存访问）  
    - Processors have equal access speed to memory    
      处理器访问内存的速度相同  
    - Symmetric multiprocessing (SMP) is a common UMA architecture    
      对称多处理（SMP）是常见的UMA架构  
    - Modern multicore processors use SMP architecture    
      现代多核处理器采用SMP架构  
  
2. Non-uniform memory access (NUMA)（非一致内存访问）  
    - Often created by connecting multiple SMP systems    
      通常通过连接多个SMP系统实现  
    - Processors have varying access speeds to different memory parts    
      处理器访问不同部分内存的速度不同  
    - All processors can still access all memory    
      所有处理器仍可访问全部内存  
  
### Caches in shared memory systems（共享内存系统中的缓存）  
  
- Each core typically has its own fast, local cache    
  每个核心通常都有自己的快速本地缓存  
- Cache coherency becomes a challenge when updating shared memory    
  更新共享内存时，缓存一致性成为一个挑战  
- Hardware handles cache coherency in multicore processors    
  多核处理器中由硬件处理缓存一致性  
  
### Advantages and disadvantages（优缺点）  
  
- Easier for programming due to simple data sharing    
  由于数据共享简单，编程更容易  
- May not scale well due to increased bus traffic and synchronization needs    
  由于总线流量和同步需求增加，扩展性可能较差  
  
---  
  
## Distributed Memory Architecture（分布式内存架构）  
  
Each processor has its own local memory and address space; no global address space exists, and processors are connected through a network.    
每个处理器都有自己的本地内存和地址空间，不存在全局地址空间，处理器通过网络连接。  
  
### Key characteristics（主要特征）  
  
- Changes in one processor's memory are not automatically reflected in others    
  一个处理器内存的变化不会自动反映到其他处理器  
- Programmers must explicitly define data communication between nodes    
  程序员必须明确定义节点间的数据通信  
  
### Advantages and disadvantages（优缺点）  
  
- Highly scalable: adding processors increases both processing power and memory    
  高度可扩展：增加处理器同时提升计算能力和内存容量  
- Cost-effective using commodity hardware    
  利用普通硬件，性价比高  
- Communication between nodes can be challenging to program    
  节点间通信编程难度较高  