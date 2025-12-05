# Computational Graphs    
# 计算图  
  
Computational graphs model relationships between program steps.    
计算图用于建模程序各步骤之间的关系。  
  
Graphs visualize which steps can be executed in parallel to help coordinate parallel execution and identify dependencies.    
图形化展示哪些步骤可以并行执行，从而协调并行执行并识别依赖关系。  
  
---  
  
## Directed Acyclic Graphs (DAGs)    
## 有向无环图（DAG）  
  
- **Nodes** represent tasks or units of work    
  节点代表任务或工作单元  
- **Directed edges** indicate progression and dependencies between tasks    
  有向边表示任务之间的进展和依赖关系  
  
**Example:**    
Barron illustrates the concept using a salad-making process:    
Barron 用制作沙拉的过程演示计算图概念：  
  
- Chop lettuce    
  切生菜  
- Chop tomatoes    
  切番茄  
- Mix ingredients    
  混合食材  
- Add salad dressing    
  加沙拉酱  
  
Chopping lettuce and tomatoes can occur asynchronously (in parallel).    
切生菜和切番茄可以异步进行（并行）。  
  
- "Spawn" node represents the start of parallel execution    
  “Spawn”节点表示并行执行的开始  
- "Sync" node ensures both chopping tasks complete before mixing    
  “Sync”节点确保两个切菜任务完成后才混合  
  
---  
  
## Key Terminology    
## 关键术语  
  
- **Spawn/fork:** Initiates parallel execution paths    
  Spawn/fork：启动并行执行路径  
- **Sync/join:** Synchronizes completion of parallel tasks    
  Sync/join：同步并行任务的完成  
- **Asynchronous:** Tasks that can occur in any order relative to each other    
  异步：任务之间可以以任何顺序发生  
- **Critical path:** Longest sequence of dependent operations in the graph    
  关键路径：图中依赖操作的最长序列  
  
---  
  
## Analyzing Parallel Potential    
## 并行潜力分析  
  
- **Work:** Total execution time on a single processor (sum of all task times)    
  Work：单处理器上所有任务时间的总和  
- **Span:** Shortest possible execution time with maximum parallelization (sum of critical path times)    
  Span：最大并行化时的最短可能执行时间（关键路径的总时间）  
- **Ideal parallelism:** Ratio of work to span, indicating maximum speed improvement    
  理想并行度：Work/Span 的比值，表示理论上的最大加速比  