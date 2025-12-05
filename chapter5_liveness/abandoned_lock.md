# Abandoned Lock: A New Form of Deadlock    
# 被遗弃的锁：死锁的新形式  
  
An abandoned lock occurs when a thread acquires a lock on a shared resource and exits before releasing its lock on that resource, leaving other threads trying to acquire the lock to wait indefinitely.    
被遗弃的锁是指一个线程获取了共享资源的锁后，在释放该锁之前就退出，导致其他尝试获取该锁的线程无限期地等待。  
  
When a thread or process acquires a lock and then terminates unexpectedly, it may not release the lock automatically.    
当线程或进程获取锁后异常终止时，锁可能不会被自动释放。  
  
Barron and Olivia demonstrate an abandoned lock as two dining philosophers sharing a chopstick when one philosopher (Barron) abruptly leaves with one chopstick, resulting in a deadlock scenario; other tasks (represented by Olivia) become stuck, waiting indefinitely for a lock that will never be released.    
Barron 和 Olivia 通过就餐哲学家问题演示了被遗弃的锁：两位哲学家共用筷子时，Barron 突然带着一根筷子离开，导致死锁；其他任务（Olivia）就会被卡住，无限期地等待永远不会被释放的锁。  
  
Deadlocks can occur not only through resource competition but also through unexpected thread termination.    
死锁不仅可能由于资源竞争发生，还可能由于线程意外终止导致。  