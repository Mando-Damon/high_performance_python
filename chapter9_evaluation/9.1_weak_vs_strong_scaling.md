# Weak Scaling vs. Strong Scaling    
# 弱扩展性与强扩展性  
  
---  
  
## Weak Scaling (弱扩展性)  
  
- **Definition:** Increase the problem size as you add more processors, keeping the workload per processor constant    
  定义：增加处理器数量的同时增加问题规模，使每个处理器的工作量保持不变  
- **Purpose:** Tackle larger problems in the same amount of time    
  目的：在相同时间内处理更大规模的问题  
- **Example:**    
  例子：一个人一小时可以装饰10个纸杯蛋糕，两个人并行可以在一小时内装饰20个  
  
---  
  
## Strong Scaling (强扩展性)  
  
- **Definition:** Use more processors to solve a fixed-size problem faster    
  定义：将固定规模的问题分配给更多处理器，以更快完成任务  
- **Purpose:** Accomplish tasks more quickly    
  目的：更快完成任务  
- **Example:**    
  例子：装饰10个纸杯蛋糕，一个人需一小时，两个人并行可在约30分钟内完成  
  
---  
  
# Key Metrics in Parallel Computing    
# 并行计算关键指标  
  
## Throughput (吞吐量)  
- Measures the number of tasks completed per unit time    
  衡量单位时间内完成的任务数量  
- 增加处理器可以提升总吞吐量，例如一个工人每小时装饰10个蛋糕，三人则能装饰30个  
  
## Latency (延迟)  
- Time taken to execute a single task from start to finish    
  完成单个任务所需时间  
- 即使多处理器并行，每个蛋糕的装饰时间仍为6分钟（每个任务的延迟不变）  
  
## Speedup (加速比)  
- Ratio of sequential execution time to parallel execution time    
  顺序执行时间与并行执行时间的比值  
- 例如：一人需60分钟，两人需30分钟，加速比为2  
  
---  
  
# Limitations of Parallelization    
# 并行化的局限  
  
- Real-world programs often have both parallelizable and sequential components    
  现实中的程序通常包含可并行和必须顺序执行的部分  
- Sequential parts (如将蛋糕装入共享容器)限制最大可实现的加速比    
  顺序部分限制了最大加速，处理器数量增加时收益递减  