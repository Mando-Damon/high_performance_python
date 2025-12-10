# Partitioning: Breaking Down the Problem    
# 分解：将问题拆分成多个部分  
  
---  
  
## What is Partitioning?    
什么是分解？  
  
Partitioning means dividing a problem into discrete chunks of work so they can be distributed among multiple tasks.    
分解就是把问题拆分成独立的工作块，便于分配给多个任务（或处理器）。  
  
In the early design stage, the goal is **maximum decomposition**—break the problem down as much as possible, regardless of the actual number of processors available.    
在设计早期，重点是尽可能多地分解问题，而不用考虑处理器数量等实际限制。  
  
Different decomposition methods have different advantages depending on the problem and hardware.    
不同的分解方法在不同问题和硬件下各有优劣。  
  
---  
  
## Domain (Data) Decomposition    
## 域（数据）分解  
  
- **Idea:** Split the data of the problem into small, ideally equal-sized partitions    
  思路：将问题相关的数据分割成小块，最好是等大小  
- Each partition is assigned its own computation    
  每块数据对应自己的计算任务  
  
**Example:**    
视频中的例子：装饰一盘纸杯蛋糕，可以按块分配（每人一组蛋糕），或循环分配（每人轮流拿一个蛋糕）。  
  
---  
  
## Functional Decomposition    
## 功能分解  
  
- **Idea:** Identify all the types of work (functions/steps) needed by the program    
  思路：找出程序需要完成的所有工作类型（功能/步骤）  
- Divide the overall work into distinct tasks, each performing different computations    
  将整体工作拆分为不同的任务，每个任务执行不同的计算  
  
**Example:**    
视频中的例子：制作纸杯蛋糕的流程可以拆分成配料、搅拌、烘烤、装饰等独立任务。  
  
---  
  
## Complementary Approaches    
## 互补方法  
  
- Domain and functional decomposition are complementary; often used together    
  域分解和功能分解是互补的，通常结合使用  
- Developers usually start with domain decomposition since it's the basis of many parallel algorithms    
  开发者通常先用域分解，因为它是很多并行算法的基础  
- Exploring both approaches can reveal optimization opportunities and issues that data-only decomposition might miss    
  结合两种方法能发现更多优化空间和潜在问题，仅考虑数据分解可能会遗漏  
  