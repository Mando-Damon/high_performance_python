# Measuring Speedup and Efficiency    
# 测量加速比与效率  
  
---  
  
## Speedup (加速比)  
  
- **Definition:**    
  Speedup = Time for sequential execution / Time for parallel execution    
  加速比 = 顺序执行时间 / 并行执行时间  
  
- **Interpretation:**    
  - Speedup > 1 表示并行化带来了性能提升    
  - Speedup < 1 表示顺序算法更优  
  
- **Example:**    
  Barron 和 Olivia 记录了加总购物小票的时间：    
  - 顺序任务：单人加总，耗时 25 秒    
  - 并行任务：两人一起加总，耗时 17 秒    
  - 计算加速比：25 / 17 ≈ 1.47（几乎快了 1.5 倍）  
  
---  
  
## Efficiency (效率)  
  
- **Definition:**    
  Efficiency = Speedup / Number of processors    
  效率 = 加速比 / 处理器数量  
  
- **Interpretation:**    
  效率描述处理器资源的利用率  
  
- **Examples:**    
  - 两个处理器，速度提升 1.47 倍，效率为 1.47 / 2 = 73.5%    
  - 八个处理器，速度提升 2.2 倍，效率为 2.2 / 8 = 27.5%  
  
---  
  
## Benchmarking Best Practices    
## 性能测试最佳实践  
  
- 限制其他程序运行，避免资源竞争    
- 多次独立运行并取平均值，减少执行波动影响    
- 在使用即时编译（JIT）的环境下，先“热身”运行一次    
- 第一次运行用于预热和填充缓存，正式测量前再运行一次  
  