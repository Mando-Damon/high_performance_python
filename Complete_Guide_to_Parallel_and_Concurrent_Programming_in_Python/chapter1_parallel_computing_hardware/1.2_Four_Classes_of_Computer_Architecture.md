# Four Classes of Computer Architecture (Flynn’s Taxonomy)  
# 计算机体系结构的四大类（弗林分类法）  
  
Parallel computing requires parallel hardware with multiple processors. Flynn's taxonomy classifies one of four multi-processor architectures based on its instruction streams and data streams:  
  
并行计算需要配备多处理器的并行硬件。弗林分类法根据指令流和数据流，将多处理器体系结构分为以下四类：  
  
---  
  
## 1. Single Instruction, Single Data (SISD)  
### 单指令流，单数据流（SISD）  
  
- Sequential computer with a single processor unit    
  采用单个处理器的顺序计算机  
- Executes one series of instructions on one data element at a time    
  每次在一个数据元素上执行一串指令  
  
---  
  
## 2. Single Instruction, Multiple Data (SIMD)  
### 单指令流，多数据流（SIMD）  
  
- Parallel computer with multiple processing units    
  具有多个处理单元的并行计算机  
- All processors execute the same instruction simultaneously on different data elements    
  所有处理器在不同的数据元素上同时执行相同的指令  
- Well-suited for applications performing repetitive operations on large datasets (for example, image processing)    
  非常适合对大型数据集进行重复操作的应用（例如，图像处理）  
- Modern GPUs often use SIMD instructions    
  现代GPU通常采用SIMD指令  
  
---  
  
## 3. Multiple Instruction, Single Data (MISD)  
### 多指令流，单数据流（MISD）  
  
- Each processing unit executes its own series of instructions on the same data stream    
  每个处理单元在同一数据流上执行各自的指令序列  
- Not a commonly used architecture due to limited practical applications    
  由于实际应用有限，这种架构很少被采用  
  
---  
  
## 4. Multiple Instruction, Multiple Data (MIMD)  
### 多指令流，多数据流（MIMD）  
  
- Each processing unit can execute different instructions on different datasets    
  每个处理单元可以在不同的数据集上执行不同的指令  
- Most commonly used architecture found in multicore PCs, networked clusters, and supercomputers    
  是多核个人电脑、网络集群和超级计算机中最常见的架构  
  
### MIMD Subdivisions  
#### MIMD 的细分  
  
#### Single Program, Multiple Data (SPMD)  
##### 单程序，多数据（SPMD）  
  
- Multiple processing units execute copies of the same program simultaneously    
  多个处理单元同时执行同一个程序的副本  
- Processors can run asynchronously and execute different program parts based on conditional logic    
  处理器可异步运行，并根据条件逻辑执行程序的不同部分  
- The most common style of parallel programming    
  是最常见的并行编程模式  
  
#### Multiple Program, Multiple Data (MPMD)  
##### 多程序，多数据（MPMD）  
  
- Processors execute different, independent programs simultaneously on different data    
  处理器在不同的数据上同时执行不同、相互独立的程序  
- Often uses a "host" or "manager" node to distribute work to other nodes and then collect results    
  通常使用“主机”或“管理节点”分配任务至其他节点，再汇总结果  
- Less common than SPMD but useful for certain applications    
  虽然不如 SPMD 常见，但在某些应用场景下很有用  