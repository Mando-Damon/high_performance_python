# Reentrant Mutexes    
# 可重入互斥锁  
  
A reentrant mutex is a type of mutex that can be locked multiple times by the same thread or process.    
可重入互斥锁是一种可以被同一个线程或进程多次加锁的互斥锁。  
  
It keeps track internally of how many times it has been locked by the owning thread.    
它在内部记录拥有线程已经加锁了多少次。  
  
The reentrant mutex must be unlocked an equal number of times before another thread can acquire it.    
必须解锁同样次数后，其他线程才能获取可重入互斥锁。  
  
Reentrant mutexes are also known as "recursive mutexes" or "recursive locks" in various programming languages.    
在不同编程语言中，可重入互斥锁也被称为“递归互斥锁”或“递归锁”。  
  
## Reentrant Mutexes versus Standard Mutexes    
## 可重入互斥锁与标准互斥锁的区别  
  
Standard mutexes can lead to deadlocks if a thread tries to lock a mutex it already owns.    
如果一个线程尝试锁定自己已经拥有的标准互斥锁，可能会导致死锁。  
  
Reentrant mutexes prevent this type of deadlock by allowing multiple locks by the same thread.    
可重入互斥锁允许同一个线程多次加锁，从而避免这种死锁。  
  
## Use Cases for Reentrant Mutexes    
## 可重入互斥锁的应用场景  
  
### Nested function calls    
### 嵌套函数调用  
  
Reentrant mutexes are useful when functions that use locks are called within other locked sections of code.    
当使用锁的函数在其他加锁的代码段内被调用时，可重入互斥锁非常有用。  
  
This scenario can occur when retrofitting locks into existing code or when creating functions that use other locked functions.    
这种情况可能出现在给现有代码添加锁时，或在创建调用其他已加锁函数的函数时。  
  
### Recursive functions    
### 递归函数  
  
Reentrant mutexes are essential for recursive functions that need to lock resources.    
对于需要锁定资源的递归函数来说，可重入互斥锁是必不可少的。  
  
As the function calls itself, it can lock the mutex multiple times and then unlock it an equal number of times as it unwinds.    
随着函数自身递归调用，可以多次加锁互斥锁，并在递归展开时相应次数地解锁。  
  
## Advantages and Considerations    
## 优势与注意事项  
  
Reentrant mutexes can simplify coding by reducing concerns about what has already been locked.    
可重入互斥锁可以简化编码，减少对已加锁内容的担忧。  
  
Reentrant mutexes can facilitate easier integration of locks into existing code structures; however, there is debate in the programming community about their use, with some arguing for code refactoring to avoid nested locks instead.    
可重入互斥锁有助于更容易地将锁集成到现有代码结构中；但在编程社区中对其使用存在争议，有些人主张通过重构代码来避免嵌套锁。  