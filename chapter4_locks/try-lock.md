# Try-Lock    
# 尝试加锁  
  
A “try-lock” is a non-blocking version of the standard lock or mutex used in multithreaded programming.    
“尝试加锁”是在多线程编程中使用的标准锁或互斥锁的非阻塞版本。  
  
Try-lock is useful when threads have multiple tasks, and constant blocking for lock acquisition is inefficient.    
当线程有多个任务且持续阻塞以获得锁效率低时，尝试加锁非常有用。  
  
## Acquiring a Try-Lock    
## 获取尝试加锁  
  
If the mutex is available, it gets locked, and the method returns true.    
如果互斥锁可用，就会被加锁，方法返回 true。  
  
If the mutex is already held by another thread, it immediately returns false.    
如果互斥锁已被其他线程持有，会立即返回 false。  
  
This allows threads to continue with other tasks rather than waiting for the lock.    
这样线程就可以继续执行其他任务，而不是等待获得锁。  
  
## Analogies for Try-Lock    
## 尝试加锁的类比  
  
Barron and Olivia demonstrate a try-lock by representing two threads performing different tasks on their shared shopping list:    
Barron 和 Olivia 用他们的共享购物清单演示了尝试加锁，表示两个线程在执行不同任务：  
  
- Olivia searches for grocery coupons and adds items to a shared shopping list.    
  Olivia 搜索购物优惠券并向共享购物清单添加物品。  
- Barron takes inventory of the fridge and adds items to the same shared list.    
  Barron 清点冰箱并向同一购物清单添加物品。  
  
A pencil serves as their mutex, representing the lock for accessing the shopping list.    
一支铅笔作为他们的互斥锁，代表访问购物清单的锁。  
  
In a later analogy, Olivia compares try-lock to being at a house party with one shared bathroom for all guests to use.    
在后面的类比中，Olivia 把尝试加锁比作在家庭聚会时，所有客人共用一个卫生间。  
  
Guests can check to see if the bathroom is locked and, if so, return to the party and try again later rather than waiting outside an occupied bathroom.    
客人可以检查卫生间是否被锁住，如果被占用就回到聚会，稍后再来尝试，而不是在外面等着。  
  
## Advantages of Try-Lock    
## 尝试加锁的优点  
  
Try-lock provides a way to attempt lock acquisition without forcing threads into a waiting state.    
尝试加锁让线程可以尝试获取锁，而不会被迫进入等待状态。  
  
It prevents unnecessary blocking when threads have other useful tasks to perform; this is particularly useful in scenarios where threads have multiple independent tasks to perform.    
当线程还有其他有用任务时，它可以防止不必要的阻塞；在需要执行多个独立任务的场景下尤其有用。  
  
It improves efficiency by allowing threads to switch to alternative tasks when a resource is unavailable, improving resource utilization.    
通过让线程在资源不可用时切换到其他任务，尝试加锁提高了效率和资源利用率。  