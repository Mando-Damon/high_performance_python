# Agglomeration    
# 聚合（合并任务）  
  
Agglomeration is the stage in parallel programming that comes after partitioning the problem and establishing communication between tasks.    
聚合是在并行设计流程中，完成任务分解和通信建立之后的阶段。  
  
---  
  
## Granularity    
## 粒度  
  
### Fine-Grained Parallelism (细粒度并行)  
- **Definition:** Splitting a program into many small tasks    
  把程序拆分成大量的小任务  
- **Advantages:** Better load balancing across processors    
  更容易实现负载均衡  
- **Disadvantages:** High communication/synchronization overhead, low computation-to-communication ratio    
  通信和同步开销大，计算与通信比低  
  
### Coarse-Grained Parallelism (粗粒度并行)  
- **Definition:** Splitting the program into a few large tasks    
  把程序拆分成少量的大任务  
- **Advantages:** Lower communication overhead, more time for computation    
  通信开销小，计算时间多  
- **Disadvantages:** Possible load imbalance, some processors may be idle    
  易产生负载不均，一些任务可能空闲  
  
### Medium-Grained Parallelism (中等粒度并行)  
- **Definition:** A compromise between fine and coarse granularity    
  在细粒度和粗粒度之间折中  
- **Advantages:** Often most efficient for general-purpose computers    
  对通用计算机通常最有效  
  
---  
  
## Demonstration Example    
## 示例演示  
  
Barron 和 Olivia 用给纸杯蛋糕抹糖霜来说明聚合：  
  
- 12 个纸杯蛋糕，分成 12 个任务（细粒度）  
- 需要 34 次任务间通信  
- 聚合后，任务数变为可用处理器数（2个），每个任务负责 6 个蛋糕（粗粒度）  
- 通信次数减少到 2 次，但每次需交换更多信息  
  
---  
  
## Recommendations    
## 建议  
  
- 避免硬编码任务数量上限    
- 用编译期或运行时参数控制粒度  
- 设计程序能适应可用处理器数量变化（自动调整任务分配）  
  