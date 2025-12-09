# Communication between Parallel Tasks    
# 并行任务之间的通信  
  
---  
  
## Why is Communication Needed?    
为什么需要通信？  
  
- After dividing a problem into separate tasks, tasks often need to coordinate and share data.  
- 分解问题后，各任务常常需要协调和共享数据。  
  
---  
  
## Types of Task Communication    
## 任务通信类型  
  
### 1. Independent Tasks (独立任务)  
- Tasks do not need to share data.  
- 任务彼此独立，无需通信。  
- **Example:** Each person independently给杯蛋糕上糖霜，无需交流。  
  
### 2. Interdependent Tasks (相互依赖任务)  
- Tasks need information from others to complete their work.  
- 任务需要从其他任务获取信息才能完成工作。  
- **Example:** 制作彩虹图案的纸杯蛋糕，每个人需要知道邻近蛋糕的颜色。  
  
---  
  
## Communication Structures    
## 通信结构  
  
### 1. Point-to-Point Communication (点对点通信)  
- Direct connections between neighboring tasks.  
- 任务之间直接通信，适合每个任务只需与少数其他任务交流。  
- 典型角色：发送者（生产者）和接收者（消费者）。  
  
### 2. Collective Communication (集体通信)  
- Tasks communicate with a larger group.  
- 任务与一组任务通信。  
- 例子：广播（一个任务向所有任务发送消息），分发/收集（scatter/gather）。  
  
### 3. Centralized Management (集中式管理)  
- One task is the central coordinator.  
- 一个任务负责协调所有分布式工作者。  
- 缺点：随着任务数增多，协调者可能成为瓶颈。  
- Divide-and-conquer strategies can distribute both computation and communication load.  
- 分治策略能分散计算和通信负载。  
  
---  
  
## Communication Factors to Consider    
## 通信需要考虑的因素  
  
### 1. Synchronous vs. Asynchronous (同步 vs. 异步)  
- **Synchronous (同步/阻塞):** 任务必须等待通信完成后才能继续。  
- **Asynchronous (异步/非阻塞):** 任务在通信过程中可以做其他工作。  
  
### 2. Performance Considerations (性能考量)  
- **Processing overhead (处理开销):** 通信时间与数据处理时间的对比。  
- **Latency (延迟):** 消息从发送到接收所需的时间。  
- **Bandwidth (带宽):** 单位时间内可传输的数据量。  
  
---  
  
## Context-Specific Considerations    
## 特定情境下的考虑  
  
- 在单机多线程程序中，延迟和带宽通常不是主要瓶颈。  
- 在多台物理机的分布式系统中，系统间通信对整体性能影响很大。  
  