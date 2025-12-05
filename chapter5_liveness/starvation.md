# Starvation    
# 饿死现象  
  
Starvation occurs when a process or thread is perpetually denied access to the resources it needs, preventing it from progressing.    
饿死现象指的是某个进程或线程一直无法获得所需资源，导致其无法继续执行。  
  
Ideally, threads will take turns accessing shared resources, but this is not guaranteed due to how operating systems schedule thread execution.    
理想情况下，线程会轮流访问共享资源，但由于操作系统的调度方式，这并不能得到保证。  
  
A "greedy" thread frequently holding a lock on a shared resource can lead to other threads being starved out of being able to make progress.    
如果有“贪婪”的线程经常持有共享资源的锁，其他线程就会因无法获得资源而陷入饿死状态。  
  
In simple scenarios with a few equally prioritized threads, starvation is less likely to be a concern; however, thread priorities can significantly impact the likelihood of starvation:    
在只有少量优先级相同线程的简单场景下，饿死现象较少见；但线程优先级会显著影响饿死的可能性：  
  
- Higher-priority threads are generally scheduled to execute more often, and lower-priority threads may struggle to gain access to resources.    
  高优先级线程通常被调度得更频繁，低优先级线程可能难以获得资源。  
  
## Implications    
## 影响  
  
Starvation can significantly impact system performance and fairness in resource allocation.    
饿死现象会严重影响系统性能和资源分配的公平性。  
  
Designers of concurrent systems need to consider thread priorities and the number of concurrent threads to prevent starvation.    
并发系统的设计者需要考虑线程优先级和并发线程数量，以防止饿死现象。  
  
While occasional delays in resource access may be tolerable, persistent starvation can severely hamper the functionality of affected threads.    
虽然偶尔的资源访问延迟可以接受，但持续的饿死会严重影响被影响线程的功能。  